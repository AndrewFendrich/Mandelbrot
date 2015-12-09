# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 12:51:28 2015

@author: User
"""
import time
from multiprocessing.connection import Client
from multiprocessing.connection import Listener
address = ('localhost', 6000)


def talk(message = "",address = "broadcast"):
    print("try:")
    bstring = str.encode(address)
    try:    
        with Listener(address, authkey=b'' + bstring) as listener:
            print("with Listener(addr...")
            with listener.accept() as conn:
                message = str(listener.last_accepted)
                print('connection accepted from', listener.last_accepted)
                message = time.strftime("%Y%m%d")
                message = message + "_"
                message = message + time.strftime("%H%M%S")
                conn.send(message)
    except:
        message = "No receivers detected"
        print(message)
    return(message)
        
        
def listen():
    try:
        with Client(address, authkey=b'secret password') as conn:
            message = conn.recv()
            print(message)
    except:
        message = "No broadcasters detected"
        print(message)
    return(message)

print("Hello")
talk("Hello")
print(listen())