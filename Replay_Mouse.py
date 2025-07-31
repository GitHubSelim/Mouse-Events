from pynput import mouse, keyboard
import time
import os
import tkinter as tk
import ctypes

# For screen resolution
if os.name == 'nt':
	import ctypes
	try:
		ctypes.windll.shcore.SetProcessDpiAwareness(2)
		ctypes.windll.kernel32.SetThreadExecutionState(0x80000002) # Prevent system sleep 
	except Exception:
		pass

root = tk.Tk()
root.withdraw()
cur_width = root.winfo_screenwidth()
cur_height = root.winfo_screenheight()
root.destroy()

#-------------------------------Initialize--------------------------------#

cwd = os.getcwd()

mouseC = mouse.Controller()
keyboardC = keyboard.Controller()

def map_x(value):
	mapped_value = value * cur_width / orig_width  # Adjust x coordinate
	return mapped_value
	
def map_y(value):
	mapped_value = value * cur_height / orig_height  # Adjust y coordinate
	return mapped_value


#________________________________Replay___________________________________#
amount = input("How many replays do you want to play?")

pos = []

for famount in range(0, int(amount)):

	folderNum = int(input("Which event do you want to play?"))
	foldername = os.path.join(cwd, "inputs", f"events{folderNum}.txt")

	if input("Do you want paint mode enabled? (y/n)") == "y":
		enable_drawing = True
	else:
		enable_drawing = False

	pos.clear()

	with open(foldername, 'r') as f:
		
		first_line = f.readline().strip() # Read the first line for resolution
		orig_width, orig_height = map(int, first_line.replace("RESOLUTION:", "").split(","))

		if enable_drawing:
			print("Starting in 5 seconds... Switch to Paint!")
			time.sleep(5)

		for line in f:
			timestamp, x, y = line.strip().split(',')
			curtime = float(timestamp)
			x = float(x)
			y = float(y)
			
			pos.append((curtime, x, y))
		
	last_time = None
	for a in range(0, len(pos)):
		if last_time is not None:
			elapsed_time = (float(pos[a][0]) - float(last_time))
			time.sleep(elapsed_time)
		
		last_time = float(pos[a][0])
		
		mouseC.position = (map_x(pos[a][1]), map_y(pos[a][2]))
		if enable_drawing:
			mouseC.click(mouse.Button.left, 1)

		print(f"moved cursor to {map_x(pos[a][1])}, {map_y(pos[a][2])}, at {pos[a][0]}")

	if enable_drawing:
		mouseC.release(mouse.Button.left)

	print(f"Finished playing event {folderNum}\nWaiting for the next replay...")
