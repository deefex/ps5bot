from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from utils.utils import setup_browser, format_hyperlink, log_result

CURRYS_BASE_URL = 'https://www.currys.co.uk/gbuk/sony-gaming/console-gaming/console-gaming/consoles/634_4783_32541_49_xx/xx-criteria.html'


class Currys:
    def __init__(self):
        self.url = CURRYS_BASE_URL
        self.shop = 'currys'
        self.driver = setup_browser()

    def check_stock(self, ps5_type):
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
                status = 'OOS'
            else:
                status = format_hyperlink(target, 'IN STOCK')
            log_result(self.shop, ps5_type, status)
        except NoSuchElementException as nsee:
            log_result(self.shop, ps5_type, nsee)
        except WebDriverException as wde:
            log_result(self.shop, ps5_type, wde)
        except Exception as e:
            log_result(self.shop, ps5_type, e)
        finally:
            self.driver.close()


