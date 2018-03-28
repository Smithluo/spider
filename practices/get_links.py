#!/usr/bin/env python
# _*_ coding:utf-8 _*_


from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from practices.get_title import get_title
import ssl,re


ssl._create_default_https_context = ssl._create_unverified_context


pages = set()


def get_links(page_url):
    global pages
    bs_obj = get_title("http://en.wikipedia.org" + page_url)
    for link in bs_obj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # 我们遇到了新页面
                new_page = link.attrs['href']
                print(new_page)
                pages.add(new_page)
                get_links(new_page)


get_links("")