import directkeys as dk
import time 
from directkeys import PressKey, ReleaseKey


LJoyUp = dk.W
LJpyLeft = dk.A
LJoyDown = dk.S
LJoyRight = dk.D


A = dk.SPACE
B = dk.LCONTROL
Y = dk.KEY_1
X = dk.R

options = dk.V
RJoyPress = dk.C
pause = dk.B 
LJoyPress = dk.LSHIFT

ArrowLeft = dk.LEFT
ArrowRight  = dk.RIGHT
ArrowUp = dk.UP
ArrowDown = dk.DOWN

def pressA(delay=0.15):
    PressKey(A)
    time.sleep(delay)
    ReleaseKey(A)

def pressB(delay=0.15):
    PressKey(B)
    time.sleep(delay)
    ReleaseKey(B)

def pressX(delay=0.15):
    PressKey(X)
    time.sleep(delay)
    ReleaseKey(X)

def pressY(delay=0.15):
    PressKey(Y)
    time.sleep(delay)
    ReleaseKey(Y)

if __name__ == '__main__':
    delay = 0.15
    pressA()
    time.sleep(delay)
    pressB()
    time.sleep(delay)
    pressX()
    time.sleep(delay)
    pressY()
    time.sleep(delay)


