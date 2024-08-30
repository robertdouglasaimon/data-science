import pandas as pd
import matplotlib.pyplot as plt

caminho_arquivo_local = r'D:/CURSOS ONLINE NUNCA APAGAR/CURSO CIENCIA DE DADOS ALURA NUNCA APAGAR/data-science/modulos/2.Data Visualization criando gráficos com bibliotecas Python/1.Conhecendo a biblioteca Matplotlib/desafio/canadian_immegration_data.csv'

df = pd.read_csv(caminho_arquivo_local)
# df.info()
# print(df.info())


df = df.rename(columns={'Country' : 'País'})
df = df.rename(columns={'Continent' : 'Continente'})
df = df.rename(columns={'Region' : 'Região'})

df.set_index('País', inplace=True)
# print(df)


# Váriavel para armazenar todo intervalo de tempo.
anos = list(map(str, range(1980, 2014)))
# print(anos)


# Vamos pegar dados do Brasil e Argentina.
brasil = df.loc['Brazil', anos]
argentina = df.loc['Argentina', anos]
# print(brasil, argentina)

# Agora vamos criar um dicionário onde cada coluna vai ter um nome.
brasil_dict = {'ano': brasil.index.tolist(), 'imigrantes': brasil.values.tolist()}
argentina_dict = {'ano': argentina.index.tolist(), 'imigrantes': argentina.values.tolist()}

# Gráfico com os dois paises destintamente destacados para comparação dos dados.
plt.figure(figsize=(10,5))
plt.plot(brasil_dict['ano'], brasil_dict['imigrantes'], label='Brasil')
plt.plot(argentina_dict['ano'], argentina_dict['imigrantes'], label='Argentina')
plt.xticks(['1980', '1985', '1990', '1995', '2000', '2005', '2010', '2013'])
plt.xlabel('Ano')
plt.ylabel('Número de imigrantes')
plt.title('Gráfico de Imigrantes do Brasil e Argentina para o Canadá')
plt.legend() # plt.legend() - Serve para ativar as label inseridas nos "plt.plot" e renderiza-lás no gráfico.
plt.show()

# FIM da atividade!