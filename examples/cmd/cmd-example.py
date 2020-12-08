import nextion

display = nextion(12, 13, 9600)
print(display.cmd('t0.txt="Its running!"'))