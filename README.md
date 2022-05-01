# w600_micropython_examples
Simple MicroPython scripts on the Wemos W600-Pico development board.

Source code to accompany [A First Look at the Winner Micro W600](https://sigmdel.ca/michel/ha/w600/first_look_w600_en.html).


1. [restore_ftp.py](restore_ftp/restore_ftp.py)

    - Short MicroPython script easily copied and pasted at the REPL prompt to restore the FTP server. 
    - Adjust the Wi-Fi credentials and the static IP address to suit. 
    - See [5. The FTP Server](https://sigmdel.ca/michel/ha/w600/first_look_w600_en.html#ftp) for details.

1. [blink.py](blink/blink.py)
    
    - Obligatory blink script flashing the on board LED of the W600-Pico.
    - See [6. A Blink Example](https://sigmdel.ca/michel/ha/w600/first_look_w600_en.htmll#blink)

1. [boot.py](boot/boot.py)

    - A custom `boot.py` script that connects to a Wi-Fi network and starts an FTP server.
    - Required for a workable programming environment.
    - Copy `boot.py` to the root directory of the W600 file system.
    - Adjust the content of [secrets.template](boot/secrets.template) and save as `secrets.py` along side `boot.py`.
