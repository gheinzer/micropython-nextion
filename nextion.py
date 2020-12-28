from machine import UART
from os import uname
import time
class nextion:
    WRITE_ONLY = 0
    WRITE_AND_READ = 1
    DECODE = 1
    RAW = 0
    def __init__(self, tx_pin, rx_pin, baudrate):
        self.uart = UART(1, baudrate, tx=tx_pin, rx=rx_pin)
        self.uart.init(baudrate, bits=8, parity=None, stop=1)
    def cmd(self, cmd, flags=WRITE_AND_READ):
        end_cmd=b'\xFF\xFF\xFF'
        self.uart.write(cmd)
        self.uart.write(end_cmd)
        if(flags == 1):
            time.sleep_ms(100)
            return self.uart.read()
    def sleep(self, state):
        self.cmd("sleep=" + str(state))
    def page(self, page):
        self.cmd("page " + str(page))
    def reset(self):
        self.cmd("rest")
    def brightness(self, brightness):
        self.cmd("dim=" + str(brightness))
    def read(self, flags=0):
        if(flags == 0):
            return self.uart.read()
        else:
            output = self.uart.read()
            if(not output is None):
                #output.replace("\xFF\xFF\xFF", "")
                output = bytearray(str(output)).decode("ascii")
                return output
            else:
                return None
