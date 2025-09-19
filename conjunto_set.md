````python
# Entendendo o funcionamento de dados set.

Um set é uma coleção que não possui objetos repetidos, usamos sets para representar conjuntos matemátios ou eliminar itens duplicados de um iterável. 


set([1, 2, 3, 1, 3, 4])

set("abacaxi")

set(("palio", "gol", "celta", "palio"))

# conjuntos em python não suportam indexação e nem fatiamento, para acessar seus valores, é prciso converter o conjunto para lista. 


numeros = {1, 2, 3, 2}

numeros = list(numeros)

numeros[0]

#iterando conjuntos com for
carros = {"gol", "celta", "palio"}

for carro in carros:
  print(carro)

#função enumerate
Para saber o índice do objeto dentro do laço for, podemos usar a função enumerate

carros = {"gol", "celta", "palio"}
for indice, carro in enumerate(carros):
  print(f"{indice}: {carro)"}

#métodos de classe

{}.union

conjunto_a = {1, 2}
comjunto_b = {3, 4}

conjunto_a.union(conjunto_b)


{}.intersection

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto _a.intersection(conjunto_b)

{}.difference

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.difference(conjunto_b)
conjunto_b.difference(conjunto_a)

{}.symmetric_difference

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.symmetric_difference(conjunto_b)

{}.issubset

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issubset(conjunto_b)
conjunto_b.issubset(conjunto_a)


{}.issuperset

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issuperset(conjunto_b)
conjunto_b.issuperset(conjunto_a)

{}.isdisjoint

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

conjunto_a.isdisjoint(conjunto_b)
conjunto_a.isdisjoint(conjunto_c)


{}.add

sorteio = {1, 23}

sorteio.add(25)
sorteio.add(42)
sorteio.add(25)

{}.clear

sorteio = {1, 23}

sorteio 
sorteio.clear()
sorteio

{}.copy

sorteio = {1, 25}
sorteio.copy()
sorteio

{}.discard
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros
numeros.discard(1)
numeros.discard(45)
numeros

{}.pop

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
numeros
numeros.pop()
numeros.pop()
numeros


{}.remove

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
numeros
numeros.remove()
numeros


len

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
len(numeros)


in

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

1 in numeros
10 in numeros





´´´







