# Este ejercicio si bien pude resolverlo, me costo decidir qué 
# estructura usar para separar las letras y contarlas. Al
# principio pense en un diccionario de clave letra y de contenido
# las apariciones, despues recordé que las cadenas tienen funciones
# muy útiles y opté por eso.

# funcion que devuelve si es primo o no un numero
def es_Primo(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2,n-1):
            if(n % x==0):
                return False
        return True 

cadena = input('Ingrese una cadena:').replace(",","").replace(" ","").lower()
# formo un conjunto con las letras de cadena
conj_cadena = set(cadena)          

# imprimo apariciones y veo cuantas aparicieron un nro primo de veces
primos = []
for letra in conj_cadena:
    cant_por_letra = cadena.count(letra) 
    if (cant_por_letra == 1):
        print("La letra ",letra," aparece: ",cant_por_letra," vez.")
    else:
        print("La letra ",letra," aparece: ",cant_por_letra," veces.")
    if (es_Primo(cant_por_letra)):
        primos.append(letra)

# imprimo resultado de primos
if(len(primos) == 0):
    print("Por lo tanto, ninguna letra aparece un numero primo de veces.")
else:
    print("Por lo tanto, las letras ",', '.join(primos)," aparecen un numero primo de veces.")

