import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
horarios=["06h", "09h", "12h", "15h", "18h", "21h"]
cidades=["Cidade A", "Cidade B", "Cidade C"]
temperaturas = np.array([
[15, 18, 25, 30, 27, 20], # Cidade A
[12, 17, 24, 29, 25, 18], # Cidade B
[10, 14, 22, 26, 23, 16] # Cidade C
])
plt.figure(figsize=(8, 5))
sns.heatmap(temperaturas, annot=True, cmap="coolwarm",
xticklabels=horarios, yticklabels=cidades)
plt.title("Temperatura ao Longo do Dia&quot")
plt.xlabel("Horários&quot")
plt.ylabel("Cidades&quot")
plt.savefig("heatmap_temperatura.tiff&quot", format="tiff&quot", dpi=300)
plt.show()
 
#exemplo 4 
# Criando matriz de correlação fictícia para as notas
notas_corr = np.array([
[1.00, 0.60, 0.45, 0.30, 0.50],
[0.60, 1.00, 0.55, 0.25, 0.65],
[0.45, 0.55, 1.00, 0.40, 0.60],
[0.30, 0.25, 0.40, 1.00, 0.35],
[0.50, 0.65, 0.60, 0.35, 1.00]
])

materias = ["Matemática", "Física", "Química", "História", "Português"]

plt.figure(figsize=(7,6))
sns.heatmap(notas_corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1,
linewidths=0.5, fmt=".2f",
xticklabels=materias, yticklabels=materias)

plt.title("Correlação entre Notas de Alunos")
plt.savefig("heatmap_correlação_notas.tiff", format="tiff", dpi=300)
plt.show()
