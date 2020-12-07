# micropython nextion library
 This library will help you control you nextion-display over UART.
## How to use
First, define an object with the class `nextion(tx_pin, rx_pin, baudrate)`
This could look like this now:
`from nextion import nextion
display = nextion(13, 12, 9600)`
Now you can control the device with different commands.
## Functions
### cmd
The code to send a 
