# w600_micropython_examples
Simple MicroPython scripts on the Wemos W600-Pico development board.

---

:warning: **Warning** 2022-12-15

These scripts work with MicroPython version v1.10-282 preloaded on the W600-Pico. As pointed out by [LexxM3](https://github.com/sigmdel/w600_micropython_examples/issues/1), Robert Hammelrath (robert-hh) has not only ported MicroPython v1.19.1 to the W60X, but he also makes the `wm_w600*.fls` image files available in his [Shared-Stuff](https://github.com/robert-hh/Shared-Stuff) repository.

It would be best to use one of these newer versions of MicroPython.

This repository will be deleted or perhaps archived and replace with an updated version as soon as possible.


---

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
