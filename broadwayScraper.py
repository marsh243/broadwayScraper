from bs4 import BeautifulSoup
from datetime import datetime
import urllib2

url = "https://lottery.broadwaydirect.com/" #initial site

content = urllib2.urlopen(url).read()

soup = BeautifulSoup(content, "lxml") #read the initial site in bs4

d = {} #dictionary for show name and url
shows = {} #will be show names + all relevant details

for link in soup.find_all('a'): #for every link find the shows specifically
    if "lottery.broadwaydirect.com/show/" in link.get('href'):
        subContent = urllib2.urlopen(link.get('href')).read()
        subSoup = BeautifulSoup(subContent, "lxml") #subSoup checks each individual show
        title = subSoup.title.string.split(") ") #trim the title and put in d and shows
        print title[0]+") "+link.get('href')+"\n" #print for testing
        d[title[0]+")"] = link.get('href') #attach title to url
        table = subSoup.find_all('div', class_="row lotteries-row hide-for-tablets show-for-desktop") #find table of info
        for row in table:
            info = row.text.split("\n") #split by line
        for a in info:
            print a #print for testing (WONKY)
        print "\n"
        #shows[title[0]+")"] =
for a in d: #print list of shows and urls
    print a+" "+d[a]+"\n"
