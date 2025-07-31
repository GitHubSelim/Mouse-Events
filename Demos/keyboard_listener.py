from pynput import keyboard
from pynput.keyboard import Key

pos = []

def on_press(key):
	
	if key == Key.space:
		for a in range(len(pos)):
			print(pos[a])
	pos.append(key)

with keyboard.Listener(on_press=on_press) as listen:
	listen.join()

print("keyboard listener finished")
