from pynput import mouse, keyboard
from pynput.keyboard import Key

mouseC = mouse.Controller()

print(type(mouseC.position))