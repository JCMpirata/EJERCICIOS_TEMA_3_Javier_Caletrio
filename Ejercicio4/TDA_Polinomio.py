# TDA Polinomio de manera recursiva

class Nodo:
    def __init__(self, coeficiente, exponente):
        self.coeficiente = coeficiente
        self.exponente = exponente
        self.siguiente = None

class Polinomio:
    def __init__(self):
        self.cabeza = None

    def agregar(self, coeficiente, exponente):
        nuevo = Nodo(coeficiente, exponente)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            aux = self.cabeza
            while aux.siguiente is not None:
                aux = aux.siguiente
            aux.siguiente = nuevo

    def mostrar(self):
        aux = self.cabeza
        while aux is not None:
            print(aux.coeficiente, "x^", aux.exponente, end=" ")
            aux = aux.siguiente
        print()

    def evaluar(self, x):
        aux = self.cabeza
        resultado = 0
        while aux is not None:
            resultado += aux.coeficiente * x ** aux.exponente
            aux = aux.siguiente
        return resultado

    def suma(self, polinomio):
        aux1 = self.cabeza
        aux2 = polinomio.cabeza
        polinomio_resultante = Polinomio()
        while aux1 is not None and aux2 is not None:
            if aux1.exponente == aux2.exponente:
                polinomio_resultante.agregar(aux1.coeficiente + aux2.coeficiente, aux1.exponente)
                aux1 = aux1.siguiente
                aux2 = aux2.siguiente
            elif aux1.exponente > aux2.exponente:
                polinomio_resultante.agregar(aux1.coeficiente, aux1.exponente)
                aux1 = aux1.siguiente
            else:
                polinomio_resultante.agregar(aux2.coeficiente, aux2.exponente)
                aux2 = aux2.siguiente
        while aux1 is not None:
            polinomio_resultante.agregar(aux1.coeficiente, aux1.exponente)
            aux1 = aux1.siguiente
        while aux2 is not None:
            polinomio_resultante.agregar(aux2.coeficiente, aux2.exponente)
            aux2 = aux2.siguiente
        return polinomio_resultante
    
    def resta(self, polinomio):
        aux1 = self.cabeza
        aux2 = polinomio.cabeza
        polinomio_resultante = Polinomio()
        while aux1 is not None and aux2 is not None:
            if aux1.exponente == aux2.exponente:
                polinomio_resultante.agregar(aux1.coeficiente - aux2.coeficiente, aux1.exponente)
                aux1 = aux1.siguiente
                aux2 = aux2.siguiente
            elif aux1.exponente > aux2.exponente:
                polinomio_resultante.agregar(aux1.coeficiente, aux1.exponente)
                aux1 = aux1.siguiente
            else:
                polinomio_resultante.agregar(-aux2.coeficiente, aux2.exponente)
                aux2 = aux2.siguiente
        while aux1 is not None:
            polinomio_resultante.agregar(aux1.coeficiente, aux1.exponente)
            aux1 = aux1.siguiente
        while aux2 is not None:
            polinomio_resultante.agregar(-aux2.coeficiente, aux2.exponente)
            aux2 = aux2.siguiente
        return polinomio_resultante

    def multiplicacion(self, polinomio):
        aux1 = self.cabeza
        aux2 = polinomio.cabeza
        polinomio_resultante = Polinomio()
        while aux1 is not None:
            while aux2 is not None:
                polinomio_resultante.agregar(aux1.coeficiente * aux2.coeficiente, aux1.exponente + aux2.exponente)
                aux2 = aux2.siguiente
            aux1 = aux1.siguiente
            aux2 = polinomio.cabeza
        return polinomio_resultante
    
    def dividir(self, polinomio):
        aux1 = self.cabeza
        aux2 = polinomio.cabeza
        polinomio_resultante = Polinomio()
        while aux1 is not None:
            while aux2 is not None:
                polinomio_resultante.agregar(aux1.coeficiente / aux2.coeficiente, aux1.exponente - aux2.exponente)
                aux2 = aux2.siguiente
            aux1 = aux1.siguiente
            aux2 = polinomio.cabeza
        return polinomio_resultante
    
    def derivar(self):
        aux = self.cabeza
        polinomio_resultante = Polinomio()
        while aux is not None:
            polinomio_resultante.agregar(aux.coeficiente * aux.exponente, aux.exponente - 1)
            aux = aux.siguiente
        return polinomio_resultante
    
    def integrar(self):
        aux = self.cabeza
        polinomio_resultante = Polinomio()
        while aux is not None:
            polinomio_resultante.agregar(aux.coeficiente / (aux.exponente + 1), aux.exponente + 1)
            aux = aux.siguiente
        return polinomio_resultante
    
    def eliminar_termino(self, exponente):
        aux = self.cabeza
        if aux.exponente == exponente:
            self.cabeza = aux.siguiente
        else:
            while aux.siguiente is not None:
                if aux.siguiente.exponente == exponente:
                    aux.siguiente = aux.siguiente.siguiente
                    break
                aux = aux.siguiente

    def modificar_termino(self, exponente, coeficiente):
        aux = self.cabeza
        while aux is not None:
            if aux.exponente == exponente:
                aux.coeficiente = coeficiente
                break
            aux = aux.siguiente

    def buscar_termino(self, exponente):
        aux = self.cabeza
        while aux is not None:
            if aux.exponente == exponente:
                return aux.coeficiente
            aux = aux.siguiente
        return None
    
    def __str__(self):
        aux = self.cabeza
        polinomio = ""
        while aux is not None:
            polinomio += str(aux.coeficiente) + "x^" + str(aux.exponente) + " "
            aux = aux.siguiente
        return polinomio

if __name__ == "__main__":
    polinomio1 = Polinomio()
    polinomio1.agregar(2, 2)
    polinomio1.agregar(3, 1)
    polinomio1.agregar(4, 0)
    polinomio2 = Polinomio()
    polinomio2.agregar(1, 2)
    polinomio2.agregar(2, 1)
    polinomio2.agregar(3, 0)
    print(polinomio1)
    print(polinomio2)
    print(polinomio1.suma(polinomio2))
    print(polinomio1.resta(polinomio2))
    print(polinomio1.multiplicacion(polinomio2))
    print(polinomio1.dividir(polinomio2))
    print(polinomio1.derivar())
    print(polinomio1.integrar())
    print(polinomio1.evaluar(2))
    polinomio1.eliminar_termino(2)
    print(polinomio1)
    polinomio1.modificar_termino(1, 5)
    print(polinomio1)
    print(polinomio1.buscar_termino(1))

    
