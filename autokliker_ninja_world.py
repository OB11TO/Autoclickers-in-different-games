import time
import pyautogui
from mss import mss
import random

janken_x = 1253
janken_y = 722

stone_x = 769
stone_y = 803

scissors_x = 886
scissors_y = 803

paper_x = 1013
paper_y = 803

fullStack = [stone_x, scissors_x, paper_x]

def start():
    with mss() as sct:
        while True:
            time.sleep(2)
            pyautogui.click(janken_x, janken_y)
            time.sleep(3)
            pyautogui.click(random.choice(fullStack), stone_y)


def monik_pos():
    while True:
        print(pyautogui.position())


time.sleep(2)
start()
