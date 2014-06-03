import xml.etree.ElementTree as ET
import urllib2
DVDs = urllib2.urlopen("http://sciron.cuyahoga.lib.oh.us/feeds/newdvds.xml")
CDs = urllib2.urlopen("http://cuyahogalibrary.org/feedData/newCDMusic.xml")

CHANNEL = 0

tree = ET.parse(DVDs)
root = tree.getroot()[CHANNEL]

for child in root:
    if child.tag == "item":
        try:
            print child[0].text, '\n'
        except:
            pass