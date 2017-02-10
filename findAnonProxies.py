#58.176.46.248 is anon
#72.55.180.117 as well
import requests

ip = requests.get( 'http://ip.42.pl/raw').text
print 'this is your ip: ' + ip
s = requests.Session()
proxy_ip = s.get('http://ip.42.pl/raw',proxies={'http':'111.13.109.27'}).text

print 'this is your new ip: ' + proxy_ip

if ip != proxy_ip:
    print 'yay'
elif ip == proxy_ip:
    print 'nay'


for i in range(129,255):
    for j in range(21,255):
        for k in range(1,255):
            for l in range (39,255):
                url = "http://{}.{}.{}.{}".format(i,j,k,l)
                urls= "https://{}.{}.{}.{}".format(i,j,k,l)
                #url = "'" + url + "'"
                print "trying " + url
                try:
                    proxy = s.get('http://ip.42.pl/raw', timeout=5, proxies={'http':url, 'https':urls})
                    print proxy.text + " connected! \nNow to see if it's anonymous..."
                    if not proxy.headers.get("X-Forwarded-For"):
                        print "YAY WE FOUND ONE"
                    else:
                        print "Darn :("
                except requests.exceptions.ConnectTimeout:
                    print "Nope"
                except requests.exceptions.ProxyError:
                    print "Nope Nope!"
                except requests.exceptions.ConnectionError:
                    print "Connection Error, oh no!"
                print"\n" 
                 
                 
                 
                 
                 
                 
                 proxy_ip=s.get('https://ip.42.pl/raw',proxies={'http':url}).text
                print proxy_ip
#                s=requests.Session()
 
                proxy_ip = s.get('http://ip.42.pl/raw',proxies={'http':url}).text

#                print proxy_ip
"""

