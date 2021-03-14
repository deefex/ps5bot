import logging
import os
import platform
from playsound import playsound
from termcolor import colored
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from utils.utils import setup_browser

CURRYS_BASE_URL = 'https://www.currys.co.uk/gbuk/sony-gaming/console-gaming/console-gaming/consoles/634_4783_32541_49_xx/xx-criteria.html'


class Currys:
    def __init__(self):
        self.url = CURRYS_BASE_URL
        self.shop = colored(' [currys]   ', 'cyan')
        self.driver = setup_browser()

    def check_stock(self, ps5_type):
        item = '::' + colored(' [%s] ' % ps5_type, 'blue') + ':: '
        try:
            self.driver.implicitly_wait(60)
            self.driver.get(self.url)

            product_list = self.driver.find_element_by_css_selector('div[data-component="product-list-view"]')
            product_list_images = product_list.find_elements_by_css_selector('div[class="productListImage"]')

            # Could be enough to check whether 'playstation-4' or playstation-5' is present/absent in link href
            ps5_found: bool = False
            target = ""
            for pli in product_list_images:
                link = pli.find_element_by_css_selector('a[class="imgC"]')
                if 'playstation-5' in link.get_attribute('href'):
                    ps5_found = True
                    target = link.get_attribute('href')
            if not ps5_found:
                status = colored('OUT OF STOCK', 'red')
            else:
                text = "IN STOCK - Buy Now"
                clickable_link = f"\u001b]8;;{target}\u001b\\{text}\u001b]8;;\u001b\\"
                status = colored(clickable_link, 'green')
                if platform.system() == 'Darwin':
                    os.system('say -v Fiona "Playstation 5 available at Currys"')
                else:
                    playsound('sounds/woohoo.mp3')
            logging.info(self.shop + item + status)
        except NoSuchElementException as nsee:
            status = colored(nsee, 'yellow')
            logging.info(self.shop + item + status)
        except WebDriverException as wde:
            status = colored(wde, 'yellow')
            logging.info(self.shop + item + status)
        except Exception as e:
            status = colored(e, 'yellow')
            logging.info(self.shop + item + status)
        finally:
            self.driver.close()


