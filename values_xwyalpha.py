# X--> Habilidades ... valores entrada
x = [
    [2,5], #fila1
    [4,6], #fila2
    [6,7] #fila3
]

# W--> Experiencia_NivelActual
w = [1.1, 1.0]

# Y_real--> Experiencias previas en combate..justifico estos valores
y_real = [11, 18, 25]

alpha = 0.01
#2 DEFINIMOS LA FUNCION
def predecir_fila(fila):
    return sum(map(lambda val, peso: val * peso, fila, w))

#3 AL FINAL HACEMOS EL CALCULO
y_hat = list(map(predecir_fila, x))

#4 Mostrar resultados
print(f"predicciones: {y_hat}")

#FUNCION DE COSTO
def calcular_error(reales, predichos):
    n = len(reales)
    diff_sq = map(lambda r, p: (r - p) ** 2, reales, predichos)
    return sum(diff_sq) / n

print(f"Error total: {calcular_error(y_real, y_hat)}")
