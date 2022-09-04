"""
Basic key test
"""

import time
import digitalio
import board

# Pinout
# dat - D9 / MISO
# clk - D8 / SCK
# ld  - D7 / RX
# rgb - D6 / TX

DAT = digitalio.DigitalInOut(board.D9)
DAT.switch_to_input()

CLK = digitalio.DigitalInOut(board.D8)
CLK.switch_to_output(value=False, drive_mode=digitalio.DriveMode.PUSH_PULL)

LD  = digitalio.DigitalInOut(board.D7)
LD.switch_to_output(value=True, drive_mode=digitalio.DriveMode.PUSH_PULL)

NUM_KEYS = 61

# SRC: https://sourcegraph.com/github.com/adafruit/circuitpython/-/blob/shared-module/keypad/ShiftRegisterKeys.c
while True:
    time.sleep(0.1)

    # Lock the scan chain
    LD.value = True
    
    # Shift in scan chain
    i = 0
    while i < NUM_KEYS:
        key = DAT.value
        
        CLK.value = True
        CLK.value = False
        
        if not key:
            print(i)
            
        i += 1
    
    # Unlock the scan chain 
    LD.value = False
