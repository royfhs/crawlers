import urllib, re

print urllib.urlopen('http://www.ishadowsocks.com/').getcode()

urllib.urlretrieve('http://www.ishadowsocks.com/',filename='ss.html')

ss = open("ss.html","r+").read()
m = re.search(r'us1\.iss\.tf',ss, re.M).span()[0]
if m:
	print "Password:",
	print ss[m+68:m+76]
	raw_input()
else:
	print "error"
	raw_input()