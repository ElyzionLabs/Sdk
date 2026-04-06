import pyautogui
import numpy as np

class VisionModule:
    def capture_screen(self):
        screenshot = pyautogui.screenshot()
        image_array = np.array(screenshot)

        print("[Vision] Screen captured")
        return image_array
