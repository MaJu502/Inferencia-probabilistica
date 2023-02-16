# Universidad del valle de guatemala
# Inteligencia Artificial
# Marco Jurado 20308
# Bayesian.py

from Nodes import *

class Bayes:
    def __init__(self,nodosBayes) -> None:
        self.nodosBayes = nodosBayes

    # forma compacta de red baysiana
    def representacionCompacta(self):
        compactaSTR = "\n".join(nodoBayesiano.Describir() for nodoBayesiano in self.nodosBayes) + "\n" #.join para iterar los elementos.
        return compactaSTR

    # array de tuplas donde los elementos de la tupla son el tag y la tabla de probabilidades. 
    def factoresRedBayesiana(self):
        return [(i.tag, i.CompoundTable) for i in self.nodosBayes]

    # si los estados X estan en los values del compound table entonces la funcion all devuelve true.
    def verificarDescrita(self):
        return all(estado in X.CompoundTable[relacionSuperior] for X in self.nodosBayes for relacionSuperior in X.CompoundTable for estado in X.estados)

    # probabilidad de un evento
    def consulta(self, pregunta):
        # pregunta es un diccionario donde se tiene que dar el tag del nodo y el estado del nodo.
        retorno = 1 # default 
        for X in self.nodosBayes:
            # por cada nodo en la red.
            relSUP = (pregunta[nodoSUP.tag] for nodoSUP in X.relSuperior) # nodos superiores a X
            retorno *= X.CompoundTable.get(tuple(relSUP), X.CompoundTable)[pregunta[X.tag]] # multiplicar de acuerdo con proceso de probabilidad conj. aprendido en clase.
        return retorno