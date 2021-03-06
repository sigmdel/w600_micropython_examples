# w600_micropython_examples
Simple MicroPython scripts on the Wemos W600-Pico development board.

## Source code to accompany [A First Look at the Winner Micro W600](https://sigmdel.ca/michel/ha/w600/first_look_w600_en.html).


1. [restore_ftp](restore_ftp/restore_ftp.py)

    - Short MicroPython script easily copied and pasted at the REPL prompt to restore the FTP server. 
    - Adjust the Wi-Fi credentials and the static IP address to suit. 
    - See [5. The FTP Server](https://sigmdel.ca/michel/ha/w600/first_look_w600_en.html#ftp).

1. [blink](blink/main.py)
    
    - Obligatory blink script flashing the on-board LED of the W600-Pico.
    - See [6. A Blink Example](https://sigmdel.ca/michel/ha/w600/first_look_w600_en.htmll#blink).

1. [boot](boot/boot.py)

    - A custom `boot.py` script that connects to a Wi-Fi network and starts an FTP server.
    - Required for a workable programming environment.
    - Copy `boot.py` to the root directory of the W600 file system.
    - Adjust the content of [secrets.template](boot/secrets.template) and save as `secrets.py` alongside `boot.py`.
    - See [7. A Custom `boot.py`](https://sigmdel.ca/michel/ha/w600/first_look_w600_en.htmll#boot_py).


1. [button](button/main.py)

    - Polling an I/O pin connected to a normally open push button.
    - [button.py](button/button.py) is a clone of [MicroPython-Button/Button.py](https://github.com/ubidefeo/MicroPython-Button) by Ubi de Feo (ubdefeo).
    - See [8. Polling a Button](https://sigmdel.ca/michel/ha/w600/first_look_w600_en.htmll#workflow).

1. [mqtt](mqtt/main.py)

    - Implementing a simple Wi-Fi switch with MQTT capabilities.
    - Uses the [MicroPython-Button/Button.py](https://github.com/ubidefeo/MicroPython-Button) library by Ubi de Feo (ubdefeo).
    - Uses the [micropython-umqtt.simple2](https://github.com/fizista/micropython-umqtt.simple2) library by Wojciech Banaś (fizista).
    - See [9. Wi-Fi Switch - Proof of Concept](http://localhost/michel/ha/w600/first_look_w600_en.htmll#wifi_switch).


## Licence

The **BSD Zero Clause** ([SPDX](https://spdx.dev/): [0BSD](https://spdx.org/licenses/0BSD.html)) licence applies to the original code in this repository. 

Please respect the licence of each of the libraries used 
  - micropython-umqtt.simple2: [MIT](https://github.com/fizista/micropython-umqtt.simple2/blob/master/LICENSE)
  - MicroPython-Button: [not defined](https://github.com/ubidefeo/MicroPython-Button)
