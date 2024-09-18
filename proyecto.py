nombre1 = input( " Escribe tu nombre: ")
print(" Miss: bienvenidos jóvenes al grupo 4, hoy tenemos una sesión de preguntas en esta clase de matemáticas....")
print(" Alejandro: no miss, si apenas ayer tuvimos exámen :(")
print(" Miss: lo siento jóvenes, ahora sigamos con la sesión de preguntas ")
print(nombre1 + " ,empecemos contigo, dime, ¿cuánto es 2 + 7?: ")
resultado1 = int(input("Escribe el resultado"))
if resultado1 == 9:
    print("Miss: correcto")
    print("Miss: bien, ahora una pregunta para Alejandro")
    print("Miss: Alejandro, cuánto es 5 + 5?_ ")
    print("Alejandro: pssss, " + nombre1)
    resultado2 = int(input("¿cuanto es 5 + 5?"))
    if resultado2 == 10:
        print("Alejandro: 10")
        print("Miss: correcto")
        print("Miss: la pregunta final, se la voy a preguntar a " + nombre1)
        print("¿Miss: ¿cuánto es 69 x 87?") 
    resultado3 = int(input("¿Cuánto es 69 x 87?"))
    if resultado3 == 6003:
        print("Miss: ¡Correcto, muy bien!")
        print("Miss: muchas gracias jóvenes, hasta aquí la sesión de preguntas")
else:
    print("Miss: incorrecto")
