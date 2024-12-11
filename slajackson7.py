import time
import playsound
from playsound import playsound
def countup(t):
    while t:
        mins,secs = divmod(t,60)
        timer = "{:02d} : {:02d}".format(mins,secs)
        print(timer,end="\r")
        time.sleep(1)
        t += 1
    print("fire in the hole")
    playsound("lula-alexandre-de-moraes.mp3")
x = int(input("tempo em segundos negão\n"))
# function call
countup(x)