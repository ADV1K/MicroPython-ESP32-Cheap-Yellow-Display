dev:
	@# Whenever the code changes, run it on the device
	ls src/* | entr -scr "make run"

run:
	@echo "Running app.py on the device..."
	@mpremote mount src + exec "import app"

upload:
	@# Deploy the code to the device and do a hard reset
	@echo "cd src"
	@cd src; mpremote cp -r . : + reset
	@echo "Running main.py on the device..."

shell:
	@# screen $(DEVICE) 115200
	@# minicom -D $(DEVICE) -b 115200
	@# picocom -b 115200 $(DEVICE) 
	mpremote mount src repl --inject-code "from app import *\n"

mount-sdcard:
	@echo "Mounting the SD card on the device..."
	mpremote exec "import os, machine; os.mount(machine.SDCard(), '/sd')"

flash:
	@echo "Flashing firmware..."
	esptool.py --port $(DEVICE) --baud 600000 erase_flash 
	esptool.py --port $(DEVICE) --baud 600000 --chip esp32 write_flash -z 0x1000 $(FIRMWARE)


.PHONY: flash shell ls sync boot run
