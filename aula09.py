import numpy as np
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression

#dadinhos exemplares
preco = np.array([10, 15, 20, 25, 30, 35, 40])
venda = np.array([100, 90, 80, 60, 50, 30, 20])

preco = preco.resharpe(-1, 1)


modelo = LinearRegression()
modelo.fit(preco, venda)

previsao = modelo.predict(preco)

#vizualização gradica ai toma
plt.scatter(preco, venda, color="blue", label="dados reais")
plt.plot(preco, previsao, color="red", linewidth=2, label="modelo linear")
plt.title("relação entre preço e vendas")
plt.xlabel("preço do produto")
plt.ylabel("vendas mensais")
plt.legend()
plt.grid(True)
plt.show()
