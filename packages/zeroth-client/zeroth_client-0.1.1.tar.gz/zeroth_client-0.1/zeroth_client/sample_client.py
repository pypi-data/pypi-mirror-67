#!/usr/bin/env python3
import client_module as client
import argparse

intro_txt="This is an example client code for Zeroth-Enterprise ASR server.\n"
intro_txt+="It takes audio stream from microphone or files, and sends to Zeroth ASR server.\n"
intro_txt+="Recognized result will be reported by JSON text as user speaks in every 0.25 ms.\n"
intro_txt+="Client can save an adaptation state reported from the server.\n"
intro_txt+="and it can send the adaptation to server before starting the next stream.\n"

def main():
    parser = argparse.ArgumentParser(description=intro_txt)
    parser.add_argument('-u', '--uri', default="ws://13.125.20.108:3179/client/ws/trusted", dest="uri", help="Server websocket URI")
    #parser.add_argument('-u', '--uri', default="ws://127.0.0.1:3179/client/ws/speech", dest="uri", help="Server websocket URI")
    #parser.add_argument('-u', '--uri', default="ws://13.125.20.108:3177/client/ws/speech", dest="uri", help="Server websocket URI")
    parser.add_argument('-r', '--rate', default=32000, dest="rate", type=int,
            help="Rate in bytes/sec at which audio should be sent to the server. \
                    For raw 16-bit audio it must be 2*samplerate! Set this to '-' if you don't need real-time")
    parser.add_argument('--model', dest="model", default="", help="connect to specific model")
    parser.add_argument('--save-adaptation-state', help="Save adaptation state to file")
    parser.add_argument('--send-adaptation-state', help="Send adaptation state from file")
    parser.add_argument('-c', '--conf', dest="conf", default="zeroth_client.yaml", help="configuration file (YAML)")
    parser.add_argument('--no-realtime', dest="no_realtime", action='store_true', help='flag for testing no real-time transmission')
    parser.add_argument('--single-mode', dest="single_mode", action='store_true',
            help='if this flag is true, server will finalize output with the first EPD point')
    parser.add_argument('--retry', dest="retry", action='store_true', help='flag for testing one file repeatedly')
    parser.add_argument('filename', help="Audio filename to be sent to the server. \
            Set this to '-' for using microphone stream")
    args = parser.parse_args()
    client.request(args.filename,args.uri,args.rate,args.model,args.save_adaptation_state,args.send_adaptation_state,
            args.conf,args.no_realtime,args.single_mode,args.retry)


if __name__ == "__main__":
    main()
