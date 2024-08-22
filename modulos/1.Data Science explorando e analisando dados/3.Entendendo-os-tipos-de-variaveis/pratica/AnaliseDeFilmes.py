import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

planilha_de_filmes = r"D:\CURSOS ONLINE NUNCA APAGAR\CURSO CIENCIA DE DADOS ALURA NUNCA APAGAR\data-science\modulos\1.Data Science explorando e analisando dados\3.Entendendo-os-tipos-de-variaveis\pratica\bases de dados\tmdb_5000_movies.csv"

tmdb = pd.read_csv(planilha_de_filmes)
tmdb.head()
print(tmdb.head())

# Prompt: Gráfico de distribuição da receita dos filmes (revenue)
sns.displot(tmdb["revenue"])
plt.title('Distribuição da receita dos filmes')
plt.xlabel('Escala de valores (10 elevado a 9º) em bilhão')
plt.show()

# Prompt: Gráfico de distribuição do orçamento dos filmes (budget)
sns.displot(tmdb["budget"])
plt.title('Distribuição do orçamento dos filmes')
plt.xlabel('Escala de valores (10 elevado a 9º) em bilhão')
plt.show()

tmdb.info()

tmdb.describe()

tmdb.query('revenue < 500')
print(tmdb.query('revenue < 500'))
