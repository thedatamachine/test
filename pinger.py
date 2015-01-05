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
range1 = extractRange.group(1)
range2 = extractRange.group(2)
print "variable triplet = %s" % (triplet)
print "variable range1 = %s" % (range1)
print "variable range2 = %s\n" % (range2)
print "list of IP's to ping:"
range1 = int(range1) - 1  # allows full range for list
iplist = []
while int(range1) < int(range2):
    range1 = int(range1) + 1
    total = str(triplet) + str(range1)
    iplist.append(total)
print iplist
for i in iplist:
    p = subprocess.Popen(["ping", "-c 1", "-W .2", i], stdout=subprocess.PIPE)
    line = p.communicate()
    print(line)
# testpusher
