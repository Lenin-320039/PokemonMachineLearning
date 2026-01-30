import values_xywalpha as values
import y_predictiva as yp

#Se calcula el vector de error "e"
# e = y_real - y_hat
e = list(map(lambda r, p: r - p, values.y_real, yp.y_hat))
