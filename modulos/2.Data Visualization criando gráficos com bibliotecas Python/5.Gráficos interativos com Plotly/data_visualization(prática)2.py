import pandas as pd # Manipulação e análise de dados.

caminho_do_arquivo = r'D:/CURSOS ONLINE NUNCA APAGAR/CURSO CIENCIA DE DADOS ALURA NUNCA APAGAR/data-science/modulos/2.Data Visualization criando gráficos com bibliotecas Python/5.Gráficos interativos com Plotly/canadian_immegration_data.csv'

df = pd.read_csv(caminho_do_arquivo) # Lê o arquivo CSV.

df # Abre o data frame.

df.head() # Mostra as primeiras linhas do DataFrame.

# Renomeando os titulos das colunas 'nome_antigo' para 'nome_novo' (Para não ficar tudo em inglês e ficar facil de entender)
df = df.rename(columns={'Country' : 'País'})
df = df.rename(columns={'Continent' : 'Continente'})
df = df.rename(columns={'Region' : 'Região'})

# Muda o "Index" para "País"
df.set_index('País', inplace=True)
print(df)

# Váriavel para armazenar todo intervalo de tempo.

anos = list(map(str, range(1980, 2014)))
print(anos)

# Vamos pegar somente os dados do Brasil.
brasil = df.loc['Brazil', anos]

# Agora vamos criar um dicionário onde cada coluna vai ter um nome.
brasil_dict = {'ano': brasil.index. tolist(), 'imigrantes': brasil.values.tolist()}

# E agora criamos o dataframe de brasil com essas duas colunas, ano e imigrantes:
dados_brasil = pd.DataFrame(brasil_dict)
dados_brasil


import plotly.express as px # Cria gráficos interativos com poucas linhas de código.

fig = px.line(dados_brasil, # Data frame usado para criar o gráfico.
              x='ano', # Eixo "x" do gráfico.
              y='imigrantes', # Eixo "y" do gráfico.
              title='Imigração do Brasil para o Canadá no período de 1980 a 2013') # Cria o gráfico.

fig.update_traces(line_color='green', # Altera a cor da linha do gráfico.
                  line_width=4 # Altera a espessura da linha do gráfico.
                  )

fig.update_layout(width=1000, height=500,
                  xaxis={'tickangle':-45}, # Rotaciona os rótulos do eixo x em 45 graus.
                  font_family='Arial', # Define a família de fonte do gráfico.
                  font_size=14,
                  font_color='grey', # Define a cor do texto do gráfico.
                  title_font_color='black', # Define a cor do título do gráfico.
                  title_font_size=22, # Define o tamanho da fonte do título do gráfico.
                  xaxis_title='Ano', # Atualiza o título do eixo x.
                  yaxis_title='Número de imigrantes') # Atualiza o layout do gráfico.
fig.show() # Mostra o gráfico.

# Criando um dataframe só com os paises da AMERICA DO SUL!

america_do_sul = df.query('Região == "South America" ') # QUERY criada para puxar da coluna "Região" só os dados classificados como "South America" do dataframe principal para criar um data frame separado com esses dados chamado "america_do_sul".
america_do_sul # Testando se o dataframe foi criado com sucesso.

# Criando um dataframe mais "LIMPO" da America do Sul:

# Removendo as colunas 'Continente', 'Região' e 'Total' do DataFrame original 'america_do_sul'
# .drop() é usado para remover colunas ou linhas de um DataFrame.
# axis=1 indica que estamos removendo colunas (axis=0 seria para remover linhas).
df_america_do_sul_clean = america_do_sul.drop(['Continente', 'Região', 'Total'], axis=1)

# Transpondo o DataFrame 'df_america_do_sul_clean':
# .T é uma propriedade que faz a transposição de um DataFrame (linhas viram colunas e colunas viram linhas).
america_do_sul_final = df_america_do_sul_clean.T

# Agora 'america_do_sul_final' é o DataFrame transposto, com as colunas e linhas invertidas em relação ao original.

america_do_sul_final.head() # Testando se o dataframe foi criado com sucesso.

america_do_sul_final

fig = px.line(america_do_sul_final, # Data frame usado para criar o gráfico.
              x = america_do_sul_final.index,
              y = america_do_sul_final.columns,
              title = 'Imigração dos países da América do Sul para o Canadá no período de 1980 a 2013',
              markers=True # Adiciona marcadores às linhas do gráfico.
              ) # Cria o gráfico.

fig.update_layout(
          xaxis={'tickangle':-45, 'title': '', 'showticklabels': True }, # Rotaciona os rótulos do eixo x em 45 graus. # Remover o título do eixo sem esconder os valores
          xaxis_title='Ano', # Atualiza o título do eixo x.
          yaxis_title='Número de imigrantes', # Atualiza o título do eixo y.
          font_family='Arial', # Define a família de fonte do gráfico.
          font_size=14,
          font_color='grey', # Define a cor do texto do gráfico.
          )

fig.show() # Mostra o gráfico.

# Salvando o gráfico "LIMPO" da America do Sul em HTML:

fig.write_html('grafico_imigracao_america_do_sul.html')