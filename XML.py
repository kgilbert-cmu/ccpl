import xml.etree.ElementTree as ET
import urllib2
import re
import webbrowser

PAGE_SIZE = 10
CHANNEL = 0
TITLE = 0
LINK = 1


def main():
    begin = raw_input("Would you like to browse CDs or DVDs?  ")

    if begin == "CD" or begin == "CDs":
        CD_XML = urllib2.urlopen("http://cuyahogalibrary.org/feedData/newCDMusic.xml")
        XML_TREE = CD_XML
    else:
        DVD_XML = urllib2.urlopen("http://sciron.cuyahoga.lib.oh.us/feeds/newdvds.xml")
        XML_TREE = DVD_XML

    tree = ET.parse(XML_TREE)
    root = tree.getroot()[CHANNEL]

    items = root.findall("item")

    for i in xrange(0, len(items) / PAGE_SIZE):
        try:
            for x in xrange(0, PAGE_SIZE):
                idx = i * PAGE_SIZE + x
                print "[{0}] {1} \n".format(idx, re.split("\[|/", items[idx][TITLE].text)[0])
            repeat = True
            while (repeat):
                inp = raw_input("\nItem #, 'next', or 'quit':  ")
                if inp in ["next", ""]:
                    repeat = False
                elif inp in ["quit", 'q']:
                    return None
                elif inp.isdigit():
                    webbrowser.open(items[int(inp)][LINK].text)
                else:
                    continue
        except UnicodeEncodeError:
            pass

if __name__ == "__main__":
    main()