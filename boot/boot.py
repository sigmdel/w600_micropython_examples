from time import sleep
import secrets
import network
WIFI_CONNECT_ATTEMPTS = 16
WIFI_SLEEP_TIME = 0.5
wlan = network.WLAN(network.STA_IF)    
wlan.active(True)                      
wlan.connect(secrets.ssid, secrets.psk)
for i in range(WIFI_CONNECT_ATTEMPTS):
	if wlan.isconnected():
		break
	else:
		sleep(WIFI_SLEEP_TIME)
if wlan.isconnected():
	print('Connected to', secrets.ssid)
	import w600
	w600.run_ftpserver(port=21,username="user",password="12345678")
	sleep(WIFI_SLEEP_TIME)
	wlan.ifconfig((secrets.ip, secrets.subnet, secrets.gateway, secrets.dns))
	sleep(WIFI_SLEEP_TIME)
	print('URL:', wlan.ifconfig()[0]+':21', 'username: "user", password:"12345678"')

