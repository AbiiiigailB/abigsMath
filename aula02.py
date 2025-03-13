# dados quantitativos vendas semanais
vendas_semanais = [150, 200, 250, 300, 350, 400]

#dadps qualitativos: feedback dos clientes
feedbacks = [
    "produto facil de usar, mas caro"
    "otimo produto"
    "muito satisfeito com a qualidade"
]

#analisando os dados quantitativos:crescimento de vendas
crescimento = [(vendas_semanais[i] - vendas_semanais[i-1]) / 
vendas_semanais]