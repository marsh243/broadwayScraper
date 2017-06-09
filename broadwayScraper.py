from bs4 import BeautifulSoup
from datetime import datetime
import urllib3

http = urllib3.PoolManager()

url = "https://lottery.broadwaydirect.com/"  # initial site

response = http.request('GET', url)

soup = BeautifulSoup(response.data, "lxml")  # read the initial site in bs4

d = {}  # dictionary for show name and url
shows = {}  # will be show names + all relevant details
info = {}
for link in soup.find_all('a'):  # for every link find the shows specifically
    if "lottery.broadwaydirect.com/show/" in link.get('href'):
        subResponse = http.request('GET', (link.get('href')))
        subSoup = BeautifulSoup(subResponse.data, "lxml")  # subSoup checks each individual show
        title = subSoup.title.string.split(") ")  # trim the title and put in d and shows
        # test = 1 if "CHICAGO" in title[0] else 0 an example on time differences for chicago showings
        print(test, "\n")
        print(title[0] + ") " + link.get('href') + "\n")  # print for testing
        d[title[0] + ")"] = link.get('href')  # attach title to url
        rows = subSoup.find_all('div', class_="row lotteries-row hide-for-tablets show-for-desktop")
        for row in rows:
            columns = row.find_all('div')
            dateTime = [x for x in columns[0].text.split(' ') if x not in ['', '\n']]
            status = [x for x in columns[1].text.split(' ') if x not in ['', '\n']]
            tickets = [x for x in columns[2].text.split(' ') if x not in ['', '\n']]
            price = [x for x in columns[3].text.split(' ') if x not in ['', '\n']]
            print(dateTime, " ", status, " ", tickets, " ", price, "\n")
        # shows[title[0]+")"] =
for a in d:  # print list of shows and urls
    print(a, " ", d[a], "\n")
