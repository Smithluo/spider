#!/usr/bin/env python
# _*_ coding:utf-8 _*_


from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup as bs
import ssl


ssl._create_default_https_context = ssl._create_unverified_context


def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs_obj = bs(html, "html.parser")
    except AttributeError as e:
        return None
    return bs_obj


title = get_title("https://en.wikipedia.org/wiki/Main_Page")
if title is None:
    print("Title could not be found")
else:
    print(title)


# 在 getTitle 函数里面，我们像前面那样检查了 HTTPError，
# 然后把两行 BeautifulSoup 代码封装在一个 try 语句里面。
# 这两行中的任何一 行有问题，AttributeError 都可能被抛出(如果服务器不存在，html 就是一个 None 对象，
# html.read() 就会抛出 AttributeError)