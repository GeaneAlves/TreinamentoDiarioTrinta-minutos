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

for indice = {"gol", "celta", "palio"}
for indice, carro in enumerate(carros):
  print(f"{indice}: {carro)"}

#métodos de classe 







