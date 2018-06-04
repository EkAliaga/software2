def abecedario(entero):
    lista = []
    for x in (map(chr, range(entero, 123, ))):
        lista.append(x)
    return lista


def matriz(entero):
    matriz1 = {}
    lista = abecedario(entero)
    matriz1 = matriz1.fromkeys(lista)
    cont = 0
    while entero < 123:
        for x in lista:
            listaD = abecedario(entero)
            matriz1[x] = listaD + lista[0:cont]
            entero += 1
            cont += 1
    return matriz1


def imprimir(matrizE):
    lista = abecedario(97)
    for x in lista:
        print(matrizE[x])
        print


def vigenere():
    tabla = matriz(97)
    palabra2 = ""
    cont = 0
    cont2 = 0
    texto = raw_input("Ingresa el Texto :")  ##hola
    clave = raw_input("Ingrese clave :")  ##delfin
    texto = texto.replace(' ', '')
    clave = clave.replace(' ', '')
    lista3 = abecedario(97)
    for x in texto:
        lista2 = tabla.get(clave[cont])
        for q in lista3:
            if q == x:
                q = "a"
                break
            cont2 += 1
        palabra2 += lista2[cont2]
        cont2 = 0
        cont += 1
        if cont >= len(clave):
            cont = 0
    print(palabra2)
    principal()


def Dvigenere():
    tabla = matriz(97)
    texto = raw_input("Ingresa el Texto :")
    clave = raw_input("Ingrese clave :")
    texto = texto.replace(' ', '')
    clave = clave.replace(' ', '')
    lista1 = abecedario(97)
    cont = 0
    cont2 = 0
    palabra = ""
    for x in texto:
        lista2 = tabla.get(clave[cont])
        for n in lista2:
            if n == x:

                break
            cont2 += 1
        palabra += lista1[cont2]
        cont += 1
        cont2 = 0
        if cont >= len(clave):
            cont = 0
    print(palabra)
    principal()

def clave():
    tabla = matriz(97)
    texto = raw_input("Ingresa el Texto :")
    clave = raw_input("Ingrese Texto Cifrado :")
    texto = texto.replace(' ', '')
    clave = clave.replace(' ', '')
    lista1 = abecedario(97)
    cont = 0
    cont2 = 0
    palabra = ""
    for x in texto:
        for w in lista1:
            if x == w:
                break
            cont += 1

        for z in lista1:
            lista2 = tabla.get(z)
            if clave[cont2] == lista2[cont]:
                palabra += lista2[0]
                break
        cont = 0
        cont2 += 1
    '''repeticiones = 0
    cont4 = 0
    cont5 = 0
    for m in palabra:
        if m == palabra[0]:
            repeticiones += 1
        cont4 += 1
        if repeticiones == 1:
            cont5 = cont4
    if repeticiones >= 3:
        palabra = palabra[0:cont5]'''
    print (palabra)
    principal()



def principal():
    print("VIGENERE: ")
    print("1.- Encriptar ")
    print("2.- Desencriptar")
    print("3.- Clave")
    print("4.- Salir")
    print("4.- Salir")
    w = int(input("Seleccione una opcion: "))

    opciones = {1: vigenere ,2: Dvigenere ,3: clave, 4:exit}

    opcion = opciones[w]()
    print (opcion)

##clave()
principal()
##vigenere()
##Dvigenere()
