from core.elyzion import Elyzion

if __name__ == "__main__":
    agent = Elyzion()
    result = agent.run("Click the submit button on screen")

    print("[Result]:", result)
