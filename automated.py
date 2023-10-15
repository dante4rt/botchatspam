import pyautogui
import time
import sys

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 3:
    print("Usage: python3 automated.py <message> <n>")
    sys.exit(1)

# Read command-line arguments
message = sys.argv[1]
n = int(sys.argv[2])

time.sleep(3)

for i in range(n):
    pyautogui.typewrite(message + '\n')
