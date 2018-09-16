from time import gmtime, strftime
import time
import os

f = open("request-log.txt", "a")
hostname = "google.com"

response = os.system("ping -c 1 " + hostname)
date = strftime("%Y-%m-%d %H:%M:%S", gmtime())

if response != 0:
    f.write("NETWORK DOWN at " + date + "\n")
