import supervisor


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
