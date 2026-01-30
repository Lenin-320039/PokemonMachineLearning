from values_xywalpha import *



def predecir_fila(fila):
    # Multiplicamos habilidad * peso y sumamos el resultado
    return sum(map(lambda val, peso: val * peso, fila, w))

# Obtenemos y_hat (predicciones)
y_hat = list(map(predecir_fila, x))

#ERROR CUADRATICO
#Comparamos y_real vs y_hat para ver que tanto fallo el instinto de Arcanine

def calcular_error_cuadratico(reales, predichos):
    n = len(reales)
    # Calculamos (real - predicho) a la 2 para cada par de datos
    diferencias_sq = map(lambda r, p: (r - p) ** 2, reales, predichos)
    #promediamos el resultado
    return sum(diferencias_sq) / n
error_total = calcular_error_cuadratico(y_real, y_hat)

#RESULTADOS
print(f"Predicciones de Arcanine (y_hat): {y_hat}")
print(f"error Cuadratico Medio: {error_total}")
