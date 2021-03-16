# ps5bot
Playstation 5 Stock Monitor

Note: The purpose of this bot is to passively monitor stock across several UK retailers, giving you an audible alert,
and a clickable hyperlink when stock is detected. There's no automated purchasing or any scalping shenanigans.

## Installation
Have a copy of python 3.8.x
- `git clone git@github.com:deefex/ps5bot.git`
- `cd ps5bot`
- `python -m venv venv`
- `. venv/bin/activate`
- `pip install -r requirements.txt`

## Check some things before you run
Use the following scripts to check whether some key elements will work on your machine:

- `python utils/link_check.py` This will check whether you can see clickable hyperlinks in your terminal emulator
- `python utils/sound_check.py` This will check whether you can hear audible notifications on your machine

## Execution (web-based bot)
- `python web_bot.py`

This will run the main (web) bot - a headless version of chrome, and it'll report status on the command line.

## Execution (link-based bot)
- `python link_bot.py`

This primarily uses the python 'requests' package, circumventing traditional browser approaches to try to ascertain 
whether direct product URLs are being redirected to 'out of stock' or 'generic' pages

## Issues/TODO
- Perhaps use espeak for Linux platform
- playsound is a pain for the supporting packages it needs (PyObjC) - alternatives?
