import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from analise_de_notas import notas

local_arquivo = r'D:/CURSOS ONLINE NUNCA APAGAR/CURSO CIENCIA DE DADOS ALURA NUNCA APAGAR/data-science/modulos/1.Data Science explorando e analisando dados/2.Analisando-os-dados/pratica/bases de dados/movies.csv'
filmes = pd.read_csv(local_arquivo)
filmes.head()

# filmes = pd.read_csv('https://raw.githubusercontent.com/alura-cursos/data-science-analise-exploratoria/main/Aula_0/ml-latest-small/movies.csv')
# filmes.columns = ["filmeId", "titulo", "generos"]
# filmes.head()

notas.head()

notas.query('filmeId==2')['nota'].mean()

medias_por_filme = notas.groupby('filmeId')['nota'].mean()
medias_por_filme.head()

medias_por_filme.plot(kind='hist')
plt.show()