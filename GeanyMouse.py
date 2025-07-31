from pynput import mouse, keyboard
import time

mouseC = mouse.Controller()
keyboardC = keyboard.Controller()

a = 0

foldername = f"events.txt{a}"

def on_move(x, y):
	print(f"Mouse has moved to {x}, {y}!")
	current_time = time.time()
	
	with open(foldername, 'a') as f:
		f.write(f"{current_time},{x},{y}\n")

def on_click(x, y, button, pressed):
	if button == mouse.button.Left and pressed:
		return False

	
with mouse.Listener(on_move=on_move, on_click=on_click) as dinle:
	dinle.join()
	

# ~ mouse_listener.start()
# ~ time.sleep(10)
# ~ mouse_listener.stop()


