from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from utils.utils import setup_browser, format_hyperlink, log_result

GAME_PS5_PAGE = 'https://www.game.co.uk/playstation-5'


class GameUk:
    def __init__(self):
        self.url = GAME_PS5_PAGE
        self.shop = 'game'
        self.driver = setup_browser()

    def check_stock(self, ps5_type):
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
            if link.text.lower() == 'out of stock':      # Find the link text
                status = 'OOS'
            else:
                status = format_hyperlink(link.get_attribute('href'), link.get_attribute('text').upper())
            log_result(self.shop, ps5_type, status)
        except NoSuchElementException as nsee:
            log_result(self.shop, ps5_type, nsee)
        except WebDriverException as wde:
            log_result(self.shop, ps5_type, wde)
        except Exception as e:
            log_result(self.shop, ps5_type, e)
        finally:
            self.driver.close()


