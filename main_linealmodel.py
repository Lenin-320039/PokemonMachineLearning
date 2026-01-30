import values_xywalpha as values
import y_predictiva as yp
import errortotal as errort
import ajuste_transpuesta as at
import ajuste_pesos as ap
import nueva_prediccion as np
import nuevo_vectorerror_errortotal as nve
# 1. Definimos Alpha (Tasa de aprendizaje)
alpha = 0.01

#2 Obtenemos predicciones (y_hat) y el error vectorial (e)
y_hat = yp.y_hat
e = list(map(lambda r, p: r - p, values.y_real, y_hat))

#3 Calculamos el Gradiente usando el módulo de transpuesta
gradiente = at.grad




# SALIDA DE DATOS 
print("   REPORTE DE ENTRENAMIENTO ARCANINE      ")
print(f"1. Error Inicial:       {errort.ErrorTotal1}")
print(f"2. Gradiente (X^T e):   {at.grad}")
print(f"3. NUEVOS PESOS (w):    {ap.w_nuevos}")
print(f"4. Nueva Predicción:    {np.y_hat_nueva}")
print(f"5. Nuevo Vector Error:  {nve.e_nuevo}")
print(f"6. NUEVO ERROR TOTAL:   {nve.ErrorTotal_nuevo}")

if nve.ErrorTotal_nuevo < errort.ErrorTotal1:
    print("¡RESULTADO: Arcanine ha mejorado su precisión!")
else:
    print("RESULTADO: El error no bajó. Revisa el valor de alpha.")
