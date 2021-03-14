import logging
from selenium import webdriver
from fake_useragent import UserAgent


def setup_browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    ua = UserAgent()
    chrome_options.add_argument(f'user-agent={ua.random}')
    chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    return webdriver.Chrome(options=chrome_options)


def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)8s :: %(message)s',
                        datefmt='%d-%m-%y %H:%M:%S')


def shutdown_logging():
    logging.shutdown()
