from nextion import nextion
import time
time.sleep(1)
display = nextion(12, 13, 9600)
display.page(1)