#  Author: Paul McELroy
#  Based off of basic code on the ZMQ guide
#  by Daniel Lundin:
##  Lazy Pirate server
##  Binds REQ socket to tcp://*:5555
##  Like hwserver except:
##   - echoes request as-is
##   - randomly runs slowly, or exits to simulate a crash.
##
##   Author: Daniel Lundin <dln(at)eintr(dot)org>
##

from __future__ import print_function

from random import randint
import time
import os
import zmq
import zmq.auth
from zmq.auth.thread import ThreadAuthenticator

context = zmq.Context(1)
base_dir = os.path.dirname(__file__)
public_keys_dir = os.path.join(base_dir, 'public_keys')
secret_keys_dir = os.path.join(base_dir, 'private_keys')

auth = ThreadAuthenticator(context)
auth.start()
auth.allow('127.0.0.1')
auth.configure_curve(domain='*', location=public_keys_dir)

server_secret_file = os.path.join(secret_keys_dir, "server.key_secret")
server_public, server_secret = zmq.auth.load_certificate(server_secret_file)

server = context.socket(zmq.REP)

server.curve_secretkey = server_secret
server.curve_publickey = server_public
server.curve_server = False
server.bind("tcp://*:5555")

cycles = 0

# EXAMPLE COMMAND MESSAGE:
cM = {
      "message_id": "067c8c59-710a-4c15-8265-b7f1e49b828c",
      "message_type": "command",
      "robot_id": "067c8c59-710a-4c15-8265-b7f1e49b828c",
      "timestamp": 1509748526.3482552,
      "configuration_id": "067c8c59-710a-4c15-8265-b7f1e49b828c",
      "session_id": "067c8c59-710a-4c15-8265-b7f1e49b828c",
      "instructions": [
        {
          "value": 0.10666666666666667,
          "actuator_id": "067c8c59-710a-4c15-8265-b7f1e49b828c",
          "ttl": 1.412,
          "type": "static"
        },
        {
          "value": 0.10666666666666667,
          "actuator_id": "067c8c59-710a-4c15-8265-b7f1e49b828c",
          "ttl": 1.412,
          "type": "static"
        },
        {
          "value": 0.10666666666666667,
          "actuator_id": "067c8c59-710a-4c15-8265-b7f1e49b828c",
          "ttl": 1.412,
          "type": "static"
        }
      ]
    }

#Example AcknowledgementMessage
aM = {
      "message_id": "067c8c59-710a-4c15-8265-b7f1e49b828c",
      "message_type": "acknowledgement",
      "timestamp": 1509748526.3482552
}


while True:
    try:
        request = server.recv_json()
        cycles += 1
        message_type = request["message_type"]
        print("I: Normal request (%s)" % request)
        if(message_type == "acknowledgement"):
            server.send_json(cM)
            print("sending command")
        elif(message_type == "acknowledgement"):
            server.send_json(cM)
            print("sending acknowledgement")

    except KeyboardInterrupt:
        print("END")
        break
auth.stop()
server.close()
context.term()
