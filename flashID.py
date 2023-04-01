#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import serial
import serial.tools.list_ports
import os
import sys
import logging
import argparse
import random
import pprint
import time
import datetime
import time
import requests

# Configure logging
logging.basicConfig(
   format="%(asctime)s %(levelname)s %(filename)s:%(funcName)s():%(lineno)i: %(message)s",
   datefmt="%Y-%m-%d %H:%M:%S",
   level=logging.DEBUG)
logger = logging.getLogger(__name__)

# define URL
url = 'https://pwid-helper-backend-lg7dh2p2uq-as.a.run.app/rasp'

def loop(serial_port: str) -> None:
   # loop forever
   while True:
        # try to open the serial port
        try:
           with serial.Serial(serial_port, 115200, timeout=1) as ser:
               #print("Press Ctrl-C to stop")
               #print("--------------------")
               ser.write(b"0\r")


               try:
                   # loop forever
                   while True:
                       # read a line from the serial port
                       line = ser.readline().decode('utf-8').strip()


                       # if the read was successful, do something with it
                       if line == "5":
                           print(f"{line}")
                           request_message = {'id':line, 'long':103.8494183, 'lat':1.2975488}
                           response = requests.post(url, json = request_message)
                           response_message = response.text + "\r"
                           print(response_message.encode('utf-8'))
                           ser.write(response_message.encode('utf-8'))

               except KeyboardInterrupt:
                   print()
                   print("kthxbye")
                   break
                   
        except serial.SerialException:
            # if unable to open port (not plugged in), then retry after 2 seconds
            print(serial_port, " not detected")
            time.sleep(2);
        
        except KeyboardInterrupt:
           print()
           print("port never opened, goodbye")


def main() -> None:


   # Parse arguments
   # parser = argparse.ArgumentParser()
   # parser.add_argument("port", nargs="?")
   # args = parser.parse_args()
   # args_port = args.port
   args_port = "/dev/ttyACM0"
   #print(f"Using serial port: {args_port}")

# check if serial port works, if not then wait for serial port to start
   loop(args_port)




if name == "__main__":
   main()
