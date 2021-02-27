import logging
import os
import requests
import time
from termcolor import colored
from fake_useragent import UserAgent
from utils.utils import setup_logging

GAME_PS5DE = "https://www.game.co.uk/en/playstation-5-digital-edition-2826341"
GAME_PS5CE = "https://www.game.co.uk/en/playstation-5-console-2826338"
GAME_PS5DE_BUNDLE1 = "https://www.game.co.uk/en/playstation-5-digital-edition-ps5-media-remote-player1-tee-l-2850624"
GAME_PS5DE_BUNDLE2 = "https://www.game.co.uk/en/playstation-5-digital-edition-ps5-hd-camera-player1-tee-l-2850623"
GAME_NOSTOCK = "https://www.game.co.uk/playstation-5"

ARGOS_PS5DE = "https://www.argos.co.uk/product/8349024"
ARGOS_PS5CE = "https://www.argos.co.uk/product/8349000"
ARGOS_NOSTOCK = "https://www.argos.co.uk/vp/oos/ps5.html"

CURRYS_PS5DE = 'https://www.currys.co.uk/gbuk/gaming/console-gaming/consoles/sony-playstation-5-digital-edition-825-gb-10205198-pdt.html'
CURRYS_NOSTOCK = "https://www.currys.co.uk/gbuk/gaming/console-gaming/consoles/634_4783_32541_xx_xx/xx-criteria.html"

# https://game.queue-it.net/?c=game&e=liveps&t=https%3A%2F%2Fwww.game.co.uk%2Fen%2Fplaystation-5-digital-edition-2826341%3Ft_origqs%3D&cid=en-GB


def check_link(url, product, fail_url):
    item = ' [%s] :: ' % product
    # ua = UserAgent()
    # header = {'User Agent': ua.random}
    # header = {'User Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36'}
    response = requests.get(url, allow_redirects=True)
    if response.status_code == 200 and response.url == fail_url:
        status = colored('OUT OF STOCK', 'red')
        logging.info(shop + item + status)
    elif response.status_code == 200 and response.url != fail_url:
        target = url
        text = 'IN STOCK - CLICK HERE'
        clickable_link = f"\u001b]8;;{target}\u001b\\{text}\u001b]8;;\u001b\\"
        status = colored(clickable_link, 'green')
        logging.info(shop + item + status)
        os.system('say -v Fiona "Playstation 5 available"')
    elif response.status_code == 404:
        status = colored('PAGE NOT FOUND', 'yellow')
        logging.info(shop + item + status)
    else:
        error = "ERROR: RESPONSE CODE " + str(response.status_code)
        status = colored(error, 'yellow')
        logging.info(shop + item + status)


if __name__ == '__main__':
    setup_logging()
    # shop = colored(' [gameuk]', 'blue')

    while True:
        shop = colored(' [gameuk]', 'blue')
        check_link(GAME_PS5DE, 'ps5de-console', GAME_NOSTOCK)
        check_link(GAME_PS5CE, 'ps5ce-console', GAME_NOSTOCK)
        check_link(GAME_PS5DE_BUNDLE1, 'ps5de-bundle1', GAME_NOSTOCK)
        check_link(GAME_PS5DE_BUNDLE2, 'ps5de-bundle2', GAME_NOSTOCK)

        # shop = colored(' [argos]', 'blue')
        # check_link(ARGOS_PS5DE, 'ps5de-console', ARGOS_NOSTOCK)
        # check_link(ARGOS_PS5CE, 'ps5ce-console', ARGOS_NOSTOCK)

        shop = colored(' [currys]', 'blue')
        check_link(CURRYS_PS5DE, 'ps5de-console', CURRYS_NOSTOCK)

        time.sleep(1)
