from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from utils.utils import setup_browser, format_hyperlink, log_result

ARGOS_BASE_URL = "https://www.argos.co.uk/search/"


class Argos:
    def __init__(self):
        self.url = ARGOS_BASE_URL
        self.shop = 'argos'
        self.driver = setup_browser()

    def check_stock(self, ps5_type):
        if ps5_type == "ps5-digital":
            # self.url += "sony-ps4-500gb-console" # test string for success
            self.url += "sony-playstation-5-digital-console/"
        if ps5_type == "ps5-console":
            self.url += "sony-playstation-5-console/"
        try:
            self.driver.implicitly_wait(60)
            self.driver.get(self.url)

            # find the product list
            product_list = self.driver.find_element_by_css_selector('div[data-test="product-list"]')
            # If the button is a[data-test="component-button"] kind="secondary", text="More details" - OUT OF STOCK
            # If the button is button[data-test="component-att-button"] kind="primary" - IN STOCK
            product_button = product_list.find_element_by_css_selector('a[data-test="component-button"]')
            if product_button.get_attribute('text').lower() == "more details":
                status = 'OOS'
                log_result(self.shop, ps5_type, status)
        except NoSuchElementException as nsee1:
            try:
                # We're here on the assumption we couldn't find a secondary button (link)
                product_list = self.driver.find_element_by_css_selector('div[data-test="product-list"]')
                product_button = product_list.find_element_by_css_selector('button[data-test="component-att-button"]')

                # There's no url to yield as it's an 'add to trolley' button so take the original search result url
                status = format_hyperlink(self.url, 'IN STOCK')
                log_result(self.shop, ps5_type, status)
            except NoSuchElementException as nsee2:
                # If we can't find the button, barf and move on
                log_result(self.shop, ps5_type, nsee2)
        except WebDriverException as wde:
            log_result(self.shop, ps5_type, wde)
        except Exception as e:
            log_result(self.shop, ps5_type, e)
        finally:
            self.driver.close()
