#!/usr/bin/env python3
# Copyright (c) 2014, alumae
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
# 
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
# 
# * Redistributions in binary form must reproduce the above copyright notice, this
#   list of conditions and the following disclaimer in the documentation and/or
#   other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Based on kaldi-gstreamer client:
# https://github.com/alumae/kaldi-gstreamer-server/blob/master/kaldigstserver/client.py
#
# Modified by 2018 Lucas Jo (Atlas Labs)
# Apache 2.0
#
# This is a client example code for Zeroth-Enterprise ASR server.
# It takes audio stream from microphone or file, and sends to Zeroth ASR server.
# Recognized result will be reported by JSON text as user speaks
#
# Client can save adaptation state reported from zeroth-gstserver 
# and it can send it to server before starting the next stream
# plz check options:
#  --save-adaptation-state
#  --send-adaptation-state

import sys
import at_mic as at
import argparse
import time
import threading
import sys
import urllib.parse
import queue
import json
import os
import audioop
import math
import logging
import logging.config
import yaml
from ws4py.client.threadedclient import WebSocketClient
import requests
import platform
import random
import re
import base64


RETRY_TIME_MIN = 2
RETRY_TIME_MAX = 3

logger = logging.getLogger(__name__)

def rate_limited(maxPerSecond):
    minInterval = 1.0 / float(maxPerSecond)
    def decorate(func):
        lastTimeCalled = [0.0]
        def rate_limited_function(*args,**kargs):
            elapsed = time.process_time() - lastTimeCalled[0]
            leftToWait = minInterval - elapsed
            if leftToWait>0:
                time.sleep(leftToWait)
            ret = func(*args,**kargs)
            lastTimeCalled[0] = time.process_time()
            return ret
        return rate_limited_function
    return decorate

