from pynput import mouse, keyboard
from pynput.keyboard import Key
import time
import os
import tkinter as tk

# For screen resolution
if os.name == 'nt':
	import ctypes
	try:
		ctypes.windll.shcore.SetProcessDpiAwareness(2) 
	except Exception:
		pass

root = tk.Tk()
root.withdraw()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()

#-------------------------------Initialize--------------------------------#

cwd = os.getcwd() #Current working directory

mouseC = mouse.Controller()
keyboardC = keyboard.Controller()

directory = os.path.join(cwd, "inputs")

a = None
with open("a_value.txt", 'r') as f:
	a = int(f.read())

positions = []
foldername = f"events{a}.txt"
file_path = os.path.join(directory, foldername)

def on_move(x, y):
	print(f"moved{x}, {y}")
	current_time = time.time() 
	cur_time_3dp = round(current_time, 3)
	positions.append(f"{cur_time_3dp},{x},{y}\n")
		

def on_click(x, y, button, pressed):

	global foldername, a, file_path
	foldername = f"events{a}.txt"
	file_path = os.path.join(directory, foldername)

	if button == mouse.Button.left and pressed:
		print(f"{foldername} created")
		with open(file_path, 'w') as f:

			f.write(f"RESOLUTION:{screen_width},{screen_height}\n") #screen resolution
			f.writelines(positions) # Write all positions at once for better performance
	
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
