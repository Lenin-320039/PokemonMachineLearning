import values_xywalpha as values

def actualizar_pesos(grad, alpha):
    # Nueva experiencia = vieja experiencia + (aprendizaje * gradiente)
    # Usamos map para actualizar ambos pesos a la vez sin for
    w_nuevos = list(map(lambda w_v, g: w_v + (alpha * g), values.w, grad))
    return w_nuevos
