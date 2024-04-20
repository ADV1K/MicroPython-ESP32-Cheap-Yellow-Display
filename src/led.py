# pyright: reportMissingImports=false
import machine
import random
import time

ON = 0
OFF = 1

red = machine.Pin(4, machine.Pin.OUT)
green = machine.Pin(16, machine.Pin.OUT)
blue = machine.Pin(17, machine.Pin.OUT)
lights = [red, green, blue]

pattern = [
    [ON, OFF, OFF],
    [OFF, ON, OFF],
    [OFF, OFF, ON],
    [ON, ON, OFF],
    [OFF, ON, ON],
    [ON, OFF, ON],
    # [ON, ON, ON],  # I don't like white light
]


def reset():
    "Turn off all the lights"
    for light in lights:
        light.value(OFF)


def blink(color, count=3, delay=0.1):
    "Blink led to indicate a state change, like connecting to wifi"
    led = {
        "red": red,
        "green": green,
        "blue": blue,
    }[color]

    for _ in range(count):
        led.value(ON)
        time.sleep(delay)
        led.value(OFF)
        time.sleep(delay)


def sequence():
    "Go through the pattern one by one"
    while True:
        for combination in pattern:
            for light, state in zip(lights, combination):
                light.value(state)
            time.sleep(random.uniform(0.2, 1.2))


def random_sequence():
    "Pick a random led combination"
    while True:
        combination = random.choice(pattern)
        for light, state in zip(lights, combination):
            light.value(state)
        time.sleep(random.uniform(0.2, .5))


reset()

