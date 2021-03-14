import logging
import os
import platform
from playsound import playsound
from termcolor import colored
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from utils.utils import setup_browser

ARGOS_BASE_URL = "https://www.argos.co.uk/search/"


class Argos:
    def __init__(self):
        self.url = ARGOS_BASE_URL
        self.shop = colored(' [argos]    ', 'cyan')
        self.driver = setup_browser()

    def check_stock(self, ps5_type):
        item = '::' + colored(' [%s] ' % ps5_type, 'blue') + ':: '
        if ps5_type == "ps5-digital":
            # self.url += "sony-ps4-500gb-console" # test string for success
            self.url += "sony-playstation-5-digital-console/"
        if ps5_type == "ps5-console":
            self.url += "sony-playstation-5-console/"
        try:
            # self.driver.implicitly_wait(60)
            self.driver.get(self.url)

            # find the product list
            product_list = self.driver.find_element_by_css_selector('div[data-test="product-list"]')
            # If the button is a[data-test="component-button"] kind="secondary", text="More details" - OUT OF STOCK
            # If the button is button[data-test="component-att-button"] kind="primary" - IN STOCK
            product_button = product_list.find_element_by_css_selector('a[data-test="component-button"]')
            if product_button.get_attribute('text').lower() == "more details":
                status = colored('OUT OF STOCK', 'red')
                logging.info(self.shop + item + status)
        except NoSuchElementException as e:
            try:
                # We're here on the assumption we couldn't find a secondary button (link)
                product_list = self.driver.find_element_by_css_selector('div[data-test="product-list"]')
                product_button = product_list.find_element_by_css_selector('button[data-test="component-att-button"]')
                target = self.url
                text = "IN STOCK - Buy Now"
                clickable_link = f"\u001b]8;;{target}\u001b\\{text}\u001b]8;;\u001b\\"
                status = colored(clickable_link, 'green')
                if platform.system() == 'Darwin':
                    os.system('say -v Fiona "Playstation 5 available at Argos"')
                else:
                    playsound('sounds/woohoo.mp3')
                logging.info(self.shop + item + status)
            except NoSuchElementException as e:
                # If we can't find the button, barf and move on
                status = colored("ERROR: NoSuchElementException (nested)", 'yellow')
                logging.info(self.shop + item + status)
        except WebDriverException as wde:
            status = colored(wde, 'yellow')
            logging.info(self.shop + item + status)
        except Exception as e:
            status = colored(e, 'yellow')
            logging.info(self.shop + item + status)
        finally:
            self.driver.close()
