#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import urlopen
from BeautifulSoup import BeautifulSoup
import random
from collections import OrderedDict


url = "http://quotes.yourdictionary.com/theme/marriage/"

stran = urlopen(url).read()

soup = BeautifulSoup(stran)

print("Hi, here are 5 random quotes about marriage:")
print""


quote = soup.findAll("div", attrs={"class": "item quote_pic"})
quote_selection = random.sample(quote, 5)

for quote in quote_selection:
    print quote.p.string.strip()
    print ("(" + quote.span.small.text.strip() + ")").title()   #title() capitalizes names
    print ""

