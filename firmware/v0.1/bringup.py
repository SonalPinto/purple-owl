"""
Basic key test
"""

import time
import digitalio
import board

columns = [
    digitalio.DigitalInOut(board.GP13),
    digitalio.DigitalInOut(board.GP12),
    digitalio.DigitalInOut(board.GP11),
    digitalio.DigitalInOut(board.GP10),
    digitalio.DigitalInOut(board.GP9),
    digitalio.DigitalInOut(board.GP8),
    digitalio.DigitalInOut(board.GP7),
    digitalio.DigitalInOut(board.GP6),
    digitalio.DigitalInOut(board.GP5),
    digitalio.DigitalInOut(board.GP4),
    digitalio.DigitalInOut(board.GP3),
    digitalio.DigitalInOut(board.GP2),
    digitalio.DigitalInOut(board.GP1),
    digitalio.DigitalInOut(board.GP0),
]

for col in columns:
    col.switch_to_input(pull=digitalio.Pull.UP)

rows = [
    digitalio.DigitalInOut(board.GP29),
    digitalio.DigitalInOut(board.GP28),
    digitalio.DigitalInOut(board.GP27),
    digitalio.DigitalInOut(board.GP26),
    digitalio.DigitalInOut(board.GP15),
]

for row in rows:
    col.switch_to_input(pull=digitalio.Pull.UP)

# SRC: https://sourcegraph.com/github.com/adafruit/circuitpython/-/blob/shared-module/keypad/KeyMatrix.c?L126
while True:
    time.sleep(0.1)
    
    y = 0
    for row in rows:
        row.switch_to_output(value=False, drive_mode=digitalio.DriveMode.PUSH_PULL)
        
        x = 0
        for col in columns:
            key = col.value
            if not key:
                print(y, ",", x)
            x += 1
        
        row.value = True
        row.switch_to_input(pull=digitalio.Pull.UP)
        y += 1
