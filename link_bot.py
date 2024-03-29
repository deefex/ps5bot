import requests
import sys
import time
from fake_headers import Headers
from utils.utils import setup_logging, format_hyperlink, log_result

# Direct links for the products in question
GAME_PS5DE = "https://www.game.co.uk/en/playstation-5-digital-edition-2826341"
GAME_PS5CE = "https://www.game.co.uk/en/playstation-5-console-2826338"
GAME_BUND1 = "https://www.game.co.uk/en/playstation-5-digital-edition-ps5-media-remote-player1-tee-l-2850624"
GAME_BUND2 = "https://www.game.co.uk/en/playstation-5-digital-edition-ps5-hd-camera-player1-tee-l-2850623"
GAME_BUND3 = "https://www.game.co.uk/en/playstation-5-digital-edition-gameware-starter-kit-player1-tee-m-2850619"
GAME_DEFAULT = "https://www.game.co.uk/playstation-5"

ARGOS_PS5DE = "https://www.argos.co.uk/product/8349024"
ARGOS_PS5CE = "https://www.argos.co.uk/product/8349000"
ARGOS_DEFAULT = "https://www.argos.co.uk/vp/oos/ps5.html"

CURRYS_PS5DE = 'https://www.currys.co.uk/gbuk/gaming/console-gaming/consoles/sony-playstation-5-digital-edition-825-gb-10205198-pdt.html'
CURRYS_DEFAULT = "https://www.currys.co.uk/gbuk/gaming/console-gaming/consoles/634_4783_32541_xx_xx/xx-criteria.html"

# Data structures to pass into the link checker
game = {
    'name': 'game',
    'fail_url': GAME_DEFAULT,
    'items': [
        {'link': GAME_PS5DE, 'name': 'ps5de-console'},
        {'link': GAME_PS5CE, 'name': 'ps5ce-console'},
        {'link': GAME_BUND1, 'name': 'ps5de-bundle1'},
        {'link': GAME_BUND2, 'name': 'ps5de-bundle2'},
        {'link': GAME_BUND3, 'name': 'ps5de-bundle3'},
    ]
}

argos = {
    'name': 'argos',
    'fail_url': ARGOS_DEFAULT,
    'items': [
        {'link': ARGOS_PS5DE, 'name': 'ps5de-console'},
        {'link': ARGOS_PS5CE, 'name': 'ps5ce-console'},
    ]
}

currys = {
    'name': 'currys',
    'fail_url': CURRYS_DEFAULT,
    'items': [
        {'link': CURRYS_PS5DE, 'name': 'ps5de-console'},
    ]
}


# The link checker (duh!)
def link_checker(shop):
    shop_name = shop['name']
    fail_url = shop['fail_url']
    for item in shop['items']:
        item_name = item['name']
        headers = Headers(headers=True).generate()
        try:
            response = requests.get(item['link'], allow_redirects=True, headers=headers, timeout=5)
            if response.status_code == 200 and response.url == fail_url:
                status = 'OOS'
                log_result(shop_name, item_name, status)
            elif response.status_code == 200 and response.url != fail_url:
                status = format_hyperlink(item['link'], 'IN STOCK')
                log_result(shop_name, item_name, status)
            elif response.status_code == 404:
                log_result(shop_name, item_name, 'PAGE NOT FOUND')
            else:
                log_result(shop_name, item_name, 'ERROR: RESPONSE CODE ' + str(response.status_code))
        except requests.exceptions.Timeout as t:
            log_result(shop_name, item_name, 'TIMEOUT')
        except requests.exceptions.TooManyRedirects as t:
            log_result(shop_name, item_name, str(t))
        except requests.exceptions.RequestException as e:
            log_result(shop_name, item_name, str(e))


if __name__ == '__main__':
    setup_logging()

    try:
        while True:
            link_checker(game)
            link_checker(argos)
            link_checker(currys)
            time.sleep(3)
    except KeyboardInterrupt as kbi:
        print("Keyboard Interrupt. Exiting link_bot.py...")
        sys.exit(1)
