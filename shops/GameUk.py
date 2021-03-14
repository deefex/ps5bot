import logging
import os
import platform
from playsound import playsound
from termcolor import colored
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from utils.utils import setup_browser

GAME_PS5_PAGE = 'https://www.game.co.uk/playstation-5'


class GameUk:
    def __init__(self):
        self.url = GAME_PS5_PAGE
        self.shop = colored(' [game]     ', 'cyan')
        self.driver = setup_browser()

    def check_stock(self, ps5_type):
        item = '::' + colored(' [%s] ' % ps5_type, 'blue') + ':: '
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
                if platform.system() == 'Darwin':
                    os.system('say -v Fiona "Playstation 5 available at Game UK"')
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


