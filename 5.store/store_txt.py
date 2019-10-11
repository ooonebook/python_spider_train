import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/explore'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36\
 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
}
html = requests.get(url, headers=headers).text
# print(html)
doc = pq(html)

# file = open('explore.txt')

items = doc('.ExploreSpecialCard.ExploreHomePage-specialCard').items()
for item in items:
#     # print(item.find()text())
    print('最新专题【%s】' %(item('.ExploreSpecialCard-title').text()))
    sub_items = item('.ExploreSpecialCard-contentItem').items()
    for sub_item in sub_items:
        print('        Tag<%s> Titile<%s>' %(\
                sub_item('.ExploreSpecialCard-contentTag').text(),\
                sub_item('.ExploreSpecialCard-contentTitle').text()))
