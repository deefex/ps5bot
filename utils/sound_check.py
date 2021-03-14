import os
import platform
from playsound import playsound

# If you're on a Mac use the cool notification, otherwise use playsound
if platform.system() == 'Darwin':
    os.system('say -v Fiona "Holey moley, I have found a PlayStation 5"')
else:
    playsound('sounds/woohoo.mp3')