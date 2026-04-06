from core.elyzion import Elyzion

def test_run():
    agent = Elyzion()
    result = agent.run("Test task")

    assert result == "Task executed"
