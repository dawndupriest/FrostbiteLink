import time
import board
import neopixel
import busio

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 1.5)
        g = int(130 - pos * 1.5)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(130 - pos * 1.5)
        g = 0
        b = int(pos * 1.5)
    else:
        pos -= 170
        r = 0
        g = int(pos * 1.5)
        b = int(130 - pos * 1.5)
    return (r, g, b)

def rainbow_cycle(wait, totaltime):
    curtime = 0
    wut = time.monotonic();
    #print(wut)
    j=0
    while (wut + totaltime > time.monotonic()):
        pixelstrip.fill(wheel(j))
        pixelstrip.show()
        time.sleep(wait)
        #curtime = curtime + wait

        #print(time.monotonic())
        j = j + 1
        if j>254:
            j = 0


def red_strobe(wait, totaltime):
    curtime = 0
    wut = time.monotonic();
    while (wut + totaltime > time.monotonic()):
        pixelstrip.fill((130,0,0))
        time.sleep(wait/2)
        pixelstrip.fill((0,0,0))
        time.sleep(wait/2)


def green_pulse(wait, totaltime):
    curtime = 0
    wut = time.monotonic();
    j = 130
    while (wut + totaltime > time.monotonic()):
        pixelstrip.fill((0,j,0))
        time.sleep(wait/13)
        j = j-10
        if (j<0):
            j=130



#npin= pin.Pin(board.D3,OUTPUT)
pixelstrip = neopixel.NeoPixel(board.IO18,200,pixel_order=(0,1,2))
print(board.IO18)
b = 0
delta = 2
uart = busio.UART(board.IO39, board.IO37, baudrate=9600, timeout=0.02)

blue = True

while True:
    if blue:
        pixelstrip.fill((b//10,b//4,b))
    else:
        pixelstrip.fill((b,0,0))
    time.sleep(0.01)
    b = b + delta
    if b > 130 or b < 1:
        delta = delta * -1
    print(b)

    if (b % 10) == 0:
        data = uart.read(32)
        if data is not None:
            data_string = ''.join([chr(k) for k in data])
            print(data_string,end="")
            if "RED" in data_string:
                blue = False
            elif "BLUE" in data_string:
                blue = True
            elif "RST" in data_string:
                b = 0
                delta = 4
                print("SYNC")
                pixelstrip.fill((0,0,255))
                time.sleep(0.5)
            elif "COLGERA" in data_string:
                rainbow_cycle(0.001,34.1)
            elif "GLEEOK" in data_string:
                red_strobe(0.1, 12)
                green_pulse(0.5, 11.5)
                pixelstrip.fill((0,0,0))
                time.sleep(0.3)
                pixelstrip.fill((130,130,130))
                time.sleep(2.0)


# Write your code here :-)
