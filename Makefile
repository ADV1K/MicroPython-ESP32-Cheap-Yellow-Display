dev:
	@# Whenever the code changes, run main.py
	ls src/* | entr -scr "make run"

run:
	@# Run the main.py file on the microcontroller
	mpr run src/main.py

boot:
	@# Run the boot.py file on the microcontroller
	mpr run src/boot.py

sync:
	@# Upload all the python files to the device
	@for file in src/*; do \
		echo "Uploading $$file..."; \
		mpr put $$file /; \
	done

shell:
	# screen $(DEVICE) 115200
	# minicom -D $(DEVICE) -b 115200
	# picocom -b 115200 $(DEVICE) 
	mpr repl

flash:
	@echo "Flashing firmware..."
	esptool.py --port $(DEVICE) erase_flash 
	esptool.py --port $(DEVICE) --chip esp32 write_flash -z 0x1000 $(FIRMWARE)


.PHONY: flash shell ls sync boot run
