import time
import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("<--your-ssid-->","<--your-wifi-password-->")
time.sleep(2)
import w600
w600.run_ftpserver(port=21,username="user",password="12345678")
time.sleep(1)
wlan.ifconfig(('192.168.1.145', '255.255.255.0', '192.168.1.1', '8.8.8.8'))
time.sleep(0.5)
print("ftp server at", wlan.ifconfig()[0]+":21, username is 'user', password is '12345678'")