class MyClient(WebSocketClient):

    def __init__(self, filename, url, pid, protocols=None, extensions=None, heartbeat_freq=None, byterate=32000, no_realtime=False,
                 save_adaptation_state_filename=None, send_adaptation_state_filename=None):
        super(MyClient, self).__init__(url, protocols, extensions, heartbeat_freq)
        self.final_hyps = []
        self.filename = filename
        self.byterate = byterate
        self.no_realtime = no_realtime
        self.final_hyp_queue = queue.Queue()
        self.save_adaptation_state_filename = save_adaptation_state_filename
        self.send_adaptation_state_filename = send_adaptation_state_filename
        self.tik0 = 0
        self.tik  = 0
        self.tok  = 0
        self.tok2 = 0
        self.total_length = 0
        self.pid = pid
        self.platform = platform.system()
        self.src_file = None
        self.sessionId = None
        self.count = 0
        self.result_file = open('./result', 'w')

    @rate_limited(4) # comment out this line to send as soon as possible
    def send_data(self, data):
        self.send(data, binary=True)
        if self.platform is "Windows":
            self.tik = time.monotonic()
        else:
            self.tik = time.clock_gettime(time.CLOCK_REALTIME)

        if self.count == 0: self.tik0 = self.tik
        self.count += 1
    
    def send_data_norate(self, data):
        self.send(data, binary=True)   
        if self.platform is "Windows":
            self.tik = time.monotonic()
        else:
            self.tik = time.clock_gettime(time.CLOCK_REALTIME)

        if self.count == 0: self.tik0 = self.tik
        self.count += 1

    def opened(self):
        logger.info("Socket opened")
        def send_data_to_ws():
            # send adaptation state
            if self.send_adaptation_state_filename is not None:
                logger.info("Sending adaptation state from %s" % self.send_adaptation_state_filename)
                try:
                    adaptation_state_props = json.load(open(self.send_adaptation_state_filename, "r"))
                    self.send(json.dumps(dict(adaptation_state=adaptation_state_props)))
                except:
                    e = sys.exc_info()[0]
                    logger.info("Failed to send adaptation state: {}".format(e))

            if self.filename != '-':
                # sending audio blocks
                try:
                    self.src_file = open(self.filename, "rb")
                except FileNotFoundError as e:
                    logger.error(e)
                    raise


                if self.no_realtime:
                    for block in iter(lambda: self.src_file.read(8000), b''):
                        self.send_data_norate(block)
                else:
                    for block in iter(lambda: self.src_file.read(int(self.byterate/4)), b''):
                        try:
                            self.send_data(block)
                        except Exception as e:
                            logger.info("exception in send_data from {}".format(self.sessionId))
                            pass


                # important: send EOS to finalize this connection
                logger.info("sending EOS")
                self.send("EOS")
                if self.platform is "Windows":
                    self.tik = time.monotonic()
                else:
                    self.tik = time.clock_gettime(time.CLOCK_REALTIME)
                logger.info("Tik")

            else:
                try:
                    with at.Microphone(sample_rate=16000) as source:
                        #---------------------------------------------------------------------
                        # Sending audio chuck from microphone
                        #   read samples from microphone stream (pyAudio)
                        #   ex) source.stream.read(samples)
                        #
                        #   need to send 32000/4=8000 byte/sec = 8000 * 8 bit/sec 
                        #                                      = 16 bit * 4000 samples/sec

                        # Parameters for end-point detection
                        energy_threshold = 300 
                        dynamic_energy_adjustment_damping = 0.15
                        dynamic_energy_ratio = 1.5
                        pause_threshold = 4
                        pause_count = 0
                        nSample = int(self.byterate/8)
                        seconds_per_buffer = nSample / float(source.SAMPLE_RATE)
                        pause_buffer_count = int(math.ceil(pause_threshold / seconds_per_buffer))

                        logger.info("Mic. is ready, you can say something with proper volume")
                        for block in iter(lambda: source.stream.read(nSample), ""):
                            self.send_data(block)

                            # Energy measurement simple SAD
                            energy = audioop.rms(block, source.SAMPLE_WIDTH)  # energy of the audio signal
                            damping = dynamic_energy_adjustment_damping ** seconds_per_buffer  # account for different chunk sizes and rates
                            target_energy = energy * dynamic_energy_ratio
                            energy_threshold = energy_threshold * damping + target_energy * (1 - damping)

                            #print >> sys.stderr, "(energy = %f, threshould = %f)" %(energy, energy_threshold)
                            if energy > energy_threshold:
                                pause_count = 0
                            else:
                                pause_count += 1
                            if pause_count > pause_buffer_count:  # end of the phrase
                                logger.info('silence detected')
                                break

                        # important: send EOS to finalize this connection
                        self.send("EOS")

                except Exception as e:
                    logger.error("[Error] Can not sent data through websocket. Reason: %s", str(e))
                    self.close()

        t = threading.Thread(target=send_data_to_ws)
        t.start()

    def received_message(self, m):
        response = json.loads(str(m))
        #logger.debug(response)
        json_data = json.dumps(response, ensure_ascii=False) # to recognize unicode hangul
        if 'objectives' in response: # NLU OUTPUT
            logger.debug("NLU JSON was: {}".format(json_data))
            if self.platform is "Windows":
                self.tok2 = time.monotonic()
            else:
                self.tok2 = time.clock_gettime(time.CLOCK_REALTIME)
            logger.debug("Tok2")
        elif 'sessionId' in response:
            self.sessionId = response['sessionId']
            logger.debug("Session ID was: {}".format(response['sessionId']))
            #self.tok = time.clock_gettime(time.CLOCK_REALTIME)
        elif 'status' in response: # ASR OUTPUT
            if response['status'] == 0:
                # log JSON reponse from the server
                if 'result' in response:
                    if 'total-length' in response:
                        self.total_length = response['total-length']
                    logger.debug("JSON was: {}".format(json_data))
                    if response['result']['final']:
                        trans = response['result']['hypotheses'][0]['transcript']
                        if self.platform is "Windows":
                            self.tok = time.monotonic()
                        else:
                            self.tok = time.clock_gettime(time.CLOCK_REALTIME)
                        logger.debug("Tok")
                
                # save adaptation stat from the server
                if 'adaptation_state' in response:
                    if self.save_adaptation_state_filename:
                        logger.info("Saving adaptation state to {}".format(self.save_adaptation_state_filename))
                        with open(self.save_adaptation_state_filename, "w") as f:
                            f.write(json.dumps(response['adaptation_state']))
            else:
                logger.info("Received error from server (status {})".format(response['status']))
                if 'message' in response:
                    logger.info("Error message: {}".format(response['message']))
        else:
            logger.debug("Undefined JSON was: {}".format(json_data))


    def get_full_hyp(self, timeout=60):
        return self.final_hyp_queue.get(timeout)

    def closed(self, code, reason=None):
        logger.info("Websocket closed() called")
        self.src_file.close()

        if reason is not None:
            logger.info("closed() is called with reason: {}".format(reason))
        delay = self.tok - self.tik
        tx_time = self.tik - self.tik0
        
        logger.info("[{}] tik = {:.2f}, tok = {:.2f}, elapsed_time ASR = {:.2f}, total-length ASR = {:.2f}".format(self.pid,
            self.tik, self.tok, delay, self.total_length))
        logger.info("[{}] tx time = {:.2f}".format(self.pid, tx_time))
        rtf = (delay + self.total_length)/self.total_length
        logger.info("[{}] real-time factor = {} from {}".format(self.pid, rtf, self.filename))

        if self.tok2 != 0:
            delay2 = self.tok2 - self.tik
            logger.info("[{}] tik = {:.2f}, tok2 = {:.2f}, elapsed_time NLU = {:.2f}, total-length NLU = {:.2f}".format(self.pid,
                self.tik, self.tok2, delay2, self.total_length))
            rtf = (delay2 + self.total_length)/self.total_length
            logger.info("[{}] real-time factor NLU = {} from {}".format(self.pid, rtf, self.filename))

            logger.info("[{}] difference between delays = {:.2f}".format(self.pid, (delay2 - delay)*1000))




        self.final_hyp_queue.put(" ".join(self.final_hyps))



