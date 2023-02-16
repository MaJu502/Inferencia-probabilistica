# Universidad del valle de guatemala
# Inteligencia Artificial
# Marco Jurado 20308
# Nodes.py

# Se utilizan nodos para representar los elementos de la red bayesiana como visto en clase.
class BayesNode:
    def __init__(self, estados, tag, relSuperior = None, cmpTable = None) -> None:
        self.estados = estados
        self.tag = tag

        # relación superior = nodos que afectan la probablidad del nodo en discusión.
        if relSuperior is not None:
            self.relSuperior = relSuperior
        else:
            self.relSuperior = []
 
        # key = combinación de padres  
        # value = probabilidad que toma el nodo dada la prob de los padres.
        if cmpTable is not None:
            self.CompoundTable = cmpTable
        else:
            self.CompoundTable = {}

    # agregar relaciones que afectaran al nodo
    def nuevaConexionSuperior(self, x):
        self.relSuperior.append(x)
    
    def agregarCompound(self,x):
        self.CompoundTable.append(x)

    def Describir(self):
        retorno = ''
        retorno += 'Nodo: ' + str(self.tag) + '\n  relaciones superiores:\n'
        for p in self.relSuperior:
            retorno += '    - ' + str(p) + '\n'
        retorno += '  relaciones del nodo:\n'
        for relSUP, Probabilidad in self.CompoundTable.items():
            print('    - ' ,relSUP, ":", Probabilidad)