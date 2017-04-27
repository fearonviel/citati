#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import urlopen
from BeautifulSoup import BeautifulSoup
import random

url = "http://quotes.yourdictionary.com/theme/marriage/"

stran = urlopen(url).read()

soup = BeautifulSoup(stran)

#for link in soup.findAll("a"):
#    if '/marriage' in link:
#        print link

print("Hi, here are 5 random quotes about marriage:")
print""
vsi_citati = soup.findAll("p", attrs={"class": "quoteContent"})
selekcija_citatov = random.sample(vsi_citati, 5)
for citat in selekcija_citatov:
    print citat.string.strip()

