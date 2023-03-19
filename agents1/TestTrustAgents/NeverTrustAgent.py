from agents1.TrustAgent import TrustAgent
from matrx.agents import StateTracker, Navigator


class NeverTrustAgent(TrustAgent):
    def get_trust(self, folder):
        trustBeliefs = {}
        trustBeliefs[self._humanName] = {'competence': -1.0, 'willingness': -1.0}
        return trustBeliefs

    def update_trust(self, competence, willingness, folder):
        pass
