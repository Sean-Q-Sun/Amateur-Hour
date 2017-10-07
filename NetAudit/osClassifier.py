from scapy.all import *
from scapy.layers.inet import IP, ICMP


with open('ipList.txt') as f:
    for line in f:
        packet = IP(dst=line)/ICMP()
        resp = sr1(packet, timeout=2, verbose = 0)
        if resp == None:
            pass
        elif IP in resp:
            if resp.getlayer(IP).ttl <= 64:
                os = "Linux"
            elif resp.getlayer(IP).ttl <= 128:
                os = "Windows"
            elif resp.getlayer(IP).ttl <= 255:
                os = "FreeBSD"
            print (line,": TTL:",resp.getlayer(IP).ttl,": OS: ", os)
            
