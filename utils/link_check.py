from termcolor import colored

target = 'http://example.com/'
text = 'CLICK HERE'
clickable_link = f"\u001b]8;;{target}\u001b\\{text}\u001b]8;;\u001b\\"
click_me = colored(clickable_link, 'green')
print('\nIf you are running this in a terminal emulator such as iTerm2, GNOME Terminal, Tillix, etc.')
print('You should be able to cmd-click (or ctrl-click) on this -->', click_me, '\n')
