from microbit import *

i = Image("09990:00900:00900:00900:09990")
u = Image("09090:09090:09090:09090:09990")

while True:
    display.show(i)
    sleep(500)
    display.show(Image.HEART)
    sleep(500)
    display.show(u)
    sleep(500)

