import vlc
import sys
import time
import datetime
import os

os.chdir("./Media")

args = sys.argv
try:
    m = str(args[1])
    time_to_play = None
    if len(args) > 2:
        time_to_play = str(args[2])
except:
    print("Wrong arguments! Should be:\npython3 sync.py <filename> <time>[format: HH:MM:SS]")
    exit(1)

# Setting up Media
player = vlc.MediaPlayer()

media = vlc.Media(m)

player.set_media(media)


#calculate time
if (time_to_play != None):
    now = (time.localtime(time.time()))
    now_H = int(time.strftime("%H", now))
    now_M = int(time.strftime("%M", now))
    now_S = int(time.strftime("%S", now))
    target_H = int(time_to_play[0:2])
    target_M = int(time_to_play[3:5])
    target_S = int(time_to_play[6:8])
    now_in_seconds = (now_H*60*60 + now_M*60 + now_S )
    target_in_seconds = (target_H*60*60 + target_M*60 + target_S) 
    if target_in_seconds - now_in_seconds >= 0:
        seconds_to_wait = target_in_seconds - now_in_seconds
    else:
        seconds_to_wait = 24*60*60 - now_in_seconds + target_in_seconds

    print(time.strftime("Time at excecution: %H:%M:%S", now))
    print("Seconds to wait:")

    while(seconds_to_wait > 0):
        print(seconds_to_wait)
        seconds_to_wait -= 1
        time.sleep(1)


player.play()
time.sleep(0.05)
duration = player.get_length()
player.play()
time.sleep(duration)
# time.sleep(media.get_duration())