#!/usr/bin/python
import sys
import time
import datetime
sys.path.append('/home/pi/python-code/Adafruit-Raspberry-Pi-Python-Code/Adafruit_LEDBackpack')
from Adafruit_8x8 import ColorEightByEight

board = [[0,1,0,0,0,0,0,0],
        [0,0,1,0,0,0,0,0],
        [1,1,1,0,0,0,0,0],
        [0,0,0,0,0,1,1,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]
grid = ColorEightByEight(address=0x70)
iter =0;
while(True):
    iter=iter+1
    for i in range(0,8):
        for j in range(0,8):
            if (board[i][j]):
                grid.setPixel(i, j, i%4)
            else:
                grid.clearPixel(i-1,j-1)
    neighbors = [[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]
    for i in range(0,8):
        for j in range(0,8):
            for k in [-1,0,1]:
                for m in [-1,0,1]:
                    if(not((k==0) and (m==0))):
                        neighbors[i][j] += board[(i+k)%8][(j+m)%8]
    for i in range(0,8):
        for j in range(0,8):
            if (((board[i][j] == 1) and (neighbors[i][j] == 2 or neighbors[i][j] == 3)) or ((neighbors[i][j] == 3) and (board[i][j] == 0))):
                board[i][j] = 1
            else:
                board[i][j] = 0
