from vision.vision_module import VisionModule
from language.language_module import LanguageModule
from automation.automation_module import AutomationModule

class Elyzion:
    def __init__(self):
        self.vision = VisionModule()
        self.language = LanguageModule()
        self.automation = AutomationModule()

    def run(self, task: str):
        print(f"[Elyzion] Task received: {task}")

        visual_data = self.vision.capture_screen()
        interpreted = self.language.process(task, visual_data)

        result = self.automation.execute(interpreted)

        return result
