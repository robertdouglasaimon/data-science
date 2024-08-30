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
plt.show()
