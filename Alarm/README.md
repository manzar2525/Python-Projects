## Alam Program using python

### In this program below packages of python has been used
  1. datetime   (to get the current time)
  2. sleep      (to put the program into sleep for 30 second. It implies that the program will check for the alarm time every minute twice.)
  3. mixer      (to play the audio when alarm time and current time matches.)

### Code
```
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
 ```