intro_txt="This is an example client code for Zeroth-Enterprise ASR server.\n"
intro_txt+="It takes audio stream from microphone or files, and sends to Zeroth ASR server.\n"
intro_txt+="Recognized result will be reported by JSON text as user speaks in every 0.25 ms.\n"
intro_txt+="Client can save an adaptation state reported from the server.\n"
intro_txt+="and it can send the adaptation to server before starting the next stream.\n"

def reqToken(endpoint, authinfo):

    b64Val  = base64.b64encode(authinfo.encode()).decode()
    headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic '+b64Val }
    data    = 'grant_type=client_credentials'
    try:
        res = requests.post(endpoint, headers = headers, data=data, verify=False)
    except Exception as e:
        logger.debug('http request is faild, bypass it. error = {}'.format(e))
        return None
    
    if res.status_code != 200:
        logger.debug('predict_punctuation call is faild, bypass it')
        return None
    
    return json.loads(res.text)

def request(filename,uri='ws://13.125.20.108:3179/client/ws/trusted',rate='3200',model='',save_adaptation_state=None,send_adaptation_state=None,
            conf_path='zeroth_client.yaml',no_realtime=None,single_mode=None,retry=None):

    if filename == '-' and retry:
        logging.info("for microphone input, retry mode is no-meaning")
        sys.exit()

    # load configuration
    f_auth = False
    conf = []
    with open(conf_path) as f:
        conf = yaml.safe_load(f)
        if "logging" in conf:
            logging.config.dictConfig(conf["logging"])

        if "fork" in conf and conf["fork"] > 1:
            import tornado.process
            logging.info("Forking into %d processes" % conf["fork"])
            ret = tornado.process.fork_processes(conf["fork"], 100000)  # try 100000
            logging.debug("return of fork_processes pid:{}, task_id:{}".format(os.getpid(), tornado.process.task_id()))

        if 'auth' in conf:
            f_auth = True

    # build client websocket instance with uri information
    uri = uri

    if single_mode:
        uri += '?%s' % (urllib.parse.urlencode([("single", "true")]))
    else:
        uri += '?%s' % (urllib.parse.urlencode([("single", "false")]))
    
    # for authentication
    if f_auth:
        auth_key = reqToken(conf['auth']['endpoint'], conf['auth']['info'])
        if auth_key:
            access_token = auth_key['access_token']
            uri += '&%s' % (urllib.parse.urlencode([("access-token", access_token)]))
            uri += '&%s' % (urllib.parse.urlencode([("pos", "dvd")]))
        else:
            logger.info('Authentication failed')
            sys.exit()
   
    # for a specified model name
    if model != "":
        uri += '&%s' % (urllib.parse.urlencode([("model", model)]))
    
    # for sending raw audio type such as uncompressed PCM or stream from microphone
    # for encoded audio such as
    content_type=''
    if filename == '-' or filename.endswith(".raw"):
        content_type = "audio/x-raw, layout=(string)interleaved, rate=(int)%d, format=(string)S16LE, channels=(int)1" %(rate/2)
        uri += '&%s' % (urllib.parse.urlencode([("content-type", content_type)]))

    logger.info("URI: " + uri)
    logger.info("filename: " + filename)

    count = 0
    while True:
        ws = MyClient(
                filename,
                uri, 
                os.getpid(),
                byterate=rate,
                no_realtime=no_realtime,
                save_adaptation_state_filename=save_adaptation_state, 
                send_adaptation_state_filename=send_adaptation_state
            )

        try:
            # connect websocket
            ws.connect()
            # if there is no respons in 60 seconds, it will return
            #result = ws.get_full_hyp()
            ws.run_forever()
        except Exception as e:
            logger.error("Couldn't connect to the server. Reason: {}".format(e))
            sys.exit()

        if not retry:  break

        if 'retry_time' in conf:
            _min = float(conf['retry_time'].split(':')[0])
            _max = float(conf['retry_time'].split(':')[1])
            time.sleep(random.uniform(_min, _max))
        else:
            time.sleep(random.uniform(RETRY_TIME_MIN, RETRY_TIME_MAX))

