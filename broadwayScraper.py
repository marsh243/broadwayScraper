from bs4 import BeautifulSoup
from datetime import datetime
import urllib2

url = "https://lottery.broadwaydirect.com/"

content = urllib2.urlopen(url).read()

soup = BeautifulSoup(content, "lxml")

d = {}
shows = {}
showTimes = {}
parseInfo = {}

for link in soup.find_all('a'):
    if "lottery.broadwaydirect.com/show/" in link.get('href'):
        subContent = urllib2.urlopen(link.get('href')).read()
        subSoup = BeautifulSoup(subContent, "lxml")
        title = subSoup.title.string.split(") ")
        print title[0]+") "+link.get('href')+"\n"
        d[title[0]+")"] = link.get('href')
        table = subSoup.find_all('div', class_="row lotteries-row hide-for-tablets show-for-desktop")
        for row in table:
            info = row.text.split("\n")
        for a in info:
            print a
        #print dateTime
        print "\n"
        #shows[title[0]+")"] =
for a in d:
    print a+" "+d[a]+"\n"
