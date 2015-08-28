# Final RPi Project for SPIS 2015

import RPi.GPIO as GPIO, time, sys

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
  print('right forward')

def leftForward(speed):
  a.ChangeDutyCycle(speed)
  b.ChangeDutyCycle(0)
  print('left forward')

def rightBackward(speed):
  p.ChangeDutyCycle(0)
  q.ChangeDutyCycle(speed)
  print('right backward')

def leftBackward(speed):
  a.ChangeDutyCycle(0)
  b.ChangeDutyCycle(speed)
  print('left backward')

def forward(speed):
  rightForward(speed)
  leftForward(speed)
  print('forward')

def backward(speed):
  rightBackward(speed)
  leftBackward(speed)
  print('backward')

def turnRight():
  rightForward(0)
  leftForward(slowspeed)
  print('turn right')

def turnLeft():
  rightForward(slowspeed)
  leftForward(0)
  print('turn left')

def stopall():
  p.ChangeDutyCycle(0)
  q.ChangeDutyCycle(0)
  a.ChangeDutyCycle(0)
  b.ChangeDutyCycle(0)
  print('stop')

def followLine():
  if GPIO.input(11) == 0 and GPIO.input(12) == 1 and GPIO.input(13) == 0:
    forward(slowspeed)
    setLEDs(0, 0)
  elif GPIO.input(11) == 1:
    turnRight()
    setLEDs(1, 0)
  elif GPIO.input(13) == 1:
    turnLeft()
    setLEDs(0, 1)

def sonar():
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
  print 'Distance:', distance
  time.sleep(1)

def setLEDs(L2, L3):
  GPIO.output(LED2, L2)
  GPIO.output(LED3, L3)

setLEDs(1, 1)

try:
  while True:
    followLine()

except KeyboardInterrupt:
  GPIO.cleanup()
  sys.exit()
