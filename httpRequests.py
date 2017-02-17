#!/usr/bin/python
import socket
import urllib

def connection(host, port):
    s = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s

"""Get the flag by doing a POST request
"""
def getFlag(host, port):
    flag = ""
    request = "POST / HTTP/1.1\n"
    reqHost = "Host: 54.209.150.110\n\n"
    s = connection(host,port)
    s.send(request + reqHost)
    while True:
        response = s.recv(1024)
        if response: 
            flag = response
        break
    flag = flag.split()[len(flag.split())-1][:-1]
    s.close()
    return flag

def getToken(host, port):
    token = ""
    request = "POST /getSecure HTTP/1.1\n"
    reqHost = "Host: 54.209.150.110\n\n"
    cLife = "Connection: keep-alive\n\n"
    s = connection(host,port)
    s.send(request + reqHost + cLife)
    while True:
        response = s.recv(1024)
        if response: 
            token = response
        break
    token = token.split()[len(token.split())-1][:-1]
    s.close()
    return token

def getFlag2(host, port, token):
    flag = ""
    request = "POST /getFlag2 HTTP/1.1\n"
    reqHost = "Host: "+host+"\n\n"
    cLife = "Connection: keep-alive\n\n" 
    token = "token="+token+"\n\n"
    cType = "Content-Type: application/x-www-form-urlencoded\n"
    cLength = "Content-Length: {}\n\n".format(len(token)-2)
    s = connection(host,port)
    s.send(request + reqHost + cType + cLength + cLife + token)
    while True:
        response = s.recv(1024)
        print response
        if response:
            flag = response
        break
    flag = flag.split()[len(flag.split())-1][:1]
    s.close()
    return flag
    
        

def main():
    host = '54.209.150.110'
    port = 80
    print("Activity 1: " + getFlag(host, port))
    print getToken(host, port)
    print("Activity 2: " + getFlag2(host, port, getToken(host, port)))

main()
