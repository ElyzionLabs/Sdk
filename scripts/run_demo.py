from core.elyzion import Elyzion

agent = Elyzion()

tasks = [
    "Open browser",
    "Click login button",
    "Fill form"
]

for task in tasks:
    print(agent.run(task))
