import datetime
from time import sleep
from pygame import mixer

hour=int(input("Please enter the hour: "))
min=int(input("Please enter the minute: "))
am=input("Please enter am or pm: ")
mixer.init()
mixer.music.load("honey_singh.wav")

if am == "pm":
    hour +=12
    while True:
       # print(f"Current Time is        {currentTime.hour}:{currentTime.minute}")
        if hour==datetime.datetime.now().hour and min== datetime.datetime.now().minute:
            print("playing music")
            mixer.music.play(2)
            sleep(60)
            break
        else:
            sleep(30)