import requests
from urllib.parse import urlencode
import time
import datetime
import os
from hashlib import md5
import sys


# https://www.toutiao.com/api/search/content/?
# aid=24&app_name=web_search&offset=80&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1570714203381

# set-cookie:tt_webid=6747648672941819395; Max-Age=7776000

url_main= 'https://www.toutiao.com'
url_base = 'https://www.toutiao.com/api/search/content/?'
keywords = '街拍'

IMAGE_DIR = "IMAGES"

headers = {
    # ':authority': 'www.toutiao.com',
    # ':method': 'GET',
    # ':path': '/api/search/content/?aid=24&app_name=web_search&offset=0&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1570798418357',
    # ':scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, sdch, br',
    'accept-language': 'zh-CN,zh;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'tt_webid=6746164670426629639; WEATHER_CITY=%E5%8C%97%E4%BA%AC; s_v_web_id=8d8433390d3aee87ae5a6cb96d963329; __tasessionId=fzh0st3791570798377742; csrftoken=68530614f1bd1c4343bbd1c13b017932; tt_webid=6746164670426629639',
    'upgrade-insecure-requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
    #'X-Requested-With': 'XMLHttpRequest',
}

session = requests.Session()

def session_init():
    try:
        response = session.get(url_main, headers=headers)
        if response.status_code == 200:
            # print(response.headers)
            # print(response.request.headers)
            print(response.text)
            return True
        else:
            return False
    except requests.ConnectionError as e:
        print('Error', e.args)


def get_page(offset):
    t = time.time()
    params = {
        'aid': '24',
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': keywords,
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis',
        'timestamp':  round(t * 1000),
    }
    url = url_base + urlencode(params)
    try:
        response = session.get(url, headers=headers)
        if response.status_code == 200:
            # print(response.headers)
            print(response.request.headers)
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)

def test_get_page():
    url = 'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=0&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1570799471521'
    try:
        response = session.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)

def get_images(json):
    if json.get('data'):
        for item in json.get('data'):
            title = item.get('title')
            images = item.get('image_list')
            if images:
                for image in images:
                    yield {
                        'image': image.get('url'),
                        'title': title,
                    }

def save_image(item):
    image_dir = IMAGE_DIR+os.path.sep+item.get('title')
    if not os.path.exists(image_dir):
        os.mkdir(image_dir)
    try:
        response = requests.get(item.get('image'))
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(image_dir, md5(response.content).hexdigest(),'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image')

if __name__ == "__main__":
    if not os.path.exists(IMAGE_DIR):
        os.mkdir(IMAGE_DIR)

    if session_init() == True: 
        print('Session init Success')
    else:
        print('Session init Fail')
        sys.exit()

    print('Session init success')

#     json = get_page(0)
#     # json = test_get_page()
#     for image_item in get_images(json):
#         print('title[%s] url[%s]'%(image_item.get('title'), image_item.get('image')))
#         save_image(image_item)
    json = get_page(0)
    print(json)