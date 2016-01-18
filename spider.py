# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 21:17:44 2016

@author: zhicheng.qi
gramophone官网的爬虫，暂时爬feature这个栏目，只爬第一页
第一版
"""

import requests
from bs4 import BeautifulSoup
list_page = 'http://www.gramophone.co.uk/features/all'
r = requests.get(list_page)

soup = BeautifulSoup(r.text)

news_list = soup.findAll("div", {"class": "node-article-layout"})
for item in news_list:
    title = item.find('h2').get_text()
    link = item.find('h2').find('a')['href']
    link = list_page + link
    introduction = item.findAll('p', {'class': 'tuck-down'})[0].get_text()
    print('标题:', title)
    print('介绍:', introduction)
    print('链接:', link)
    print('\n')

# detail_page = 'http://www.gramophone.co.uk/feature/my-music-john-bercow'

# r = requests.get(detail_page)
# soup = BeautifulSoup(r.text)

# sub_heading = soup.find('h2',{'class' : 'sub-heading'}).get_text()
