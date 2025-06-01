Files for Link Cosplay shown here in this YouTube short: https://youtube.com/shorts/ZK1LJon-Nh0?feature=share
Because of the sheer number of LED's, I used four microcontrollers and four power banks. The bluetooth is accessed via an Adafruit Feather 32u4 Bluefruit LE. https://www.adafruit.com/product/3242  
It is also stacked with a Music Maker Featherwing https://www.adafruit.com/product/3357  to which I connect a small powered speaker.

On the feather, the pinouts are:
Neopixel data (the zonai energy cells): pin 13
Software Serial RX: 0 (connected to the TX of all of the other microcontrollers)
Software Serial TX: 11 (connected to RX of all other microcontrollers)
Many pins are used by the Music Maker Featherwing.


On the LOLIN s2 Minis, the pinouts are:
Neopixel data: IO18
TX (connected to all other LOLIN TX, but the Feather's RX): 39
RX (connected to all other LOLIN RX, but the feather's TX): 37

