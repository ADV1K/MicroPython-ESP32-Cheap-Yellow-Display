# Introduction
My experiments with MicroPython on the [ESP32 Cheap Yellow Display](https://github.com/witnessmenow/ESP32-Cheap-Yellow-Display).

# Setup
## Download MicroPython Firmware
1. Download the latest firmware from the [MicroPython ESP32 download page](https://micropython.org/download/ESP32_GENERIC/) or use the one provided in the repo.
2. Figure out the device path of the ESP32. For example, it could be `/dev/ttyUSB0` on Linux, or `COM4` on Windows, and `/dev/cu.usbserial-XXXX` on macOS.

```bash
pip install mpr  # pipx install mpr
mpr list
```

## Flashing MicroPython
After connecting the device using a USB cable, run the following command to flash MicroPython. Replace `FIRMWARE` with the path to the firmware file and `DEVICE` with the device path.
Hold the `BOOT` button on the ESP32 after pasting the command to enter flashing mode.

```bash
export FIRMWARE=firmware/ESP32_GENERIC-20240222-v1.22.2.bin
export DEVICE=/dev/cu.usbserial-110
make flash
```

## Connecting to REPL
After flashing the firmware, you can connect to the MicroPython REPL using `mpr`. On Windows, PuTTY should work as well.

```bash
mpr repl
```

## Running the Code
You can run the code on the ESP32 using `mpr`

```bash
make run
```

## Wi-Fie
To connect to a Wi-Fi network, edit the SSID and password in `config.py` and run the boot.py or reboot the device. Also make sure that your Wi-Fi network is 2.4 GHz.

```bash
make boot
```

# Resources
- [ESP32 Tutorial on MicroPython Docs](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html)
