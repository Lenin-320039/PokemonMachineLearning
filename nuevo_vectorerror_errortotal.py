import values_xywalpha as values
import nueva_prediccion as np

#1 calculamos el nuevo vector de error (e_nuevo)
e_nuevo = list(map(lambda r, p: r - p, values.y_real, np.y_hat_nueva))

#2 Calculamos el nuevo Error Total
#Sumamos los cuadrados de cada elemento del vector e_nuevo
ErrorTotal_nuevo = sum(map(lambda err: err ** 2, e_nuevo))
