from nextion import nextion
import time

display = nextion(12, 13, 9600)
display.brightness(50)
time.sleep_ms(500)
display.brightness(60)
time.sleep_ms(500)
display.brightness(70)
time.sleep_ms(500)
display.brightness(80)
time.sleep_ms(500)
display.brightness(90)
time.sleep_ms(500)
display.brightness(100)