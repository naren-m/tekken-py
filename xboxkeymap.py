import directkeys as dk
import time 
from directkeys import PressKey, ReleaseKey


options = dk.V
RJoyPress = dk.C
pause = dk.B


LJoyPress = dk.LSHIFT

def pressLJoyPress(delay=0.15):
    PressKey(LJoyPress)
    time.sleep(delay)
    ReleaseKey(LJoyPress)

LJoyUp = dk.W
LJoyLeft = dk.A
LJoyDown = dk.S
LJoyRight = dk.D

def pressLJoyUp(delay=0.15):
    PressKey(LJoyUp)
    time.sleep(delay)
    ReleaseKey(LJoyUp)

def pressLJoyLeft(delay=0.15):
    PressKey(LJoyLeft)
    time.sleep(delay)
    ReleaseKey(LJoyLeft)

def pressLJoyDown(delay=0.15):
    PressKey(LJoyDown)
    time.sleep(delay)
    ReleaseKey(LJoyDown)

def pressLJoyRight(delay=0.15):
    PressKey(LJoyRight)
    time.sleep(delay)
    ReleaseKey(LJoyRight)

LeftArrow = dk.LEFT
RightArrow  = dk.RIGHT
UpArrow = dk.UP
DownArrow = dk.DOWN

def pressLeftArrow(delay=0.15):
    PressKey(LeftArrow)
    time.sleep(delay)
    ReleaseKey(LeftArrow)

def pressRightArrow(delay=0.15):
    PressKey(RightArrow)
    time.sleep(delay)
    ReleaseKey(RightArrow)

def pressUpArrow(delay=0.15):
    PressKey(UpArrow)
    time.sleep(delay)
    ReleaseKey(UpArrow)

def pressDownArrow(delay=0.15):
    PressKey(DownArrow)
    time.sleep(delay)
    ReleaseKey(DownArrow)



A = dk.SPACE
B = dk.LCONTROL
Y = dk.KEY_1
X = dk.R

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


