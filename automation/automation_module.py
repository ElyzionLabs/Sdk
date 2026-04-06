import pyautogui

class AutomationModule:
    def execute(self, instruction):
        print(f"[Automation] Executing: {instruction}")

        if instruction["action"] == "click":
            pyautogui.click(100, 100)  # dummy position

        return "Task executed"
