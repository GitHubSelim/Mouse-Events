from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController

mouse = MouseController()
keyboard = KeyboardController()

def onMove(x, y):
	print(f"Mouse has moved to {x}, {y}!")
	mouse.position = (x, y)
	
cur = mouse.position
print(f"{cur}")

onMove(954, 74)
