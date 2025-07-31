from pynput import mouse, keyboard
import ctypes
import time
import os
import tkinter as tk

# ----------------- Screen Resolution Detection -----------------
if os.name == 'nt':
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(2)
    except Exception:
        pass

try:
    root = tk.Tk()
    root.withdraw()
    cur_width = root.winfo_screenwidth()
    cur_height = root.winfo_screenheight()
    root.destroy()
except Exception as e:
    print(f"Error detecting screen resolution: {e}")
    cur_width, cur_height = 1920, 1080  # fallback

# Allow user to override
user_input = input(f"Press Enter to use detected resolution ({cur_width}x{cur_height}), "
                   "or enter as WIDTH,HEIGHT: ")
if user_input.strip():
    try:
        cur_width, cur_height = map(int, user_input.split(","))
    except ValueError:
        print("Invalid input. Using detected resolution.")

# ----------------- Prevent Sleep (Windows only) -----------------
if os.name == 'nt':
    try:
        ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)
    except Exception:
        print("Warning: Could not prevent system sleep.")

cwd = os.getcwd()
inputs_path = os.path.join(cwd, "inputs")

# ----------------- Check for inputs folder -----------------
if not os.path.isdir(inputs_path):
    print("Error: 'inputs' folder not found. Please create it and add event files.")
    exit(1)

mouseC = mouse.Controller()
keyboardC = keyboard.Controller()

def map_x(value):
    return value * cur_width / orig_width

def map_y(value):
    return value * cur_height / orig_height

# Minimum interval between clicks (to avoid too fast clicking)
MIN_CLICK_INTERVAL = 0.01  # 10 ms

# ----------------- Replay Logic -----------------
try:
    try:
        amount = int(input("How many replays do you want to play? "))
    except ValueError:
        print("Invalid input. Defaulting to 1 replay.")
        amount = 1

    pos = []

    for famount in range(amount):
        try:
            folderNum = int(input("Which event do you want to play? "))
        except ValueError:
            print("Invalid event number. Skipping.")
            continue

        foldername = os.path.join(inputs_path, f"events{folderNum}.txt")
        if not os.path.exists(foldername):
            print(f"Error: File {foldername} not found. Skipping.")
            continue

        enable_drawing = input("Do you want paint mode enabled? (y/n) ").strip().lower() == "y"

        pos.clear()
        try:
            with open(foldername, 'r') as f:
                first_line = f.readline().strip()
                if not first_line.startswith("RESOLUTION:"):
                    print("File missing resolution info. Skipping this replay.")
                    continue

                try:
                    orig_width, orig_height = map(int, first_line.replace("RESOLUTION:", "").split(","))
                except ValueError:
                    print("Invalid resolution info in file. Skipping this replay.")
                    continue

                if enable_drawing:
                    print("Starting in 5 seconds... Switch to Paint!")
                    time.sleep(5)

                for line in f:
                    try:
                        timestamp, x, y = line.strip().split(',')
                        pos.append((float(timestamp), float(x), float(y)))
                    except ValueError:
                        print(f"Skipping malformed line: {line}")
                        continue

            if not pos:
                print(f"No valid mouse positions found in {foldername}. Skipping.")
                continue

            last_time = None
            for curtime, x, y in pos:
                if last_time is not None:
                    elapsed_time = curtime - last_time
                    if elapsed_time < MIN_CLICK_INTERVAL:
                        elapsed_time = MIN_CLICK_INTERVAL
                    time.sleep(elapsed_time)
                last_time = curtime

                try:
                    mouseC.position = (map_x(x), map_y(y))
                    if enable_drawing:
                        mouseC.click(mouse.Button.left, 1)
                    print(f"Moved cursor to {map_x(x):.2f}, {map_y(y):.2f}, at {curtime}")
                except Exception as e:
                    print(f"Mouse action failed: {e}")
                    break  # Stop replay if mouse fails repeatedly

            print(f"Finished playing event {folderNum}\nWaiting for the next replay...")

        except Exception as e:
            print(f"Unexpected error while replaying file {folderNum}: {e}")

except KeyboardInterrupt:
    print("\nReplay interrupted by user. Exiting safely.")
