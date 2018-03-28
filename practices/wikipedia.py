#!/usr/bin/env python
# _*_ coding:utf-8 _*_


from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup as bs
import ssl,re,datetime,random


ssl._create_default_https_context = ssl._create_unverified_context
random.seed(datetime.datetime.now())

'''
程序的主函数首先把起始页面 https://en.wikipedia.org/wiki/Kevin_Bacon 里的词条链接列表 (links 变量)设置成链接列表。
然后用一个循环，从页面中随机找一个词条链接标签并抽 取 href 属性，
打印这个页面链接，再把这个链接传入 getLinks 函数，重新获取新的链接
列表。
'''


def get_links(article_url):
    try:
        html = urlopen("https://en.wikipedia.org" + article_url)
    except HTTPError as e:
        return None
    try:
        bs_obj = bs(html, "html.parser")
        items = bs_obj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
    except AttributeError as e:
        return None
    else:
        return items


links = get_links("/wiki/Main_Page")
while (len(links)) > 0:
    new_article = links[random.randint(0, len(links)-1)].attrs["href"]
    print(new_article)
    links = get_links(new_article)