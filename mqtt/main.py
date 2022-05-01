'''
References:
  Button: https://github.com/ubidefeo/MicroPython-Button
  MQTT: https://pypi.org/project/micropython-umqtt.simple2/#files
        https://github.com/fizista/micropython-umqtt.simple2/blob/master/example_sub.py
        https://github.com/fizista/micropython-umqtt.simple2/blob/master/example_pub.py
  notes
        1. umqtt.simple is the micropython umqtt library
           https://github.com/micropython/micropython-lib/tree/master/micropython/umqtt.simple
        2. there is a "robust" version which may be better for final use
'''

from machine import reset, Pin
import time
import json
from umqtt.simple2 import MQTTClient
from Button import Button

if not wlan.isconnected():
	print("WiFi not connected after", WIFI_CONNECT_ATTEMPTS*WIFI_SLEEP_TIME, "seconds")
	print("Restarting in 2 seconds")
	sleep(2)
	reset()   # start over with hard reset

#-- <params> ----------------------
# MQTT server
MQTT_SERVER = "192.168.0.45"

# Domoticz parameters
SUB_TOPIC = "domoticz/out"
PUB_TOPIC = "domoticz/in"
DOMO_IDX = 195

# I/O pin connected to LED
LED_PIN = Pin.PA_00
LED_ON = 0

# I/O pin connected to relay 
RELAY_PIN = Pin.PA_01
RELAY_ON = 1

# I/O pin connected to n.o. push button 
#               

#
BUTTON_PIN = Pin.PB_07
BUTTON_EXT_PULLUP = True    # externally pulled high 

# If BUTTON_EXT_PULLUP = True then must connect external
# pull up resistor and the button must momentarily 
# pull the I/O pin down to GND.
#               +----------[ R ]---> 3.3V
#               |    _[]_
# I/O pin ==o<--+----o  o----------> GND

# If BUTTON_EXT_PULLUP = FALSE then must connect external
# pull down resistor and the button must momentarily 
# pull the I/O pin up to 3.3 volts.
#                    _[]_
# I/O pin ==o<--+----o  o----------> 3.3V
#               |
#               +----------[ R ]---> GND


#-- </params> ------------------------

# setup I/O pins

RELAY_OFF = 1-RELAY_ON
Relay = Pin(RELAY_PIN, Pin.OUT, Pin.PULL_FLOATING)
Relay.value(RELAY_OFF)

LED_OFF = 1-LED_ON
Led = Pin(LED_PIN, Pin.OUT, Pin.PULL_FLOATING)
Led.value(LED_OFF)

# Relay / LED control

RelayOn = False  # initial state

def TurnRelayOn():
	global RelayOn
	Relay.value(1)
	Led.value(LED_ON)
	RelayOn = True

def TurnRelayOff():
	global RelayOn
	Relay.value(0)
	Led.value(LED_OFF)
	RelayOn = False
	
def ToggleRelay():
	global RelayOn
	if RelayOn:
		TurnRelayOff()
	else:
		TurnRelayOn()

# MQTT

def publish(status):
	action = "On" if status else "Off"
	msg = '{"command": "switchlight", "idx":'+str(DOMO_IDX)+', "switchcmd": "'+action+'" }'
	mc.publish(PUB_TOPIC, msg) 
	#print("MQTT publishing: [" + PUB_TOPIC + "]", msg)
 

# MQTT callback on received messages on the subscribed topic
def sub_cb(topic, msg, retain, dup):
	#print((topic, msg, retain, dup))
	json_msg = json.loads(msg)
	if json_msg["idx"] == DOMO_IDX:
		#print(json_msg)
		if json_msg["nvalue"] == 0:
			TurnRelayOff()
		elif json_msg["nvalue"] == 1:
			TurnRelayOn()

#print("Starting mqtt client & subscribing to", SUB_TOPIC);
mc = MQTTClient("umqtt_client", MQTT_SERVER)
mc.set_callback(sub_cb)
mc.connect()
mc.subscribe(b"domoticz/out")  

# Button 
def btn_change(button, event):
	global RelayOn
	if event == Button.RELEASED:
		ToggleRelay()
		publish(RelayOn)
		#print("button released")


# W600 needs to set either the internal_pullup or internal_pulldown 
# resistor. It is not possible to leave it undefined as assumed in 
# button.py
if BUTTON_EXT_PULLUP: 
	btn = Button(BUTTON_PIN, True, btn_change, internal_pullup = True)
else:
	btn = Button(BUTTON_PIN, False, btn_change, internal_pulldown = True)
	
print('Setup completed.')
print('Start pressing button to toogle the Domoticz device off / on.')
print('Change the state of virtual device in Domoticz.')

# Run endlessly
#while (True):

# Testing for 3 minutes
for i in range(3*60*4):
	mc.check_msg() # non blocking mqtt message pump
	btn.update()   # check button state
	sleep(0.250)

mc.disconnect()  # get here only if testing
# fall through to REPL
