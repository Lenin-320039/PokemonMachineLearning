import values_xywalpha as values
import ajuste_transpuesta as at

#sustituir el FOR por: w = w + (alpha * gradiente)
# Usamos el alpha definido en tus valores

w_nuevos = list(map(lambda w_v, g: w_v + (values.alpha * g), values.w, at.grad))

