# pyright: reportMissingImports=false
import network
import time
import socket
import struct

import config
import led

def connect_wifi():
    # Disable the access point
    ap = network.WLAN(network.AP_IF)
    ap.active(False)

    # Connect to the WiFi network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    start_time = time.time()

    if not wlan.isconnected():
        print(f"Connecting to WiFi SSID: {config.WIFI_SSID}")
        wlan.connect(config.WIFI_SSID, config.WIFI_PASSWORD)

        while not wlan.isconnected():
            time.sleep(1)
            if (time.time() - start_time) > config.WIFI_TIMEOUT:
                return False

    print(f"Connected to {wlan.config('ssid')}")
    print(f"IP address: {wlan.ifconfig()[0]}")

    return True


def sync_time_with_sntp():
    TIME1970 = 2208988800
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = '\x1b' + 47 * '\0'
    client.sendto(data.encode('utf-8'), (config.NTP_SERVER, 123))
    data, address = client.recvfrom(1024)
    if data: 
        print('Response received from:', address)
    t = struct.unpack('!12I', data)[10] - TIME1970
    print('\tTime = %s' % time.ctime(t))


def main():
    if connect_wifi():
        led.blink("green")
    else:
        led.blink("red")


main()
