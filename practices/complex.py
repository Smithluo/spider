#!/usr/bin/env python
# _*_ coding:utf-8 _*_


from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup as bs
import ssl


ssl._create_default_https_context = ssl._create_unverified_context


html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs_obj = bs(html, 'html.parser')

for sibling in bs_obj.find("img", {"src": "../img/gifts/img1.jpg"}).parent.previous_sibling:
    print(sibling)
