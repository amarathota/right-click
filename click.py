import pyautogui
import time
from pynput import keyboard

running = True

def click_mouse():
    pyautogui.click()
    print("right click action done after 30 sec!")

def on_press(key):
    global running
    try:
        if key.char == 'q':
            running = False
            return False  # Stop listener
    except AttributeError:
        pass


listener = keyboard.Listener(on_press=on_press)
listener.start()


try:
    while running:
        click_mouse()
        time.sleep(30)
except KeyboardInterrupt:
    print("Script interrupted by user by pressing q.")

# Clean up code if needed
print("Bye!")
