import random as rand

from agents1.TrustAgent import TrustAgent
from matrx.agents import StateTracker, Navigator


class RandomTrustAgent(TrustAgent):
    def get_trust(self, folder):
        trustBeliefs = {}
        competence = rand.randint(-10, 10)/10
        willingness = rand.randint(-10, 10) / 10
        trustBeliefs[self._humanName] = {'competence': competence, 'willingness': willingness}
        print("random competence = ", competence, " willingness = ", willingness)
        return trustBeliefs

    def update_trust(self, competence, willingness, folder):
        pass
