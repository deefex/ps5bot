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

CURRYS_PS5DE = 'https://www.currys.co.uk/gbuk/gaming/console-gaming/consoles/sony-playstation-5-digital-edition-825-gb-10205198-pdt.html'
CURRYS_BASE_URL = 'https://www.currys.co.uk/gbuk/sony-gaming/console-gaming/console-gaming/consoles/634_4783_32541_49_xx/xx-criteria.html'


class Currys:
    def __init__(self):
        self.url = CURRYS_BASE_URL
        self.shop = colored(' [currys]', 'blue')
        self.driver = setup_browser()

    def check_stock(self, ps5_type):
        item = ' [%s] :: ' % ps5_type
        try:
            self.driver.implicitly_wait(60)
            self.driver.get(self.url)

            product_list = self.driver.find_element_by_css_selector('div[data-component="product-list-view"]')
            products = product_list.find_elements_by_css_selector('article[class="product result-prd"]')
            product = product_list.find_element_by_css_selector('article[class="product result-prd"]')
            image = product.find_element_by_tag_name('img')
            if len(products) == 1 and image.get_attribute('alt') == "PlayStation 4 - 500 GB":
                status = colored('OUT OF STOCK', 'red')
            else:
                target = link.get_attribute('href')
                text = "IN STOCK - Buy Now"
                clickable_link = f"\u001b]8;;{target}\u001b\\{text}\u001b]8;;\u001b\\"
                status = colored(clickable_link, 'green')
                os.system('say -v Fiona "Playstation 5 available at Currys"')
            logging.info(self.shop + item + status)
        except NoSuchElementException as e:
            status = colored("ERROR: NoSuchElementException", 'yellow')
            logging.info(self.shop + item + status)
        except Exception as e:
            status = colored(e, 'yellow')
            logging.info(self.shop + item + status)
        finally:
            self.driver.close()


