#dicionário x conjunto x lista

dicionario = {}
print(dicionario)

dicionario[127] = "NeoCity"

dicionario = {"NCT":"NEO CITY TECNOLOGY", "NANA": "NA jaemin"}
print(dicionario["NCT"])

print(dicionario.get("NTX", "NÃO ENCONTRADO"))

dicionario["TXT"]="Tomorow X Together"

print(dicionario)

print(dicionario.pop("NANA"))
print(dicionario)

del dicionario["NCT"]
print(dicionario)

for chave in dicionario:
    print(chave)

for chave in dicionario.keys():
    print(chave)

for valor in dicionario.values():
    print(valor)

dicionario["TXT"]="Tomorow and Together"
print(dicionario)

for valor in dicionario.values():
  print(valor)

dicionario["RJ"] = "Rio de Janeiro"
dicionario["MG"] = "Minas Gerais"

for chave, valor in dicionario.items():
  print(chave, valor)

print()
for item in dicionario.items():
  print(item)

for indice, (chave, valor) in enumerate(dicionario.items(), start=1):
  print(indice, chave, valor)