# Copyright (c) 2014 University of California, San Diego 
# Author: Diba Mirza 
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import time

import Image
import ImageDraw
from math import *

from Adafruit_LED_Backpack import BicolorMatrix8x8

digit_color=[(255,0,0), (255,255,0), (0,255,0)]
def DrawDigit(draw, num, digit):
        if digit>2:
           print "Digit cannot exceed 3"
           return draw;
	
	if num ==0:
		# Draw a zero which is a rectangle 
		#draw.rectangle((0,digit*3,3,digit*3+1), outline=(255,0,0), fill=(255, 255, 0))
		draw.rectangle((0,digit*3,3,digit*3+1), outline=digit_color[digit], fill=(255, 255, 0))

	else:
		# Draw a one which is a line 
		#draw.line((0,digit*3,3,digit*3), fill=(0,255,0))
		draw.line((0,digit*3,3,digit*3), fill=digit_color[digit])

	return draw;

def DisplayCounter(count):
	counter= count%8;
	# Alternatively, create a display with a specific I2C address and/or bus.
	display = BicolorMatrix8x8.BicolorMatrix8x8(address=0x70, busnum=1)

	# Initialize the display. Must be called once before using the display.
	display.begin()
	display.clear()

	# First create an 8x8 RGB color image.
	image = Image.new('RGB', (8, 8))

	# Then create a draw instance.
	draw = ImageDraw.Draw(image)
        #draw.rectangle((0,0,7,7), outline =(255,0,0),fill =(255,255,0))
	draw= DrawDigit(draw, counter &1 , 0)
 	draw =DrawDigit(draw, (counter>>1) &1, 1)
 	draw =DrawDigit(draw, (counter>>2) &1, 2)
	# Draw the image on the display buffer.
	display.set_image(image)
	# Draw the buffer to the display hardware.
	display.write_display()
	#time.sleep(0.5)
        return
