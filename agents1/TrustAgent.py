from matrx.agents.agent_utils.state import State

from brains1.ArtificialBrain import ArtificialBrain


class TutorialAgent(ArtificialBrain):

    def __init__(self, slowdown, condition, name, folder):
        super().__init__(slowdown, condition, name, folder)
        self._slowdown = slowdown
        self._humanName = name
        self._folder = folder
        self._condition = condition

    def initialize(self):
        pass

    def filter_observations(self, state):
        pass

    def decide_on_action(self, state: State):
        pass

    def get_log_data(self):
        pass