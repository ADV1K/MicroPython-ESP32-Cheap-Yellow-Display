# pyright: reportMissingImports=false, reportUndefinedVariable=false

import machine
import os

# PS: Make sure your SD Card is *unpartitioned* and *formatted* as FAT32 before running this code.
# sudo mkfs.fat -F 32 /dev/sdX

# To figure out the slot number, check the table at: https://docs.micropython.org/en/latest/library/machine.SDCard.html 
sd = machine.SDCard(slot=2)
vfs = os.VfsFat(sd)
os.mount(vfs, "/sd")

# write a file to the SD Card
with open("/sd/test.txt", "w") as f:
    f.write("Hello SD Card!")
    print("File written to SD Card")
