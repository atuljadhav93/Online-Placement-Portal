import time

def countdown(t):
    while t:
        mins, secs = divmod(t,60)
        timer = '{:2d}:{:2d}'.format(mins,secs)
        print(timer,end="\r")
        time.sleep(1)
        t -= 1
    print("test Ended...")

countdown(60)