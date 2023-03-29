# REGLA DE SARRUS PARA CALCULAR EL DETERMINANTE DE UNA MATRIZ 3x3 DE FORMA ITERATIVA

def determinante_sarrus(matriz):
    if len (matriz) != 3 or len (matriz[0]) != 3:
        raise ValueError ( "La matriz debe ser 3x3" )
    
    diagonal_principal = matriz[0][0] * matriz[1][1] * matriz[2][2] + matriz[0][1] * matriz[1][2] * matriz[2][0] + matriz[0][2] * matriz[1][0] * matriz[2][1]

    diagonal_secundaria = matriz[0][2] * matriz[1][1] * matriz[2][0] + matriz[0][1] * matriz[1][0] * matriz[2][2] + matriz[0][0] * matriz[1][2] * matriz[2][1]

    return diagonal_principal - diagonal_secundaria

if __name__ == "__main__":
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(determinante_sarrus(matriz))
