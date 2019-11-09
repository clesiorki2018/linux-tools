#!/usr/bin/env python3
# extend-ip-by-CIDR.py
#
# @Author Clesiorki
# Created in november 8, 2019
#
# extends a IP/CIDR in yours IPs 
# only ipv4
#
# Example: python3 extend-ip-by-CIDR.py 192.168.0.0/24

import sys

def help():
    print('\
        extends a IP/CIDR in yours IPs\n\
        only ipv4\n\
        \n\
        Example: python3 extend-ip-by-CIDR.py 192.168.0.0/24')


def calc_hosts_from_CIDR(CIDR):
    return 2**(32 - CIDR)


def increment(ip):
    prefix = ip.split('.')[0]
    a = ip.split('.')[1]
    b = ip.split('.')[2]
    c = ip.split('.')[3]

    prefix = int(prefix)
    a = int(a)
    b = int(b)
    c = int(c)

    if c == 255:
        c = 0
        if b == 255:
            b = 0
            if a == 255:
                a = 0
                prefix += 1
            else:
                a += 1
        else:
            b += 1
    else:
        c += 1

    return str(prefix)+'.'+str(a)+'.'+str(b)+'.'+str(c)
    

def generate(ip,number):
    ips = [ip]

    for i in range(number):
        j = increment(ips[-1])
        ips.append(j)

    return ips

def dump(ips):
    for ip in ips:
        if ip.split('.')[-1] != '0' and ip.split('.')[-1] != '255':
            print(ip)

if len(sys.argv) != 2:
    help()
    sys.exit(1)

else:
    ip = sys.argv[1].split('/')[0]
    mask = sys.argv[1].split('/')[1]
    mask = int(mask)
    number = calc_hosts_from_CIDR(mask)
    ips = generate(ip, number)
    dump(ips)


