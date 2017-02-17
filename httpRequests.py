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
    return s.recv(1024).split()[len(s.recv(1024).split())-1][:-1]


def getFlag1(host, port):
    request = "POST / HTTP/1.1\n"
    reqHost = "Host: "+host+"\n\n"
    s = connection (host, port)
    s.send(request + reqHost)
    return getItem(s)

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
    s.send(request + reqHost + cType + cLength + token)
    
    solution = "solution=" + str(eval(getItem(s)))
    token = "&token=" + token[6:]
    cLength = "Content-Length: {}\n\n".format(len(solution + token)-2)
    s = connection(host, port)
    s.send(request + reqHost + cType + cLength + solution + token)
    return getItem(s)

def getFlag4(host, port):
    request = "POST /getSecure HTTP/1.1\n"
    reqHost = "Host: "+host+"\n"
    s = connection(host,port)
    s.send(request + reqHost + "Conncetion: keep-alive\n\n")
    token = getItem(s)
    s.close()
    token = "&token="+token+"\n\n" 
    
    request = "POST /createAccount HTTP/1.1\n"
    s = connection(host,port)
    login = "username=chaim" +token
    cType = "Content-Type: application/x-www-form-urlencoded\n"
    cLength = "Content-Length: {}\n\n".format(len(login)-2)
    userAgent = "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko\n"
    accept = "Accept: text/html,application/xhtml+xml,appliaction/xml;q=0.9,*/*;q=0.8\n"
    lang = "Accept-Language: en-US,en;q=0.5\n"
    encoding = "Accept-Encoding: gzip, deflate\n"
    s.send(request + reqHost + userAgent + accept + lang + encoding + cType + cLength + login)

    password = ""
    while True:
        password = s.recv(1024)
        if password:
            password = password.split(' ')[-1].strip('\"').strip()
        break
    
    request = "POST /login HTTP/1.1\n"
    s = connection(host,port)
    login = "username=chaim" +"&password="+ urllib.quote_plus(password)+token
    cLength = "Content-Length: {}\n\n".format(len(login)-2)
 
    s.send(request + reqHost + userAgent + accept + lang + encoding + cType + cLength + login)
    
    return getItem(s)

def main():
    host = '54.209.150.110'
    port = 80
    print "Activity 1 Flag = " + getFlag1(host, port)
    print "Activity 2 Flag = " + getFlag2(host, port)
    print "Activity 3 Flag = " + getFlag3(host, port) 
    print "Activity 4 Flag = " + getFlag4(host, port)

main()
