import sys
from shops.GameUk import GameUk
from shops.Currys import Currys
from shops.Argos import Argos
from utils.utils import setup_logging

if __name__ == '__main__':

    try:
        while True:
            setup_logging()

            gameUk = GameUk()
            gameUk.check_stock('ps5-digital')
            gameUk = GameUk()
            gameUk.check_stock('ps5-console')

            currys = Currys()
            currys.check_stock('ps5-anytype')

            argos = Argos()
            argos.check_stock('ps5-digital')
            argos = Argos()
            argos.check_stock('ps5-console')
    except KeyboardInterrupt:
        print("Keyboard Interrupt. Exiting web_bot.py...")
        sys.exit(1)
