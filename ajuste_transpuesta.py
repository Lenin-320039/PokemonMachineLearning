import values_xywalpha as values
import errorvector as evector

#Calculamos el gradiente (X transpuesta por e)
# Columna 0 y columna 1
grad = [
    sum(map(lambda fila, err: fila[0] * err, values.x, evector.e)),
    sum(map(lambda fila, err: fila[1] * err, values.x, evector.e))
]
