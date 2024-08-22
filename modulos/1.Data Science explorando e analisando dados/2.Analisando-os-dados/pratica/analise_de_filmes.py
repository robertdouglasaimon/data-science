import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from analise_de_notas import notas

filmes = pd.read_csv("https://raw.githubusercontent.com/alura-cursos/data-science-analise-exploratoria/main/Aula_0/ml-latest-small/movies.csv")
filmes.columns = ["filmeId", "titulo", "generos"]
filmes.head()

# Desta base, vamos nos concentrar na análise dos 2 primeiros filmes “Toy Story” e “Jumanji” chamando-os por meio de seus IDs na base notas que criamos na aula anterior. Para isso, vamos ler a média das notas de cada um dos 2 filmes utilizando o método query():

notas.query("filmeId==1")["nota"].mean()
notas.query("filmeId==2")["nota"].mean()
print( 
      notas.query("filmeId==1")["nota"].mean(),
      notas.query("filmeId==2")["nota"].mean()
    )
# Resultado: 3.9209302325581397 / 3.4318181818181817


# Agora, vamos calcular média de todos filmes individualmente, agrupando-os por meio do método groupby() e utilizando como fórmula de agregação de dados o mean():

media_por_filme = notas.groupby('filmeId')['nota'].mean() # Agrupa as notas por filmeID e calcula a média das notas.
media_por_filme.head() # Mostra as 5 primeiras linhas da tabela de dados.
print(media_por_filme.head())

# Resposta/Resultado: ↓
# filmeId (Olhar no terminal o resultado)
# 1    3.920930
# 2    3.431818
# 3    3.259615
# 4    2.357143
# 5    3.071429

#-----------------------------------------------------------------------------------------------------------------#

# Vamos observar agora a distribuição das médias por filme? Criaremos um histograma e um boxplot, separadamente para esse processo:

media_por_filme.plot(kind="hist")
plt.title('Distribuição das Médias por Filme')
plt.show()

# Resposta/Resultado:
# Histograma personalizado e criado com seaborn e boxplot:

# plt.figure(figsize=(10, 6)): Comando para gerar um gráfico com tamanho especifico. Nesse caso especificamos dentro dos parenteses que: 
    # figsize: Comando que vai determinar o tamanho do gráfico em largura e polegaas.
    # (10, 6): Aqui temos os valores 10 e 6. Sendo 10 a LARGURA e 6 as polegadas.

# Com Seaborn o histograma deve ser chamado após a sigla da biblioteca('histplot'), e dentro dos parenteses deve ir a váriavel que recebe os dados mais os parametros do gráfico.

# Se você tem um conjunto de dados que varia de 0 a 100, e define bins=50, o Seaborn criará 50 intervalos de igual largura para cobrir todo o intervalo de dados. Cada intervalo teria 2 unidades de largura (porque 100/50 = 2).
# Isso significa que a primeira barra (ou bin) contará quantos valores estão entre 0 e 2, a segunda barra entre 2 e 4, e assim por diante.

# kde=True: Adiciona uma estimativa de densidade de Kernel (KDE) ao histograma, que é uma curva suave representando a densidade de probabilidade dos dados. Isso ajuda a visualizar a distribuição subjacente dos dados de forma contínua.

# O plt.title, xlabel, ylabel e show são auto explicativos! Mas para caso de duvida: title colocar um titulo no gráfico, x e ylabel são os eixos do gráfico e dentro dos parenteses você pode dar descrição para esses eixos. O show mostra o gráfico (Não usamos print para mostrar gráficos!).

# Na prática, tudo que eu disse acima fica assim:
plt.figure(figsize=(10, 6))
sns.histplot(media_por_filme, bins=50, kde=True)
plt.title('Distribuição das Médias por Filme')
plt.xlabel('Média das Notas')
plt.ylabel('Frequência')
plt.show()

#------------------------------------------------------------------------------------------------------------------#

# Por fim, para conseguirmos observar os dados que o boxplot apresenta, vamos ler o resumo dos dados com o describe().
# Resposta/Resultado:
media_por_filme.describe()
print(media_por_filme)