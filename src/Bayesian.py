# Universidad del valle de guatemala
# Inteligencia Artificial
# Marco Jurado 20308
# Bayesian.py

from Nodes import *

class Bayes:
    def __init__(self,nodosBayes) -> None:
        self.nodosBayes = nodosBayes

    # forma compacta de red baysiana
    def compacta(self):
        compactaSTR = "\n".join(str(nodoBayesiano) for nodoBayesiano in self.nodosBayes) + "\n" #.join para iterar los elementos.
        return compactaSTR

    # factores de la red - needs work
    def factoresRed(self):
        factorSRT = "\n".join(str(tabla) for tabla in self.nodosBayes) + "\n" #.join para iterar los elementos.
        return factorSRT

    # esta descrita la red?
    #def descrita(self):
