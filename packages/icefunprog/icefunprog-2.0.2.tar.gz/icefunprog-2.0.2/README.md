# iceFUN Programmer
Multiplatform script to upload bitstream to iceFUN FPGAs. This was done to be used with [apio](https://github.com/FPGAwars/apio) micro-ecosystem, but it can also be used as a standalone script.

## Installation
Using pip
```
pip install -U icefunprog
```

Manual installation
```
$ git clone https://github.com/pitrz/icefunprog.git
$ cd icefunprog/
$ python setup.py build
$ sudo python setup.py install
```

## Usage

```
$ icefunprog
Usage: icefunprog serial_device bitstream_file
$ icefunprog /dev/ttyACM0 hardware.bin
Wrote 135100 bytes
```