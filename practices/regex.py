#!/usr/bin/env python
# _*_ coding:utf-8 _*_


from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import ssl,re


ssl._create_default_https_context = ssl._create_unverified_context


html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs_obj = bs(html, "html.parser")
images = bs_obj.findAll("img", {"src": re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
for image in images:
    print(image["src"])


