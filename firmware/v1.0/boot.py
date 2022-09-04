import supervisor
import board
import digitalio
import storage
import usb_cdc
import usb_hid
import usb_midi


# =============================================================
# KMK base boot.py
supervisor.set_next_stack_limit(4096 + 4096)

# =============================================================
# Purple Owl Dev Mode entry
#
# Latch the chain and poll the first bit of the scan data.
# If the key was pressed, then enter CircuitPython Dev Mode
# Else, turn off all USB enumerations except HID
#

DAT = digitalio.DigitalInOut(board.D9)
DAT.switch_to_input()

LD  = digitalio.DigitalInOut(board.D7)
LD.switch_to_output(value=True, drive_mode=digitalio.DriveMode.PUSH_PULL)

if DAT.value:
    storage.disable_usb_drive()
    usb_cdc.disable()
    usb_midi.disable()
    usb_hid.enable(boot_device=1)

DAT.deinit()
LD.deinit()
