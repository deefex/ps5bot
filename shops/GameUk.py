import logging
import os
from termcolor import colored
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from utils.utils import setup_browser

PS5DE_DIRECT = "https://www.game.co.uk/en/playstation-5-digital-edition-2826341"
PS5CE_DIRECT = "https://www.game.co.uk/en/playstation-5-console-2826338"


class GameUk:
    def __init__(self):
        self.url = 'https://www.game.co.uk/playstation-5'
        self.shop = colored(' [gameuk]', 'blue')
        self.driver = setup_browser()

    def check_stock(self, ps5_type):
        item = ' [%s] :: ' % ps5_type
        try:
            self.driver.implicitly_wait(60)
            self.driver.get(self.url)
            # image = self.driver.find_element_by_css_selector('img[title="HD Camera"]')  # Test for in stock item
            if ps5_type == 'ps5-digital':
                image = self.driver.find_element_by_css_selector('img[title="PlayStation 5 Digital Edition"]')
            else:
                image = self.driver.find_element_by_css_selector('img[title="PlayStation 5"]')
            parent = image.find_element_by_xpath('..')   # Find the parent
            link = parent.find_element_by_tag_name('a')  # Find the link
            if link.text.lower() == 'out of stock':
                status = colored('OUT OF STOCK', 'red')
            else:
                target = link.get_attribute('href')
                text = link.get_attribute('text').upper()
                clickable_link = f"\u001b]8;;{target}\u001b\\{text}\u001b]8;;\u001b\\"
                status = colored(clickable_link, 'green')
                os.system('say -v Fiona "Playstation 5 available at Game UK"')  # Fiona is Scottish :-)
            logging.info(self.shop + item + status)
        except NoSuchElementException as e:
            status = colored("ERROR: NoSuchElementException", 'yellow')
            logging.info(self.shop + item + status)
        except Exception as e:
            status = colored(e, 'yellow')
            logging.info(self.shop + item + status)
        finally:
            self.driver.close()


