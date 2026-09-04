# PYTHON
## Temas

-Librerias

## Ejemplos:

# LIBRERIAS:
## numpy:

En librerias tenemos como primero a "numpy" la cual la vamos a declarar una variable para poder ejecutarlo mas sencillo
el codigo para implementarlo seria

"import numpy as np"

Siendo "np" siendo una variable para llamar a la funcion

Ahora esta libreria nos consigue varias funciones, como son demasiadas solo pondre las mas especificas y funcionales, mientras conocemos mas librerias lo iremos poniendo, ahora lo primero que vamos a ver seria la CREACION DE ARREGLOS(ARRAYS)

CODIGOS:

np.random.seed(42): genera numeros aleatorios

np.array([1,2,3]): Con este codigo creamos un arreglo basico con valores ya predefinidos

np.zeros(5): Crea un arreglo de cinco ceros

np.ones((3,3)): Este codigo crea una matriz de 3x3 lleno de unos

np.arange(0,10,2): Crear una secuencia de numeros de 0 al 10 con un paso de 2

np.linspace(0,1,5): Crea cinco numeros ordenados y separados uniforme entre el 0 y 1, osea 0 y 1 son los limites y el 5 que agregamos al final son los datos que quieres que haya, ahora todos tendran la separacion con la misma equivalencia 

## random:

Como esta libreria menciona se trata de funciones randomizadas para poder elegir entre variables para llamar a esta libreria usaremos el codigo

"import random"

A continuacion vamos a ver todos o la mayoria de codigos que normalmente se usa

CODIGOS:

random.seed(42): Sirve para randomizar valores bueno para hacer pruebas y ver diferentes tipos de panoramas

random.randint(a,b): Este codigo lo que genera es un numero entero aleatorio entre a y b (entre ellos mismos incluidos)

random.randrange(0,100,5): Lo que genera este codigo es los multiplos de 5 entre 0 y 100, se empieza desde 5 y acaba en 95 sin incluir el final

random.random(): Este codigo genera un numero decimal aleatorio entre 0.0 y 1.0 usado normalmente como base de porcentaje (no incluye el 1.0)

random.uniform(a,b): Genera un numero decimal aleatorio entre 2 variables cualquiera

marcas= ["Apple", "Samsung", "Sony"]

random.choice(marcas): Devuelve una marca alazar del arreglo

random.choices(lista, k=n)= Elige varios elementos del arreglo puede repetir, donde dice k=n en n tienes que poner cuantos valores quieres que nos devuelva 

random.sample(["Juan","Pedro","Maria","Ana"], k=2)= este codigo es el mismo de arriba solo que en vez que los valores se repitan aca no se repetiria seria uno por uno como sacar bolas de una bolsa de loteria

cartas=[1,2,3,4,5]

random.shuffle(cartas): Estoi  lo que hace es desordenar el arreglo


