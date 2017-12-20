import os
import time

seconds = float(0)
minutes = int(0)
hours = int(0)


run = raw_input("Press T to start")

while run.lower() == "t":
    if seconds > 59:
        seconds = 0
        minutes = minutes + 1
    if minutes > 59:
        minutes = 0
        hours = hours + 1
    os.system('cls')
    seconds = (seconds + .1)

    print (hours, ":", minutes, ":", seconds)
    time.sleep(.1)

