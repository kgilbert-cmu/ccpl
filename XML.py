import xml.etree.ElementTree as ET
import urllib2
import re

DVD_XML = urllib2.urlopen("http://sciron.cuyahoga.lib.oh.us/feeds/newdvds.xml")
CD_XML = urllib2.urlopen("http://cuyahogalibrary.org/feedData/newCDMusic.xml")

PAGE_SIZE = 10
CHANNEL = 0

tree = ET.parse(DVD_XML)
root = tree.getroot()[CHANNEL]

DVDs = root.findall("item")

for i in xrange(0,len(DVDs) / PAGE_SIZE):
    try:
        for x in xrange(0, PAGE_SIZE):
            idx = i * PAGE_SIZE + x
            print "[{0}] {1} \n".format(idx, re.split("\[|/", DVDs[idx][0].text)[0])
    except UnicodeEncodeError:
        pass