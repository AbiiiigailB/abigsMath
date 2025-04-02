#estrutura de dados: lista, tuplas, conjuntos de dicionários

r = range(1, 9)
print(r)

for intem in r:
    print(intem)

lista = list(r)
print(lista)

tupla = tuple(r)
print(tupla)

conjunto = set(r)
print(conjunto)

conjunto.add(9)
# dicionario = dict(r)
# print(dicionario)

lista = []
lista = list()

lista = ["Ana", "Paula", "Sofia"]
#lista = list("Ana", "Paula", "Sofia")

tupla = ()
tupla = tuple()

conjunto = {}
conjunto = set()

dicionario = {"SP":"São Paulo", "RJ":"Rio", "MG":"Minas"}

print(lista[1])
print(dicionario["SP"])

dicionario = {55:"Abgail", 19:"Ines"}
print(dicionario[55])
