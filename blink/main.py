'''
Blink for W600-Pico
''' 

RUNS = 5         # number of flash cycles to run
CYCLES = 8       # number of quick flashes per cycle
FLASH_TIME = 0.1 # 100 ms on/off time of quick flashes
OFF_TIME = 1.5   # 1500 ms off time between series of flashes
LED_ON = 0       # LOW turns the LED attached to GPIO 22 on
VERBOSE = True   # print state of LED to the serial port

from os import uname
from machine import Pin
from time import sleep

# Blue LED connected to pin labeled PA0 on the board
Led = Pin(Pin.PA_00, Pin.OUT, Pin.PULL_FLOATING)

print()
print('W600-Pico Blink')
print('---------------')

print("os.uname:")      
print(uname())
print()
sleep(0.25)

for j in range(RUNS):
	if VERBOSE:
		print(j+1, '/', RUNS,'  ', end='')
	for i in range(CYCLES):
		Led.value(LED_ON)
		if VERBOSE:
			print('ON ', end='')
		sleep(FLASH_TIME)
		Led.value(not Led.value())
		sleep(FLASH_TIME)
	if VERBOSE:
		print('OFF')
	sleep(OFF_TIME)

if VERBOSE:
	print("Done.")