#def main():
#    parser = argparse.ArgumentParser(description=intro_txt)
#    parser.add_argument('-u', '--uri', default="ws://13.125.20.108:3179/client/ws/trusted", dest="uri", help="Server websocket URI")
#    #parser.add_argument('-u', '--uri', default="ws://127.0.0.1:3179/client/ws/speech", dest="uri", help="Server websocket URI")
#    #parser.add_argument('-u', '--uri', default="ws://13.125.20.108:3177/client/ws/speech", dest="uri", help="Server websocket URI")
#    parser.add_argument('-r', '--rate', default=32000, dest="rate", type=int,
#            help="Rate in bytes/sec at which audio should be sent to the server. \
#                    For raw 16-bit audio it must be 2*samplerate! Set this to '-' if you don't need real-time")
#    parser.add_argument('--model', dest="model", default="", help="connect to specific model")
#    parser.add_argument('--save-adaptation-state', help="Save adaptation state to file")
#    parser.add_argument('--send-adaptation-state', help="Send adaptation state from file")
#    parser.add_argument('-c', '--conf', dest="conf", default="zeroth_client.yaml", help="configuration file (YAML)")
#    parser.add_argument('--no-realtime', dest="no_realtime", action='store_true', help='flag for testing no real-time transmission')
#    parser.add_argument('--single-mode', dest="single_mode", action='store_true',
#            help='if this flag is true, server will finalize output with the first EPD point')
#    parser.add_argument('--retry', dest="retry", action='store_true', help='flag for testing one file repeatedly')
#    parser.add_argument('filename', help="Audio filename to be sent to the server. \
#            Set this to '-' for using microphone stream")
#    args = parser.parse_args()
#    request(args.filename,args.uri,args.rate,args.model,args.save_adaptation_state,args.send_adaptation_state,
#            args.conf,args.no_realtime,args.single_mode,args.retry)
#
#
#if __name__ == "__main__":
#    main()
