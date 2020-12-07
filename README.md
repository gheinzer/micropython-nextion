# micropython nextion library
 This library will help you control you nextion-display over UART.
## How to use
First, define an object with the class `nextion(tx_pin, rx_pin, baudrate)`
This could look like this now:<br>
`from nextion import nextion<br>
display = nextion(13, 12, 9600)`<br>
Now you can control the device with different commands.
## Constants
- `nextion.WRITE_ONLY`
- `nextion.READ_AND_WRITE`
## Functions
### cmd
You can send a command over serial to the device using `display.cmd(command`[ , flags=nextion.READ_AND_WRITE])`<br>
- `command`: the command to send to the device
- `flags`: You can insert `nextion.WRITE_ONLY`, when you don't want to read the reply from UART. By default, the function is waiting 100 ms and then, the function returns the reply.
### sleep
To enter or exit sleep mode of the nextion device, use the command `display.sleep(state)`<br>
- `state`: Set the parameter to 1 for enter sleep mode. Set the parameter to 0 for exit sleep mode.
### page
To load a page on the nextion device, use the command `display.page(pageid)`<br>
- `pageid`: ID of the page or name of the page.
### reset
You can reset the device using the command `display.reset()`
### brightness
To set the display brightness use the command `display.brightness(brightness)`<br>
- `brightness`: Brightness to set in percent
