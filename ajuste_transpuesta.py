import values_xywalpha as values

#Traemos el error "e" que se calcula en el main
def calcular_gradiente(e):
    #sumamos (columna_x * error)
    # Gradiente para peso 1 y peso 2
    g0 = sum(map(lambda fila,err: fila[0] * err, values.x, e))
    g1 = sum(map(lambda fila, err: fila[1] * err, values.x, e))
    return [g0, g1]
