import pyautogui
import time
import pyperclip

# Step 1: Click on the icon
pyautogui.click(1071, 1061)
time.sleep(1)  # Wait for the app to open

# Step 2: Drag from (661, 276) to (735, 934) to select text
pyautogui.moveTo(661, 276)
pyautogui.mouseDown()
pyautogui.moveTo(735, 934, duration=0.5)  # Smooth drag
pyautogui.mouseUp()
time.sleep(0.5)

# Step 3: Copy selected text
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)

# Step 4: Get copied text from clipboard
copied_text = pyperclip.paste()

# Output (or use as needed)
print("Copied text:\n", copied_text)
