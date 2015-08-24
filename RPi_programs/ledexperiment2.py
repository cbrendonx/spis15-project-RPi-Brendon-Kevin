# First import some libraries that will help us
# do some cool, complicated stuff
# Think of a library as being like a car key. It
# give you access to powerful things.  You won't
# always know the inner workings of the libraries.
# You will learn a LOT more about them at UCSD,
# but don't worry if it looks mysterious at first!
# 
# RPi.GPIO is a library that talks to the outer world
# through the pins on the RPi
#
# time is a library that allows you to set pauses in
# the execution of a program
import RPi.GPIO as GPIO
import time

LED = 24

# Every pin has a name.
# Let the system know you are using Broadcom naming 
GPIO.setmode(GPIO.BCM)

# Setup pin 24 as output
GPIO.setup(LED,GPIO.OUT)

# Print something that tells the user they should look at the light!
print("light on!")

# Now here is the actual blinking, using the library
def pwmTest():
    p = GPIO.PWM(LED, 100)
    p.start(50)

    time.sleep(5)

    p.ChangeDutyCycle(100)

    time.sleep(5)

    p.stop()

def blink():
    for i in range(20):
        # First turn the light on by setting pin 24 to HIGH.
        GPIO.output(24,GPIO.HIGH)

        # Now wait 5 seconds
        time.sleep(.5)

        # Now turn the light off by setting pin 24 to LOW                                                                                 
        GPIO.output(24,GPIO.LOW)

        time.sleep(.5)
pwmTest()

# Now do cleanup
GPIO.cleanup()
