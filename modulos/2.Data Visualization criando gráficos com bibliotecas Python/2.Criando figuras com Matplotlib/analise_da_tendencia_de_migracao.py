import pandas as pd
import matplotlib.pyplot as plt

caminho_arquivo_local = r'D:/CURSOS ONLINE NUNCA APAGAR/CURSO CIENCIA DE DADOS ALURA NUNCA APAGAR/data-science/modulos/2.Data Visualization criando gráficos com bibliotecas Python/1.Conhecendo a biblioteca Matplotlib/canadian_immegration_data.csv'

df = pd.read_csv(caminho_arquivo_local)
# print(df)

df.info() # Para obter informações mais detalhadas do banco de dados (planilha).
# print(df.info())

#--------- 1º Tarefa do projeto: Analisar as tendências de imigração do Brasil em um determinado período.------ #

# Renomeando os titulos das colunas 'nome_antigo' para 'nome_novo' (Para não ficar tudo em inglês e ficar facil de entender)
df = df.rename(columns={'Country' : 'País'})
df = df.rename(columns={'Continent' : 'Continente'})
df = df.rename(columns={'Region' : 'Região'})

# Seta o "Index" para ser o "País"
df.set_index('País', inplace=True)
# print(df)

# Váriavel para armazenar todo intervalo de tempo.
anos = list(map(str, range(1980, 2014)))
# print(anos)

# Vamos pegar somente os dados do Brasil.
brasil = df.loc['Brazil', anos]
# print(brasil)

# Agora vamos criar um dicionário onde cada coluna vai ter um nome.
brasil_dict = {'ano': brasil.index. tolist(), 'imigrantes': brasil.values.tolist()}

# E agora criamos o dataframe com essas duas colunas, ano e imigrantes:
dados_brasil = pd.DataFrame(brasil_dict)
# print(dados_brasil)

# Criando o gráfico de plot dos dados mineirados da tabela.
plt.figure(figsize=(10, 5)) # Modifica o tamanho do gráfico baseado nos parametros dentro dos parenteses. Nesse caso aqui "figsize=(10, 5)". Sendo 10 largura e 5 altura (Em polegadas).
plt.plot(dados_brasil['ano'], dados_brasil['imigrantes'])
plt.xticks(['1980', '1985', '1990', '1995', '2000', '2005', '2010']) # Setando para exibir de 5 em 5 anos para melhorar a vizualização no eixo X.
# plt.yticks([500, 1000, 1500, 2000, 2500, 3000]) # Setando para exibir apenas os valores que eu escolher no eixo Y.
plt.title('Gráfico de Imigrantes do Brasil para o Canadá') # Titulo do gráfico.
plt.xlabel('Ano') # Váriável Independente - Não precisa de nada para se manter no gráfico.
plt.ylabel('Número de imigrantes') # Variável Dependente - Varia de acordo com o ano (Valores sobem e descem de acordo com as mudanças nos anos)
# plt.show()

#MONTANDO UM GRÁFICO EM FIGURA----------------------------------------------------------------------------------#

fig, ax = plt.subplots(figsize=(8,4)) # Explicando essa linha: Duas váriaveis estão sendo usadas para receber o plt, que são fig (figura) e ax (Os eixos do gráfico).
ax.plot(dados_brasil['ano'], dados_brasil['imigrantes']) # Nessa estrutura, como "ax" foi declarado em cima, e está recebendo os valores, só precisamos dentro dos parenteses indicar que é o eixo "X" e quem é o eixo "Y". Logo, dados_brasil['ano'] será o eixo "X" e dados_brasil['imigrantes'] será o eixo "Y".
ax.set_title('Gráfico de Imigrantes do Brasil para o Canadá \n 1980 a 2013') # Titulo do gráfico. O atributo "\n" é usado sempre que queremos ir para a próxima linha, ele lembra muito o <br> do HTML/JS/JSX.
ax.set_xlabel('Ano') # Váriável Independente - Não precisa de nada para se manter no gráfico.
ax.set_ylabel('Número de imigrantes') # Variável Dependente - Varia de acordo com o ano (Valores sobem e descem de acordo com as mudanças nos anos).
ax.xaxis.set_major_locator(plt.MultipleLocator(5)) # Modifica apenas o eixo "X" e faz o espalhamento dos dados/a frequencia baseado no numero entre os pareteses interno, nesse caso o número 5. Logo, eixo "X" vai mostrar os dados de 5 em 5 anos.                                                   
plt.show()

#----------------------------------------------------------------------------------------------------------------#

#-CRIANDO VÁRIOS GRÁFICOS NA MESMA LINHA-------------------------------------------------------------------------#
fig, axs = plt.subplots(1, 2, figsize=(15,5)) # Segue quase a mesma estrutura do gráfico anterior, só que tem como diferencial colocar "ax" no plural, pois será mais de um gráfico, logo "axs" e aqui como você fará 2 gráficos, antes de chamar o "figsize=(x,y)" para determinar o tamanho do gráfico, você precisa especificar quantas linhas vai precisar para criar os gráficos.

# Vamos criar os dois gráficos subplot! O primeiro vai ser um gráfico de linhas e o segundo um boxplot.
# Como dito anteriormente, serão dois gráficos, então para diferenciarmos quem é quem, usamos um "INDEX" para saber qual a posição e numeração de cada um. Então, após a váriavel "axs" adicionamos o index, ficando assim: "axs[0]", lembrando que o index sempre começará do zero. Vamos ver o exemplo completo abaixo:

# Gráfico 1 - Gráfico de linhas.
axs[0].plot(dados_brasil['ano'], dados_brasil['imigrantes']) 
axs[0].set_title('Imigração do Brasil para o Canadá \n 1980 a 2013')
axs[0].set_xlabel('Ano')
axs[0].set_ylabel('Número de imigrantes')
axs[0].xaxis.set_major_locator(plt.MultipleLocator(5))
axs[0].grid(True) # Adiciona uma grade no gráfico.

# Gráfico 2 - Boxplot
axs[1].boxplot(dados_brasil['imigrantes'])
axs[1].set_title('Boxplot da Imigração do Brasil para o Canadá \n 1980 a 2013')
axs[1].set_xlabel('Brasil')
axs[1].set_ylabel('Número de imigrantes')
axs[1].grid(True) # Adiciona uma grade no gráfico.

plt.show()

dados_brasil.describe() # Usamos o describe para visualizar no formato de tabela e comparar as informações dos dados do gráfico de Boxplot, para garantir a certeza dos dados, de que eles são iguais.
print(dados_brasil.describe())
#----------------------------------------------------------------------------------------------------------------#
