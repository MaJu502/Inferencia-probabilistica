from Bayesian import *
from Nodes import *

# creando noodos
A = BayesNode(estados=[True,False], tag='A')
B = BayesNode(estados=[True,False], tag='B')
C = BayesNode(estados=[True, False], tag='C', relSuperior=[A,B])

# dando valores iniciales de red 
A.agregarCompound((), {True: 0.5, False: 0.5})
B.agregarCompound((), {True: 0.5, False: 0.5})
C.agregarCompound((False, True), {True: 0.2, False: 0.8})
C.agregarCompound((False, False), {True: 0.70, False: 0.3})
C.agregarCompound((True, True), {True: 0.25, False: 0.75})
C.agregarCompound((True, False), {True: 0.8, False: 0.2})

Red = Bayes([A,B,C]) # red bayesiana

test = {'A': True, 'B': False, 'C': True} # pregunta al modelo de red bayesiana

print('\n\n\n ------------------------------------------------------------------------1')
print(Red.verificarDescrita())
print('\n\n\n ------------------------------------------------------------------------2')
print(Red.representacionCompacta())
print('\n\n\n ------------------------------------------------------------------------3')
print(Red.factoresRedBayesiana())
print('\n\n\n ------------------------------------------------------------------------4')
print(Red.consulta(test))