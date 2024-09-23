import pyautogui
import time
import sys
import threading
import keyboard

# delay of program execution
time.sleep(3)  # its in seconds

stop_script = False

def listen_for_esc():
    global stop_script
    while not stop_script:
        if keyboard.is_pressed('esc'):
            print("Stopping the script...")
            stop_script = True
            break

esc_thread = threading.Thread(target=listen_for_esc, daemon=True)
esc_thread.start()

try:
    with open("passwords.txt", "r") as file:
        for line in file:
            if stop_script:
                break

            password = line.strip()
            if not password:
                continue

            print(f"Typing Password: {password}")
            pyautogui.typewrite(password, interval=0)
            pyautogui.press("enter")
            
            time.sleep(0.1)  # Wait for the PDF to process the password

            # Simulate pressing Enter twice with a delay of 0.5 seconds if the password is incorrect
            print("------------------------")
            pyautogui.press("enter")  # First Enter
            #time.sleep(0.3)  # Delay between two Enter presses
            #pyautogui.press("enter")  # Second Enter

except KeyboardInterrupt:
    print("Script was interrupted.")
finally:
    stop_script = True
    esc_thread.join()
    sys.exit()