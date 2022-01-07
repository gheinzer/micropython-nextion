# micropython nextion library
 This library could help you control you nextion-display over UART.
## How to use
First, define an object with the class `nextion(tx_pin, rx_pin, baudrate)`
This could look like this now:<br>
```
from nextion import nextion
display = nextion(13, 12, 9600) 
```
Now you can control the device with different commands.
## Constants
- `nextion.WRITE_ONLY`
- `nextion.READ_AND_WRITE`
- `nextion.DECODE`
- `nextion.RAW`
## Functions
### cmd
You can send a command over serial to the device using `display.cmd(command`[ , flags=nextion.READ_AND_WRITE])`<br>
- `command`: Required. The command to send to the device
- `flags`: Optional. You can insert `nextion.WRITE_ONLY`, when you don't want to read the reply from UART. By default, the function is waiting 100 ms and then, the function returns the reply.  Default is `nextion.READ_AND_WRITE`.
### sleep
To enter or exit sleep mode of the nextion device, use the command `display.sleep(state)`<br>
- `state`: Required. Set the parameter to 1 for enter sleep mode. Set the parameter to 0 for exit sleep mode.
### page
To load a page on the nextion device, use the command `display.page(pageid)`<br>
- `pageid`: Required. ID of the page or name of the page.
### reset
You can reset the device using the command `display.reset()`
### brightness
To set the display brightness use the command `display.brightness(brightness)`<br>
- `brightness`: Required. Brightness to set in percent
### read
You can read bytes from serial with the command `display.read([flags=nextion.RAW])`
- `flags`: Optional. You can set the `flags` parameter to `nextion.DECODE`, if you want the function to decode the output of the displays. If you don't want to have the data ASCII encoded, you can insert `nextion.RAW`. Default is `nextion.RAW`.
