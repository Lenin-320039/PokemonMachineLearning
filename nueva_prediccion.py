import values_xywalpha as values
import ajuste_pesos as ap

#Se usan los pesos nuevos para calcular la prediccione mejorada
def predecir_mejorado(fila):
    return sum(map(lambda val, peso: val * peso, fila, ap.w_nuevos))

y_hat_nueva = list(map(predecir_mejorado, values.x))
