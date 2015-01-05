import re
import subprocess

ip = raw_input("Enter IP Range : ")
print ""
validip = re.search(
    r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)-(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b',
    ip, re.IGNORECASE)  # regex to verify input is in a valid format
extractRange = re.match(r'\d*.\d*.\d*.(\d{1,3})-(\d{1,3})', ip, re.IGNORECASE)
extractTriplet = re.match(r'\d{1,3}.\d{1,3}.\d{1,3}.', ip, re.IGNORECASE)
triplet = extractTriplet.group()  # extracted groups
range1 = int(extractRange.group(1))
range2 = int(extractRange.group(2))
print "triplet = %s" % (triplet)
print "range1 = %s" % (range1)
print "range2 = %s\n" % (range2)
print "list of IP's to ping:"
iplist = []
while range1 <= range2:
    iplist.append(str(triplet) + str(range1))
    range1 += 1
print iplist
for i in iplist:
    p = subprocess.Popen(["ping", "-c 1", "-W .2", i], stdout=subprocess.PIPE)
    line = p.communicate()
    print(line)
