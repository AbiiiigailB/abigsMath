import matplotlib.pyplot as plt
import numpy as np
dias = np.arange(1, 31)
temperaturas = [22 + 2 * np.sin(dia * 2 * np.pi / 30) + np.random.normal(0, 1) for
dia in dias]
plt.figure(figsize=(10, 6))
plt.plot(dias, temperaturas, marker="o", color="b", linestyle="-", linewidth=2,
markersize=6)
plt.title("Variação de Temperatura Média Diária ao Longo de um Mês",
fontsize=14)
plt.xlabel("Dia do Mês", fontsize=12)
plt.ylabel("Temperatura (°C)", fontsize=12)
plt.grid(True)
plt.savefig("serie_temporal_temperatura.tiff", format="tiff")
plt.show()