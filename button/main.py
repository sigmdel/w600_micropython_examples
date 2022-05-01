from Button import Button  # from https://github.com/ubidefeo/MicroPython-Button
from machine import Pin    # builtin
from time import sleep_ms  # builtin

released_count = 0

def button_change(button, event):
    global released_count
    if event == Button.RELEASED:
        released_count += 1
        print('Button released. Count:', released_count)

# Create a Button class instance
#   Positional arguments
#     1. An I/O pin number 
#     2. The I/O pin default state when the button is not pressed (True = 1)
#     3. The callback function invoked when the button changes state
#   Keyword arguments (optional)
#     internal_pullup : if True an internal pullup resistor will be activated
#                       and the default state is set to False = 0
#     internal_pulldown : if True an internal pulldown resistor will be activated
#                         and the default state is set to True = 1
#     If both internal_pulldown and internal_pullup are set to True the
#     latter takes precedence
#     
button_one = Button(Pin.PB_07, True, button_change, internal_pullup = True)

print('setup completed, start pressing button')

'''
# non stop loop à la Arduino
while (True):
    button_one.update()
    sleep_ms(250)  # do other things
'''

# Run for 3 minutes for testing.

for i in range(3*60*4):
    button_one.update()
    sleep_ms(250) # do other things

# fall back into REPL
print("Done.")
