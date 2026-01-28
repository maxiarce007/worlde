# primero creo una lista llamada "letras verificadas"
letras_verificadas = []
#luego defino la cantidad de letras permitidas
cantidad_letras = 5
# cree una funcion que me ayude a comparar la palabra ingresada con la plabra secreta
def verificador_palabra(palabra_ingresada, palabra_secreta):
# creo n bucle for con los parametros necesarios
    for i in range(cantidad_letras):
        las_palabras_son_iguales = palabra_ingresada[i] == palabra_secreta[i] # True o False
        la_letra_existe_en_la_palabra = palabra_ingresada[i] in palabra_secreta 
        
        if las_palabras_son_iguales:
            letras_verificadas.append(f"[{palabra_ingresada[i]}]")
        elif la_letra_existe_en_la_palabra:
            letras_verificadas.append(f"({palabra_ingresada[i]})")
        else: