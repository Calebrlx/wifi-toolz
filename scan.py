import time
from RF24 import RF24
# import matplotlib.pyplot as plt

CE_PIN = 18 #5
CSN_PIN = 24 #8

# Initialize the NRF24L01+ module
radio = RF24(CE_PIN, CSN_PIN)

def setup_radio():
    radio.begin()
    radio.setAutoAck(False)  # Disable auto acknowledgment
    radio.setPALevel(RF24_PA_LOW)  # Set low power for scanning
    radio.stopListening()  # Set to receive mode

def scan_channels():
    channel_rssi = {}
    for channel in range(0, 126):  # NRF24L01+ supports 126 channels
        radio.setChannel(channel)
        radio.startListening()
        time.sleep(0.005)  # Wait for RSSI stabilization
        radio.stopListening()

        # Check for valid RSSI or signal activity
        detected = radio.testCarrier()
        channel_rssi[channel] = detected

        # Print live scanning result
        status = "Active" if detected else "Inactive"
        print(f"Channel {channel}: {status}")

    return channel_rssi

def display_results(channel_rssi):
    print("\nScan Results:")
    for channel, status in channel_rssi.items():
        status_str = "Active" if status else "Inactive"
        print(f"Channel {channel}: {status_str}")

# def plot_channel_activity(channel_rssi):
#     channels = list(channel_rssi.keys())
#     activity = [1 if channel_rssi[ch] else 0 for ch in channels]

#     plt.figure(figsize=(12, 6))
#     plt.bar(channels, activity, width=1.0, align="center", alpha=0.7)
#     plt.title("Channel Activity Scan")
#     plt.xlabel("Channel (0-125)")
#     plt.ylabel("Activity (1=Active, 0=Inactive)")
#     plt.grid(True)
#     plt.show()


if __name__ == "__main__":
    setup_radio()
    print("Scanning Wi-Fi/Bluetooth Channels...")
    results = scan_channels()
    # plot_channel_activity(results)
    display_results(results)