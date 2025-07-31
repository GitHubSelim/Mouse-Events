# Getting Started

## MouseEvents - Setup Guide 💡

Welcome, this guide will walk you through running the **MouseEvents** project step-by-step - even if you're new to Python or programming. No experience needed.

---

###  1. Download the Project ZIP

> ✅ The code is **portable**, meaning it works directly from the downloaded folder - no extra file setup required.

1. Go to the GitHub repo (example):\
[https://github.com/GitHubSelim/Mouse-Events](https://github.com/GitHubSelim/Mouse-Events)

3. Click the green **Code** button → **Download ZIP**

4. Extract the `.zip` file to your desktop or a folder of your choice.


### B. Clone via Git (Optional, if you prefer Git over ZIP:)
> Remember you need to have [git](https://git-scm.com/downloads) installed 
If you prefer using the terminal:
```bash
git clone https://github.com/GitHubSelim/Mouse-Events.git
cd MouseEvents
```
---
### 🐍 2. Install Python (if you haven’t)

> Skip this step if you already have Python installed.

1. Go to: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Download **Python 3.7** or higher
3.  On the installer screen, make sure to **check** the box:\
    “Add Python to PATH”
4. Finish the install

---

###  3. Install Required Libraries


1. Open the folder where you extracted the project

2. In the white area of the folder, **hold Shift** + **Right-click**, then choose:\
**“Open PowerShell window here” (or "Open Terminal" on newer Windows)**

3. Paste this command and hit **Enter**:

```bash
pip install pynput
```

That’s it! 

---

### ▶️ 4. Run the Mouse Recorder

This will record your mouse movements until you **left-click**.

1. In the same terminal, type:

```bash
python GeanyMouse3.py
```

2. The program waits for **Ctrl key** → then starts recording
3. Move the mouse around
4. Left-click → saves the movements
5. Right-click → cancels

Your mouse data is saved in the `inputs/` folder as `events0.txt`, `events1.txt`, etc.

---

### 🔀 5. Replay Mouse Movements

1. Run the replayer:

```bash
python Replay_Mouse.py
```

2. Enter:

   - How many replays? → (e.g., `1`)
   - Which file? → (e.g., `0` for `events0.txt`)
   - Paint mode? → (`y` = yes, `n` = no)

3. The mouse will move automatically — just like you recorded it!\
   🖌️ If paint mode is on, it will click to draw.
   **Remember to switch up to a empty canvas in 5 seconds(Eg. Microsoft Paint or GIMP)**

---

###  6. Explore the Extras

- `listener_demo.py`: Shows mouse coordinates when Ctrl is pressed
- `controller_demo.py`: Tries out mouse and keyboard control
- `scratch_game.sb3`: A click-based game (opens in [Scratch](https://scratch.mit.edu))
- `a_value.txt`: Keeps track of the number of recordings

---

### 🚀 Cross-Platform Notes

* Fully tested on **Windows 10/11**  Python 3.11  
* Uses `ctypes` for DPI-awareness (Windows only)  
* Should work on **Linux/macOS**, but not fully tested  
* `tkinter` is used to get screen size  


### 🧐 What’s Next?

You can now:

- Create automated drawings
- Record and replay natural movement

---

### 💬 Need Help?

If you have trouble:

- Open an issue on GitHub
- Or contact me at: `projects.selim@gmail.com`

---

> Don’t just learn it; break, fix, then reinvent it.
