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

# plt.show()

dados_brasil.describe() # Usamos o describe para visualizar no formato de tabela e comparar as informações dos dados do gráfico de Boxplot, para garantir a certeza dos dados, de que eles são iguais.

# print(dados_brasil.describe())

#---------------------------------------------------------------------------------------------------------------------------------------------#

# TENDENCIA DE IMIGRAÇÃO PARA OS PAISES DA AMERICA DO SUL ------------------------------------------------------#
fig, axs = plt.subplots(2, 2, figsize=(10,6))
fig.subplots_adjust(hspace=0.5, wspace=0.3) # Adiciona um espaço entre os gráficos. hspace=0.5: Controla o espaçamento horizontal. wspace=0.3: Controla o espaçamento vertical.
fig.suptitle('Imigração dos quatro maiores países da América do Sul para o Canadá \n De 1980 a 2013') # Adiciona um titulo geral para todos os gráficos.


axs[0,0].plot(df.loc['Brazil', anos]) # Chamou a tabela geral (df) ao invés de chamar várias variáveis guardando uma coluna especifica, ex: dados_brasil, dados_argentina, etc, etc. E com ".loc" ela chama a variáriavel que ela quer junto do atributo.
axs[0,0].set_title('Brazil')

axs[0,1].plot(df.loc['Colombia', anos])
axs[0,1].set_title('Colombia')

axs[1,0].plot(df.loc['Argentina', anos])
axs[1,0].set_title('Argentina')

axs[1,1].plot(df.loc['Peru', anos])
axs[1,1].set_title('Peru')

for ax in axs.flat: # Essa linha pega todos os subplots e faz com que o "loop" (repetição) percorra TODOS os subplots dessa estrutura.
    ax.xaxis.set_major_locator(plt.MultipleLocator(5)) # Essa linha seleciona o eixo X e faz a distruibuição da frequência de 5 em 5 nos dos valores do mesmo (X).

for ax in axs.flat: # Essa linha pega todos os subplots e faz com que o "loop" (repetição) percorra TODOS os subplots dessa estrutura.
  ax.set_xlabel('Ano') # Adiciona label em todos os gráficos
  ax.set_ylabel('Número de imigrantes') # Adiciona label em todos os gráficos
  ax.grid(True) # Adiciona tela ao gráfico.
  
#-----------------------------------------------------------------------------------------------------------------------#
# Comando criado para evitar descrepancia nos valores dos eixos Y de cada gráfico, e ajuda também na comparação mais precisa dos dados.
# Essa dica é sempre boa de se manter e usar!

ymin = 0 # Determina o valor minimo do eixo Y
ymax = 6000 # Determina o valor maximo do eixo Y
for ax in axs.ravel(): # Essa linha pega todos os subplots e faz com que o "loop" (repetição) percorra TODOS os subplots dessa estrutura.
    ax.set_ylim(ymin, ymax)
    
# plt.show()    
#-----------------------------------------------------------------------------------------------------------------------#


#-Gráfico de Barras Horizontal com Destaque Colorido--------------------------------------------------------------------#

# Criando um novo DATAFRAME só com os paises da America do Sul para criar o gráfico
america_do_sul = df.query('Região == "South America"')
america_do_sul

# Ordena o DataFrame 'america_do_sul' em ordem crescente com base na coluna 'Total'.
# 'by' especifica a coluna usada para a ordenação ('Total'), e 'ascending=True' indica que a ordenação deve ser em ordem crescente.
# O resultado da ordenação é armazenado em 'america_do_sul_sorted'.
america_do_sul_sorted = america_do_sul.sort_values(by='Total', ascending=True)

# Inicializa uma lista vazia chamada 'cores' para armazenar as cores que serão usadas no gráfico de barras.
cores = []

# Itera sobre os índices do DataFrame 'america_do_sul_sorted'.
for pais in america_do_sul_sorted.index:
    # Verifica se o país é 'Brazil'. Se for, adiciona 'green' (verde) à lista de cores.
    if pais == 'Brazil':
        cores.append('green')
    # Se não for 'Brazil', adiciona 'silver' (prata) à lista de cores.
    else:
        cores.append('silver')

# Cria uma figura e um conjunto de eixos para o gráfico de barras horizontais.
# 'figsize' define o tamanho da figura (12 de largura por 5 de altura).
fig, ax = plt.subplots(figsize=(12, 5))

# Cria um gráfico de barras horizontal ('barh'), utilizando o índice de 'america_do_sul_sorted' como rótulos (nomes dos países)
# e a coluna 'Total' como os valores das barras. A cor de cada barra é definida pela lista 'cores'.
ax.barh(america_do_sul_sorted.index, america_do_sul_sorted['Total'], color=cores)

# Define o título do gráfico. 'loc' especifica a localização do título à esquerda e 'fontsize' define o tamanho da fonte.
ax.set_title('América do Sul: Brasil foi o quarto país com mais imigrantes \n para o Canadá no perído de 1980 a 2013', loc='left', fontsize=18)

# Define o rótulo do eixo x com o texto 'Número de imigrantes' e o tamanho da fonte.
ax.set_xlabel('Número de imigrantes', fontsize=14)

# Remove o rótulo do eixo y, mantendo-o vazio.
ax.set_ylabel('')

# Define o tamanho da fonte dos rótulos do eixo y.
ax.yaxis.set_tick_params(labelsize=12)

# Define o tamanho da fonte dos rótulos do eixo x.
ax.xaxis.set_tick_params(labelsize=12)




#----Esse "for" adiciona os valores numéricos ao lado de cada barra do gráfico de barras horizontal.---
# Mas vamos destrinchar tudo:

# 'enumerate' percorre a lista de valores da coluna 'Total' do DataFrame 'america_do_sul_sorted', 
# retornando o índice (i) e o valor (v) de cada item.
for i, v in enumerate(america_do_sul_sorted['Total']):

    # Usa o método 'ax.text' para adicionar o texto com o valor (v) ao lado de cada barra.
    # 'v + 20' determina a posição horizontal do texto, ligeiramente à direita da extremidade da barra.
    # 'i' define a posição vertical do texto, correspondente ao índice de cada barra.
    # 'str(v)' converte o valor numérico para string para exibição.
    # 'color' define a cor do texto (preto neste caso).
    # 'fontsize' define o tamanho da fonte do texto.
    # 'ha' (horizontal alignment) alinha o texto à esquerda ('left') da posição especificada.
    # 'va' (vertical alignment) alinha o texto ao centro ('center') da posição vertical da barra.
    ax.text(v + 20, i, str(v), color='black', fontsize=10, ha='left', va='center')

# Então o código limpo do "for" para adicionar valores numéricos ao lado de cada barra do gráfico fica assim:
for i, v in enumerate(america_do_sul_sorted['Total']):
  ax.text(v + 20, i, str(v), color='black', fontsize=10, ha='left', va='center')
  
  

# Exibe o gráfico.
plt.show()

#-----------------------------------------------------------------------------------------------------------------------#



# ESTUDO DA BIBLIOTECA SEABORN -------------------------------------------------------------------------------------------------------------#

import seaborn as sns

sns.set_theme() # Define o tema padrão do Seaborn

top_10 = df.sort_values('Total', ascending=False).head(10) # Ordena o DataFrame 'df' em ordem decrescente com base na coluna 'Total' e seleciona as primeiras 10 linhas.

print(top_10)

