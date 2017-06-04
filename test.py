import time

import pyautogui

from directkeys import PressKey, ReleaseKey, A, D, S, W


def jump():
    ReleaseKey(A)
    ReleaseKey(D)
    ReleaseKey(S)
    PressKey(W)

    time.sleep(0.25)
    ReleaseKey(W)

def jump_back():
    PressKey(W)
    PressKey(A)
    ReleaseKey(D)
    ReleaseKey(S)
    time.sleep(0.25)
    ReleaseKey(W)
    ReleaseKey(A)

while True:       
    jump()
    time.sleep(1)
    jump_back()
