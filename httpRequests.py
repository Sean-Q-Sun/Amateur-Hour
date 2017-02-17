#!/usr/bin/python
import socket
import urllib


""" Connect to the host on the port
"""
def connection(host, port):
    s = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s

def getItem(s):
    item = "";
    while True:
        response = s.recv(1024)
        if response:
            item = response
        break
    item = item.split()[len(item.split())-1][:-1]
    return item 

def getFlag1(host, port):
    request = "POST / HTTP/1.1\n"
    reqHost = "Host: "+host+"\n\n"
    s = connection (host, port)
    s.send(request + reqHost)
    return getItem(s)
    s.close()

def getFlag2(host, port):
    request = "POST /getSecure HTTP/1.1\n"
    reqHost = "Host: "+host+"\n"
    s = connection(host, port)
    s.send(request + reqHost +"Connection: keep-alive\n\n")
    token = getItem(s)
    s.close()

    request = "POST /getFlag2 HTTP/1.1\n"
    s = connection(host, port)

    token = "token="+token+"\n\n"
    cType = "Content-Type: application/x-www-form-urlencoded\n"
    cLength = "Content-Length: {}\n\n".format(len(token)-2)
    s.send(request + reqHost + cType + cLength + token)
    return getItem(s)
    s.close()

def getFlag3(host, port):
    request = "POST /getSecure HTTP/1.1\n"
    reqHost = "Host: "+host+"\n"
   s = connection(host,port)
    s.send(request + reqHost + "Connection: keep-alive\n\n")
    token = getItem(s)
    s.close()

    request = "POST /getFlag3Challenge HTTP/1.1\n"
    reqHost = "Host: "+host+"\n"
    s = connection(host,port)
    
    token = "token="+token+"\n\n"
    cType = "Content-Type: application/x-www-form-urlencoded\n"
    cLength = "Content-Length: {}\n\n".format(len(token)-2)
    #print (request + reqHost + cType + cLength + token)
    s.send(request + reqHost + cType + cLength + token)
    s.close()
    
    answer = eval(getItem(s))
    print answer
    solution = "solution=" + str(answer) + "\n\n"
    print solution
    token = "&token=" + token[6:]
    cLength = "Content-Length: {}\n\n".format(len(token+solution)-2)
     
    print (request + reqHost + cType + cLength + token + solution)
    s.send(request + reqHost + cType + cLength + token + solution)
    return request



def main():
    host = '54.209.150.110'
    port = 80
    print "Activity 1 Flag = " + getFlag1(host, port)
    print "Activity 2 Flag = " + getFlag2(host, port)
    
    #print "Activity 3 Flag = " + i
    getFlag3(host, port) 
main()
