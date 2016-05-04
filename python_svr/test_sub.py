import subscriber as sub
import time
import zmq

def print_msg(topic, msg):
    print topic, msg

ip = "127.0.0.1"
port = 8690
list_of_topics = ['simulator']
topic_to_callback_map = dict([("simulator", print_msg)])

s = sub.Subscriber(ip, port, list_of_topics, topic_to_callback_map)

for i in range(3):
        s.recv_message("simulator")

all_msg = s.get_messages("simulator")
print all_msg
