import threading
from threading import *
import time
dict = {}
def create(key, value, timeout=0):
    if key in dict:
        print("error: this key already exists")
    elif (key.isalpha()):
        if len(dict) < (1024 * 1020 * 1024) and value <= (
                    16 * 1024 * 1024):
            l = [value, timeout] if timeout == 0 else [value, time.time() + timeout]
            if len(key) <= 32:
                dict[key] = l
        else:
            print("Memory limit exceeded")
    else:
        print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")
def read(key):
    if key not in dict:
        print("error: given key does not exist in database. Please enter a valid key")
    else:
        b = dict[key]
        if b[1] != 0 and time.time() < b[1] or b[1] == 0:
            return str(key) + ":" + str(
                    b[0])
        else:
            print("error: time-to-live of", key, "has expired")
def delete(key):
    if key not in dict:
        print("error: given key does not exist in database. Please enter a valid key")
    else:
        b = dict[key]
        if b[1] != 0 and time.time() < b[1] or b[1] == 0:
            del dict[key]
            print("key is successfully deleted")
        else:
            print("error: time-to-live of", key, "has expired")
