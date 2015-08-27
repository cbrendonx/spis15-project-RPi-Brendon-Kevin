# Final RPi Project for SPIS 2015

import RPi.GPIO as GPIO, time

# use physical pin numbering
GPIO.setmode(GPIO.BOARD)

#set up digital line detectors as inputs
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

slowspeed = 20
fastspeed = 100
LED2 = 22
LED3 = 18
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)

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
  rightForward(slowspeed)
  leftForward(fastspeed)

def turnLeft():
  rightForward(fastspeed)
  leftForward(slowspeed)

def stopall():
  p.ChangeDutyCycle(0)
  q.ChangeDutyCycle(0)
  a.ChangeDutyCycle(0)
  b.ChangeDutyCycle(0)
  print('stop')

turnRight()
time.sleep(5)
stopall()
turnLeft()
time.sleep(5)
stopall()

GPIO.cleanup()
