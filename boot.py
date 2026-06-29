# Runs once on power-up, before USB connects to the PC.
# USB device layout must be configured here.

import storage
import usb_hid

print("boot: start")

# Hide the CIRCUITPY drive from the host so the Pico enumerates as a keyboard only.
# storage.disable_usb_drive()
# print("boot: drive disabled")

# Enable a single keyboard HID device (trailing comma makes a one-element tuple).
# usb_hid.enable((usb_hid.Device.KEYBOARD,))
# print("boot: hid enabled")

print("boot: end")
