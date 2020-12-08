from nextion import nextion
display = nextion(12, 13, 9600)
display.cmd('t0.txt="Its running!"')