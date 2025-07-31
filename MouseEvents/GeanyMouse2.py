from pynput import mouse, keyboard
from pynput.keyboard import Key
import time
import os

cwd = os.getcwd() #Current working directory

mouseC = mouse.Controller()
keyboardC = keyboard.Controller()

directory = os.path.join(cwd, "inputs")
with open("a_value.txt", 'r') as f:
	global a
	a = int(f.read())

positions = []
foldername = f"events{a}.txt"
file_path = os.path.join(directory, foldername)

def on_move(x, y):
	print(f"moved{x}, {y}")
	current_time = time.time()
	positions.append(f"{current_time},{x},{y}\n")
		


def on_click(x, y, button, pressed):
	global a, foldername, file_path
	if button == mouse.Button.left and pressed:
		print(f"event {a} created")
		with open(file_path, 'a') as f:
			for line in positions:
				f.write(line)
	
		positions.clear()
		a +=1
	
	elif button == mouse.Button.right and pressed:
		return False
			
		
def on_press(key):
	if key == Key.ctrl_l:
		print("CTRL pressed: starting mouse listener")
		return False
				

#input("\n====================================================\nMerhaba bu program mouse'ın sol butonuna basana kadarki hareketleri bir events{sayi}.txt dosyasına kaydeder.\nEğer mouse'un sağ butonuna basarsan da kod sonlanır.\n\nDevam etmek için bir tuşa basıp enterlayın.")
with keyboard.Listener(on_press=on_press) as keyboard_dinle:
	keyboard_dinle.join()
print("keyboard listener finished")

with mouse.Listener(on_move=on_move, on_click=on_click) as mouse_dinle:
	mouse_dinle.join()

with open("a_value.txt", 'w') as f:
	f.write(str(a))

print("script ended")
