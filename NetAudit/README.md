# DNS Enumeration
## tool: dnsEnum.ps1
### requires 'hostnames.txt'

This tool will look to see if the given hostnames has an IP address. If the hostname does resolve to an IP, it prints it out.
It reads from a file list 'hostnames.txt' which has one hostname per line.

Usage:
~~~~ 
C:> dnsEnum.ps1 
~~~~

# Pingsweep
## tool: pingSweep.ps1

This will will perform a ping sweep after taking in the first argument.
It can take in two forms of arguments x.x.x.x - y.y.y.y or x.x.x.x/w.
It will only print out an IP that responded to a ping!

Usage:
~~~~ 
$ .\pingSweep.sh 10.31.1.0-10.31.2.0
$ .\pingSweep.sh 10.31.0.0/16
~~~~

# OS Classification
## tool: osClasssifier.py
### requires Scapy, ipList.txt

### Setup scapy on your machine
```
cd /tmp
git clone https://github.com/phaethon/scapy
cd scapy
sudo python3 setup.py install
```

This will classify the OS of each IP given to it. It reads from a list of IPs and classifies the Operating System on those IPs based on the ping's TTL.

~~~~
$ osClassifier.py ipList.txt
~~~~

# Extra Tool - Subdomain Lister
## tool: sublister.ps1
### requires wordlist.txt

This will read from wordlist and take an argument for the target url. It will then print out which subdomains that exist along with their IP.

~~~~
$ sublister.ps1 robinhood.com
~~~~
