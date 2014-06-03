import xml.etree.ElementTree as ElementTree
import urllib2
import re
import webbrowser

PAGE_SIZE = 10
CHANNEL = 0
TITLE = 0
LINK = 1
INDEX = 0
DESC = 2


def main():
    begin = raw_input("Would you like to browse CDs or DVDs?  ")

    if begin == "CD" or begin == "CDs":
        cd_xml = urllib2.urlopen("http://cuyahogalibrary.org/feedData/newCDMusic.xml")
        xml_tree = cd_xml
    else:
        dvd_xml = urllib2.urlopen("http://sciron.cuyahoga.lib.oh.us/feeds/newdvds.xml")
        xml_tree = dvd_xml

    tree = ElementTree.parse(xml_tree)
    root = tree.getroot()[CHANNEL]

    items = root.findall("item")

    i = 0
    while i < (len(items) / PAGE_SIZE):
        try:
            for x in xrange(0, PAGE_SIZE):
                idx = i * PAGE_SIZE + x
                print "[{0}] {1} \n".format(idx, re.split("\[|/", items[idx][TITLE].text)[0])
            repeat = True
            while repeat:
                inp = raw_input("\nItem #, 'next', or 'quit':  ")
                if inp in ["next", ""]:
                    repeat = False
                elif inp == "back":
                    repeat = False
                    if i > 0:
                        i -= 2
                elif inp in ["quit", 'q']:
                    return None
                elif inp.isdigit() or '?' in inp:
                    if '?' in inp:
                        num = int(inp.split("?")[INDEX])
                        print items[num][TITLE].text, '\n'
                        print items[num][DESC].text.split('>')[-1], '\n'
                    else:
                        webbrowser.open(items[int(inp)][LINK].text)
                else:
                    continue
        except UnicodeEncodeError:
            pass
        i += 1

if __name__ == "__main__":
    main()