import pyautogui

# print(pyautogui.size())

width, height = pyautogui.size()

# print(width)

print(pyautogui.position())  # Shows mouse position

# pyautogui.moveTo(10, 10)  # Moves mouse
# pyautogui.moveTo(10, 10, duration=1.5)
# pyautogui.moveRel(200, 0)  # Move mouse from its current

# pyautogui.click(31, 1057)  # Mouse click
# pyautogui.rightClick()
# pyautogui.middleClick()
# pyautogui.doubleClick()

# Failsafe shut the program by moving mouse to (0, 0)
# pyautogui.displayMousePosition()  # Use this on command line to live display
# colour under mouse pointer
