import errorvector as evector

#Elevamos cada error al cuadrado y los sumamos
# Esto es la base del Error Cuadratico Medio
ErrorTotal1 = sum(map(lambda err: err ** 2, evector.e))
