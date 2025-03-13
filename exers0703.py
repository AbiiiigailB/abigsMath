#1. adicione o número 50 no fim da lista.*

lista_numero = [10, 20, 30, 40]
lista_numero.insert(4, 50)
print(lista_numero)

#2. adicione "laranja" ao indice 1 da lista.*
lista_frutas = ["maçã", "banana", "uva"]
lista_frutas.insert(1, "laranja")
print(lista_frutas)

#3. remova "cachorro" da lista.*
lista_animais = ["cachorro", "gato", "pássaro", "cachorro"]
lista_animais.remove("cachorro")
print(lista_animais)

#4. remova o elemento de indice 2 da lista e mostre o elemento removido.*-
lista_nomes = ["alice", "bob", "charlie", "david"]
print(lista_nomes.pop(2))
print(lista_nomes)

# 5. Encontre o índice da primeira ocorrência de ‘azul’ na lista.-*
lista_cores = ['vermelho', 'azul', 'verde', 'amarelo', 'azul']
print(lista_cores.index("azul"))

# 6. Conte quantas vezes o número 2 aparece na lista.-*
lista_numeros_repetidos = [1, 2, 3, 2, 4, 2, 5, 2]
print(len(lista_numeros_repetidos))
quantidade = lista_numeros_repetidos.count(2)
print("o número 2 aparece", quantidade, "vezes na lista")

# 7. Ordene a lista em ordem crescente.*
lista_desordenada = [50, 20, 80, 10, 40]
lista_desordenada.sort()
print(lista_desordenada)

# 8. Inverta a ordem dos elementos da lista.*
lista_invertida = ['maçã', 'banana', 'laranja', 'uva']
lista_invertida.reverse()
print(lista_invertida)

# 9. Crie uma cópia profunda da lista.*
original = [1, 2, 3, 4, 5]
copia = original[:]
print(copia)
print(original)

# 10. Dada a lista:*
lista_numerica = [15, 8, 22, 3, 10]

# a) Mostre o tamanho da lista.*
print((len(lista_numerica)))
# b) Mostre o maior valor da lista.*
print(max(lista_numerica))
# c) Mostre o menor valor da lista.*
print(min(lista_numerica))
# d) Mostre a soma de todos os elementos da lista*
print(sum(lista_numerica))