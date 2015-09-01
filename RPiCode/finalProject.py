# Final RPi Project for SPIS 2015
 
import RPi.GPIO as GPIO, time, sys, threading
import random

# use physical pin numbering
GPIO.setmode(GPIO.BOARD)

# set up digital line detectors as inputs
# Pin 11 Right Sensor
# Pin 12 Middle Sensor
# Pin 13 Left Sensor
GPIO.setup(11, GPIO.IN)
GPIO.setup(12, GPIO.IN)
GPIO.setup(13, GPIO.IN)

# use pwm on inputs so motors don't go too fast
# Pins 19, 21 Right Motor
# Pins 24, 26 Left Motor
GPIO.setup(19, GPIO.OUT)
p = GPIO.PWM(19, 20)
p.start(0)
GPIO.setup(21, GPIO.OUT)
q = GPIO.PWM(21,20)
q.start(0)

GPIO.setup(24, GPIO.OUT)
a = GPIO.PWM(24,20)
a.start(0)
GPIO.setup(26, GPIO.OUT)
b = GPIO.PWM(26,20)
b.start(0)

globalstop = 0
finished = False

# Define duty cycles as speed options
slowspeed = 20
fastspeed = 100

# Define pins for LEDs
LED2 = 22
LED3 = 18
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)

# Define Sonar pin for Trigger and Echo to be the same
SONAR = 8

def rightForward(speed):
  p.ChangeDutyCycle(speed)
  q.ChangeDutyCycle(0)

def leftForward(speed):
  a.ChangeDutyCycle(speed)
  b.ChangeDutyCycle(0)

def rightBackward(speed):
  p.ChangeDutyCycle(0)
  q.ChangeDutyCycle(speed)

def leftBackward(speed):
  a.ChangeDutyCycle(0)
  b.ChangeDutyCycle(speed)

def forward(speed):
  rightForward(speed)
  leftForward(speed)

def backward(speed):
  rightBackward(speed)
  leftBackward(speed)

def turnRight():
  rightForward(0)
  leftForward(slowspeed + 10)

def turnLeft():
  rightForward(slowspeed + 10)
  leftForward(0)

def pointTurnRight(speed = slowspeed):
  rightBackward(speed)
  leftForward(speed)

def pointTurnLeft(speed = slowspeed):
  rightForward(speed)
  leftBackward(speed)

def stopall():
  p.ChangeDutyCycle(0)
  q.ChangeDutyCycle(0)
  a.ChangeDutyCycle(0)
  b.ChangeDutyCycle(0)

def pause():
  stopall()
  time.sleep(1)

def followLine():
  if globalstop == 1:
    stopall()
  elif GPIO.input(11) == 0 and GPIO.input(12) == 1 and GPIO.input(13) == 0:
    forward(slowspeed)
    setLEDs(0, 0)
  elif GPIO.input(11) == 1:
    turnRight()
    setLEDs(1, 0)
  elif GPIO.input(13) == 1:
    turnLeft()
    setLEDs(0, 1)

def sonar():
  while finished != True:
    global globalstop
    GPIO.setup(SONAR, GPIO.OUT)
    GPIO.output(SONAR, True)
    time.sleep(0.00001)
    GPIO.output(SONAR, False)
    start = time.time()
    count = time.time()
    GPIO.setup(SONAR, GPIO.IN)
    while GPIO.input(SONAR) == 0 and time.time() - count < 0.1:
      start = time.time()
    stop = time.time()
    while GPIO.input(SONAR) == 1:
      stop = time.time()
    # Calculate pulse length
    elapsed = stop - start
    # Distance pulse travelled in that time is time
    # multiplied by the speed of sound (cm/s)
    distance = elapsed * 34000
    # That was the distance there and back so halve the value
    distance = distance / 2
    # checks if there is an obstacle within a certain distance
    if distance < 15:
      globalstop = 1
    else:
      globalstop = 0
    time.sleep(0.25)

def turnAround():
  pointTurnRight()
  time.sleep(0.5)
  while GPIO.input(12) != 1:
    pointTurnRight()

def goAround():
  turn = [0.6, 0.6, 0.5, 0.5]
  pause()
  pointTurnRight()
  time.sleep(turn[0])
  pause()
  forward(slowspeed)
  time.sleep(1)
  pause()
  pointTurnLeft()
  time.sleep(turn[1])
  pause()
  forward(slowspeed)
  time.sleep(1.5)
  pause()
  pointTurnLeft()
  time.sleep(turn[2])
  pause()
  while GPIO.input(12) != 1:
    forward(slowspeed)
  pause()
  pointTurnRight()
  time.sleep(turn[3])

def whack():
  pause()
  forward(slowspeed)
  time.sleep(0.5)
  pause()
  pointTurnRight(fastspeed)
  time.sleep(1)
  pause()
  while GPIO.input(12) != 1:
    pointTurnRight()

threading.Timer(1, sonar).start()

def setLEDs(L2, L3):
  GPIO.output(LED2, L2)
  GPIO.output(LED3, L3)

setLEDs(1, 1)

try:
  while True:
    followLine()
    if globalstop == 1:
      random.choice([turnAround, goAround, whack])()

except KeyboardInterrupt:
  finished = True # stops other loops
  GPIO.cleanup()
  sys.exit()


