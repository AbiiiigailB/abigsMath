#dados do produto
produto = {
    "nome": "smartphone x200",
    "preco": 1999.99,
    "quantidade_estoque": 50.00,
    "avaliacao_clientes": 4.7,
    "numero_avaliacoes": 345,
    "caracteristicas": ["64GB", "12MP", "4000MAh"],
    "disponivel": True
}

#função para identificar o tipo de dado
def identificar_tipo_dado(valor):
    if isinstance(valor, str):
        return "dado qualitativo(string)"
    elif isinstance(valor, (int, float)):
        return "dado quantitativo (numero)"
    elif isinstance(valor, list):
        return "dado qualitativo (lista de strings)"
    elif isinstance(valor, bool):
        return "dado qualitativo (booleano)"
    else:
        return "tipo de dado desconhecido"

    #exibir dados do seu tipo
for chave, valor in produto.items():
    tipo = identificar_tipo_de_dado(valor)
    print(f"{chave}: {valor}-> {tipo}")