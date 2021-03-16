import logging
import os
import platform
from selenium import webdriver
from termcolor import colored
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


def format_hyperlink(target: str, text: str) -> str:
    clickable_link = f"\u001b]8;;{target}\u001b\\{text}\u001b]8;;\u001b\\"
    return colored(clickable_link, 'green')


def log_result(shop, item, status):
    formatted_shop = colored(f'[{shop}]', 'cyan')
    formatted_item = colored(f'[{item}]', 'blue')
    if status == 'OOS':
        formatted_status = colored('OUT OF STOCK', 'red')
        logging.info(formatted_shop + ' :: ' + formatted_item + ' :: ' + formatted_status)
    elif '\u001b' in status:
        formatted_status = colored(status, 'green')
        logging.info(formatted_shop + ' :: ' + formatted_item + ' :: ' + formatted_status)
        play_audible_alert()
    else:
        formatted_status = colored(status, 'yellow')
        logging.error(formatted_shop + ' :: ' + formatted_item + ' :: ' + formatted_status)


def play_audible_alert():
    if platform.system() == 'Darwin':
        os.system('say -v Fiona "Playstation 5 located"')
    else:
        playsound('sounds/woohoo.mp3')