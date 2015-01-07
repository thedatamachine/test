import re
import socket
import os
import urllib2
import time


def cls():
    """
clears interpretor window
    """
    os.system(['clear', 'cls'][os.name == 'nt'])


def behind_firewall_on():
    try:
        urllib2.urlopen('http://17.209.197.81', timeout=1)
        return True
    except urllib2.URLError as err:
        pass
    return False


def prompt1():
    res = raw_input("Cannot reach internal network, press any key to continue or 'q' to quit\n")
    if res == "q":
        exit()
    else:
        pass

def mainloop():
    if not behind_firewall_on():
        prompt1()
    ip = raw_input("Enter IP Range : ")
    print ""
    validip = re.search(
        r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)-(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b',
        ip, re.IGNORECASE)
    if not validip:
        cls();
        print "%s is an invalid Range. Example Format xxx.xxx.xx-xx" % ip
        mainloop();
    extractrange = re.match(r'\d*.\d*.\d*.(\d{1,3})-(\d{1,3})', ip, re.IGNORECASE)
    extracttriplet = re.match(r'\d{1,3}.\d{1,3}.\d{1,3}.', ip, re.IGNORECASE)
    triplet = extracttriplet.group()  # extracted groups
    range1 = int(extractrange.group(1))
    range2 = int(extractrange.group(2))
    iplist = []
    while range1 <= range2:
        iplist.append(str(triplet) + str(range1))
        range1 += 1
    for i in iplist:
        try:
            print(socket.gethostbyaddr(i))
        except socket.herror as e:
            print "no connection"
    res = raw_input("Press any key to scan again or 'q' to quit")
    if res == "q":
        exit()
    else:
        cls()
        mainloop();


cls();
mainloop();
