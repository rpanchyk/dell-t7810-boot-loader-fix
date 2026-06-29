# Dell Precision T7810 bootloader fix
The project is aimed to fix the issue with the `Dell Precision T7810` motherboard bootloader if no official DELL case is available.

## Issue
The Dell Precision T7810 (as well as other versions, like T5810, etc) has a problem with the boot loader if some fan or front panel is not connected to the motherboard.

The `Alert! Front I/O Cable failure.` message is displayed after the boot:
![error](images/error.jpg)
So, you'll need to press `F1` key each time to confirm the booting.

In my case, it's not connected (absent because of unofficial PC-case):
![front-panel-socket](images/front-panel-socket.jpg)

## Solution
The workaround is to use any microcontroller board to emulate keyboard (`USB HID`).
The idea is to press the `F1` key virtually to continue the boot process.

The [Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/) (RP2040) is used in this project:
![raspberry-pi-pico-rp2040](images/raspberry-pi-pico-rp2040.jpg)

### Step 1
Download [CircuitPython](https://circuitpython.org/board/raspberry_pi_pico/) `UF2` release (or see [files](files) folder).

### Step 2
Connect `RP2040` to USB holding `BOOTSEL` button on the board and move `UF2` file to opened USB storage.

### Step 3
Download [Adafruit CircuitPython Bundle](https://circuitpython.org/libraries) of appropriate release (or see [files](files) folder).

### Step 4
Unpack and copy `adafruit_hid` folder to `lib` folder on board.

### Step 5
Create `code.py` file in root folder of board with the following content:
```python
import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Setup on-board LED
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Initialize keyboard emulation
kbd = Keyboard(usb_hid.devices)

# Turn ON the LED (optional)
led.value = True

# Wait some time (seconds)
time.sleep(30)

# Virtually press the key
kbd.send(Keycode.F1)

# Turn OFF the LED (optional)
led.value = False
```

### Step 6
Plug `RP2040` board to USB and reboot computer.
After timeout PC should be booted without additional interaction.

The final installation result looks like this:
![installation](images/installation.jpg)

## Reference
[Dell Precision Tower 7810 Owner's Manual](https://dl.dell.com/content/manual26064352-dell-precision-tower-7810-owner-s-manual.pdf)

## Known issues
- The solution is not working on reboot, since USB-ports are initialized only on first boot.

## Alternative solutions
There are some alternative methods to fix the issue, like:
1. Buy front-panel board, for example on [Aliexpress](https://www.aliexpress.com/item/1005003142913949.html) market or other.
2. Short-circuit some pins of [front-panel board socket](https://forum.overclockers.ua/viewtopic.php?t=226678&start=240) to disable hardware check.

## Contribution
Feel free to create an issue or a pull request if any ideas.

## Disclaimer
The source code of this repository is provided AS-IS and WITH NO WARRANTY of any kind.
Author and/or contributor are NOT responsible for any type of losses as a result of using source code, 
compiled binaries or other outcomes related to this repository.
