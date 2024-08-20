import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from analise_de_notas import notas

# Carregar o dataset dos filmes
filmes = pd.read_csv('https://raw.githubusercontent.com/alura-cursos/data-science-analise-exploratoria/main/Aula_0/ml-latest-small/movies.csv')
filmes.columns = ["filmeId", "titulo", "generos"]

# Calcular a média das notas por filme
medias_por_filme = notas.groupby('filmeId')['nota'].mean()

# Exibir as primeiras linhas das médias
print(medias_por_filme.head())

# Opcional: Criar um gráfico das médias
plt.figure(figsize=(10, 6))
sns.histplot(medias_por_filme, bins=50, kde=True)
plt.title('Distribuição das Médias por Filme')
plt.xlabel('Média das Notas')
plt.ylabel('Frequência')
plt.show()
