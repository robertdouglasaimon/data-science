import pandas as pd

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
print(dados_brasil)
