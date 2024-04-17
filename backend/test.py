import socket
import os
import re
import subprocess
 
print('[+] Choice')
print('1 - Scan Network')
 
hosts = []
choice = int(input())
ip = "10.144.1."
x= 0
if choice == 1:
    while x<=500:
        p = subprocess.Popen('ping ' +ip+str(x) +" -n 1" ,stdout=subprocess.PIPE, shell=True)
        out, error = p.communicate()
        out = str(out)
        find = re.search("Destination host unreachable",out)
        if find is None:
            hosts.append(ip+str(x))
            print("[*] Host found")
        x = x + 1
print("+----------------------+")
print("|     hosts:           |")
print("+----------------------+")
for host in hosts:
    try:
        name, a ,b =socket.gethostbyaddr(host)
    except:
        name = "Not Found"
    print('| '+host + " | " + name)