# REGLA DE SARRUS PARA CALCULAR EL DETERMINANTE DE UNA MATRIZ 3x3 DE FORMA RECURSIVA
def determinante_sarrus(matriz):
    if len(matriz) == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    
    else:
        det = 0
        for i in range(3):
            submatriz = []
            for j in range(1, 3):
                fila = []
                for k in range(3):
                    if k != i:
                        fila.append(matriz[j][k])
                submatriz.append(fila)
            signo = (-1) ** i
            det += signo * matriz[0][i] * determinante_sarrus(submatriz)
        return det
    
if __name__ == "__main__":
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(determinante_sarrus(matriz))