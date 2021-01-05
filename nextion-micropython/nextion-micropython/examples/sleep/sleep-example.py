from nextion import nextion
import time

time.sleep(2)

display = nextion(12, 13, 9600)
display.sleep(1)

time.sleep(2)

display.sleep(0)