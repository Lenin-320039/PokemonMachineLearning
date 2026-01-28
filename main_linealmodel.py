import values_xywalpha as values
import y_predictiva as yp
import ajuste_transpuesta as at
import ajuste_pesos as ap

# 1. Definimos Alpha (Tasa de aprendizaje)
alpha = 0.01

#2 Obtenemos predicciones (y_hat) y el error vectorial (e)
y_hat = yp.y_hat
e = list(map(lambda r, p: r - p, values.y_real, y_hat))

#3 Calculamos el Gradiente usando el módulo de transpuesta
gradiente = at.calcular_gradiente(e)

# 4. Ajustamos los Pesos usando el módulo de ajuste
nuevos_pesos = ap.actualizar_pesos(gradiente, alpha)

# SALIDA DE DATOS 
print("   REPORTE DE ENTRENAMIENTO ARCANINE      ")
print(f"Predicciones (y_hat):   {y_hat}")
print(f"Vector de Error (e):    {e}")
print(f"Gradiente (X^T e):      {gradiente}")
print(f"Pesos Originales (w):   {values.w}")
print(f"NUEVOS PESOS (w):       {nuevos_pesos}")


