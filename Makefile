# pip install adafruit-ampy

dev:
	@# Whenever a python file changes, upload the code and run the main.py
	start=$(date +%s);
	ls *.py | entr -scr "make run"

run: sync
	@# Run the main.py file on the microcontroller
	ampy --port $(DEVICE) run main.py

boot: sync
	@# Run the boot.py file on the microcontroller
	ampy --port $(DEVICE) run boot.py

sync:
	@# Upload all the python files to the device
	@for file in *.py; do \
		echo "Uploading $$file..."; \
		ampy --port $(DEVICE) put $$file; \
	done

shell:
	# screen $(DEVICE) 115200
	# minicom -D $(DEVICE) -b 115200
	picocom -b 115200 $(DEVICE) 

flash:
	@echo "Flashing firmware..."
	esptool.py --port $(DEVICE) erase_flash 
	esptool.py --port $(DEVICE) --chip esp32 write_flash -z 0x1000 $(FIRMWARE)


.PHONY: flash shell ls sync boot run
