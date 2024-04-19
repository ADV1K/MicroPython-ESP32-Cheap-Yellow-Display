import network
import config
import time

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
        while not wlan.isconnected() and (time.time() - start_time) < config.WIFI_TIMEOUT:
            print(".", end="")
            time.sleep(1)

    # Print the network configuration
    print("Network config:", wlan.ifconfig())


connect_wifi()
