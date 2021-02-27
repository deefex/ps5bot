import logging
import random
import requests
import traceback
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
from itertools import cycle
from lxml.html import fromstring
from fake_useragent import UserAgent

FREE_PROXY_LIST = 'https://free-proxy-list.net/'

FREE_ELITE_PROXIES = ['185.94.191.100:3128']


def setup_browser():
    chrome_options = webdriver.ChromeOptions()
    # proxy = '185.94.191.100:3128'
    # proxy = select_random_proxy()
    # print("DEBUG: ", proxy)
    chrome_options.add_argument("--headless")
    ua = UserAgent()
    chrome_options.add_argument(f'user-agent={ua.random}')
    # chrome_options.add_argument("--proxy-server=http://%s" % proxy)
    chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    return webdriver.Chrome(options=chrome_options)


def select_random_proxy():
    response = requests.get(FREE_PROXY_LIST)
    parser = fromstring(response.text)
    proxy_list = set()
    for x in parser.xpath('//tbody/tr')[:10]:
        if x.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([x.xpath('.//td[1]/text()')[0], x.xpath('.//td[2]/text()')[0]])
            proxy_list.add(proxy)
    # return proxy_list
    return random.choice(tuple(proxy_list))


def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)8s :: %(message)s',
                        datefmt='%d-%m-%y %H:%M:%S')


def shutdown_logging():
    logging.shutdown()
