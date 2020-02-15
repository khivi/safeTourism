#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

def headline_cleanup(headline):
    if headline.find('| ') > 0:
        headline = headline.replace('| ', ' ')
    if headline.find('? ') > 0:
        headline = headline.replace('? ', ' ', 1)
    if headline.find('! ') > 0:
        headline = headline.replace('! ', ' ')
    return headline

def google_news_main(location):
    url = 'https://news.google.com/search?q={}&hl=en-IN&gl=IN&ceid=IN%3Aen'.format(location)
    r = requests.get(url)
    print(location)
#    print(r)
    html_doc = r.content
    soup = BeautifulSoup(html_doc, 'html.parser')
    #article class
    s = soup.find_all('article')
    open('headlines.txt', 'w').close()
    f = open('headlines.txt', 'a')
    for x in range(len(s)):
        body = s[x].find_all('a')
        p = list(body[1].children)
#        print(p[0])
        headline = headline_cleanup(p[0])
        f.write(headline.encode('ascii', 'ignore').decode('ascii')+ '. \n')
    f.close()
    
#google_news_main('bengaluru')
