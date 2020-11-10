import pyautogui
import time

message = "test"
n = 5

time.sleep(3)

for i in range(n) :
    pyautogui.typewrite(message + '\n')
