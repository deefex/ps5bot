# ps5bot
Playstation 5 Stock Monitor

Note: The purpose of this bot is to passively monitor stock across several UK retailers, giving you an audible alert,
and a clickable hyperlink when stock is detected. Nothing more.

## Installation
Have a copy of python 3.8.x
- `git clone git@github.com:deefex/ps5bot.git`
- `cd ps5bot`
- `python -m venv venv`
- `. venv/bin/activate`
- `pip install -r requirements.txt`

## Execution
- `python main.py`

This will run the main bot - a headless version of chrome and it'll report status on the command line.

- `python direct_link_checks.py`

This primarily uses the python 'requests' package, circumventing traditional browser approaches to try to ascertain 
whether direct product URLs are being redirected to 'out of stock' or 'generic' pages

## Issues/TODO
- The audible alerts will only work on MacOS (I think)
- Rotating random (free) proxies is possible, but the  response times are pitiful
