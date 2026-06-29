import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Settings
BOOT_WAIT_SECONDS = 10       # delay before the first attempt
RETRY_INTERVAL_SECONDS = 3   # pause between attempts
MAX_ATTEMPTS = 3             # amount of attempts to press the key

# Initialize keyboard emulation
kbd = Keyboard(usb_hid.devices)

# Setup on-board LED
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Turn ON the LED
led.value = True

# Wait some time to let the PC boot up
time.sleep(BOOT_WAIT_SECONDS)

# Virtually press the key
for _ in range(MAX_ATTEMPTS):
    kbd.press(Keycode.F1)
    time.sleep(0.2) # hold key long enough for BIOS to register the press
    kbd.release_all()
    time.sleep(RETRY_INTERVAL_SECONDS)

# Turn OFF the LED
led.value = False
