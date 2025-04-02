import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Carregar os dados do arquivo CSV
file_path = "titanic_data.csv"
data = pd.read_csv(file_path)

# Criar o gráfico de pares (pairplot)
plt.figure(figsize=(8, 6))
pairplot = sns.pairplot(data, hue="survived", diag_kind="kde", palette="husl")

# Exibir o gráfico
plt.show()
 
 #gráfico 2
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados do arquivo CSV
df = pd.read_csv("desempenho_alunos.csv")

# Exibir as primeiras linhas do DataFrame
print(df.head())

# Criar o gráfico de pares
sns.pairplot(df, hue="Aluno", diag_kind="kde")
plt.suptitle("Gráfico de Pares: Desempenho dos Alunos", y=1.02)
plt.show()
#grafico3
