# Python Keylogger Script
This Python script records every key you press on your keyboard and saves it in a text file called `keyfile.txt`. It uses the `pynput` library to detect and log the keys.

## How It Works
1. **Listening to Keystrokes:**
   - The script listens to every key you press on your keyboard.
   - Each time you press a key, it saves it to a file.

2. **Logging Keystrokes:**
   - Regular keys (like letters and numbers) are saved as they are.
   - Special keys (like `Shift`, `Enter`, `Ctrl`) are saved with brackets around them (e.g., `[Shift]`).

3. **Saving to a File:**
   - All the keys you press are saved in a file called `keyfile.txt`.
   - The file keeps adding new keys until you stop the script.

## Requirements
To run this script, you need to have Python and the `pynput` library installed. Install `pynput` using this command:

```In bash---> pip install pynput ```

## How to Run the Script
1. **Install Dependencies:**
   - Make sure Python and `pynput` are installed on your computer.

2. **Run the Script:**
   - Run the script by typing:

   ```In bash---> python keylogger.py```

3. **View Logged Keystrokes:**
   - Open the `keyfile.txt` file to see the keys you’ve pressed.

## Stopping the Keylogger
- The script will keep running and logging keys until you stop it. You can stop it by closing the terminal or pressing `Ctrl + C`.

## IMPORTANT NOTE: 
- **Use Responsibly:** This script is meant for learning. Don’t use it to record keystrokes without permission—it’s illegal and unethical.
