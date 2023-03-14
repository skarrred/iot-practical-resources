Type in Command line:
`sudo raspi-config`
-> interfacign options
-> enable i2c
`sudo apt-get install python-smbus i2c-tools`

Download zip file:
https://github.com/timwaizenegger/raspberrypi-examples/blob/master/actor-led-7segment-4numbers/actor-led-7segment-4numbers.zip

Change python 2 strings to python 3 strings in clock.py as well as TM17...file

Run clock.py file with terminal
clock 40
dio38
vcc2,4
