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

#----------------------------------------------------------------------------------------------------------------#
# Filtrando a coluna "original_language" para saber qual foi a linguagem mais usada em todos os titulos

tmdb["original_language"].unique() # Puxa os valores ÚNICOS da tabela, nesse caso vai puxar todas as linguagens, no que diz respeito as linguagens usadas e não na quantidade.
print(tmdb["original_language"].unique()) 

tmdb["original_language"].value_counts() # Aqui sim, puxa os VALORES usados nas respectivas linguagens para à análise de qual linguagem foi mais usada.
print(tmdb["original_language"].value_counts())

#--DAQUI PARA BAIXO FILTRAMOS PARA TER O VALOR EXATO DA QUANTIDADE DE LINGUAGENS --#

contagem_de_lingua = tmdb["original_language"].value_counts().to_frame().reset_index() 
# .to_frame(): Transforma toda a coluna em uma tabela/data frame para ficar melhor de analisar. 
#.reset_index(): Cria uma nova coluna na tabela para adicionar ID's únicos para cada linha da tabela.

contagem_de_lingua.columns = ["original_language","total"]
# Modifica o nome dos titulos da tabela que criamos acima.

contagem_de_lingua.head()
#Trás as 5 primeiras linhas da tabela.
print(contagem_de_lingua.head())

sns.barplot(data =  contagem_de_lingua, x='original_language', y='total')
plt.show()
# Esse comando, gera um gráfico de plot das modificações acima que fizemos.

sns.countplot(data = tmdb, x='original_language')
plt.show()
# Exemplo de gráfico pego na documentação que pega o dataframe inteiro (tmdb) e já faz a contagem das linguagens e distribui elas visualmente no grafico para melhor analise.

# -------------------------------------------------------------------------------------------------------------#

total_por_lingua = tmdb["original_language"].value_counts()
# Valor total de todas as linguas

total_geral = total_por_lingua.sum() # <- TOTAL DE FILMES
# A linha acima está dizendo que: total_geral é a soma de todos os valores de total_por_lingua.

total_de_ingles = total_por_lingua.loc['en'] # <- TOTAL DE FILMES EM INGLES.
# A linha acima está dizendo que: total_de_ingles é tudo que total_por_lingua.loc['en'] achar de eng.
#.loc['en']: Localiza qual atributo queremos separar dos demais. Que nesse caso aqui é só a linguagem 'en'.

total_do_resto = total_geral - total_de_ingles #<- RESTO.
print(total_geral, total_de_ingles, total_do_resto)


# Criando um objeto com as váriaveis criadas acima chamado de "dados" para poder gerar um DataFrame mostrando todos os resultados.
dados = {
    "lingua" : ['ingles', 'outros'],
    "total" : [total_de_ingles, total_do_resto]
}

dados = pd.DataFrame(dados)
dados
print(dados)

sns.barplot(data= dados, x='lingua', y= 'total')
plt.show()

#------------------------------------------------------------------------------------------------------------ # 

total_de_outros_filmes_por_lingua = tmdb.query("original_language != 'en' ")["original_language"].value_counts()
total_de_outros_filmes_por_lingua.head()

plt.figure(figsize=(16, 8)) # Configura o tamanho do gráfico, mais informações na documentação do matplotlib.
sns.countplot(data = 
    tmdb.query("original_language != 'en' "), 
    order = total_de_outros_filmes_por_lingua.index, # Ordena os dados (Do maior para o menor, ordem alfabetica, enfim.. Aqui a gente ordena como quiser, basta ver na documentação o "incremento de ordenação" após o "order", como nesse caso só queremos ordenar a quantidade, não precisou incremento.)
    palette ="mako", # Paleta de cores usada para pintar as barras do gráfico. Também encontrado na documentação do seaborn, sempre que precisar olhar lá no site.
    hue ="original_language", # Ativa a paleta de cores no gráfico, mas de forma solida e padrão, como vem na paleta.
    hue_order = total_de_outros_filmes_por_lingua.index, # Ordena os dados pelas cores, sendo o mais claro a menor quantidade e as cores mais escuras as quantidades maiores.
    stat="percent", # Exibe os dados por porcentagem, outros formatos também podem ser encontrados na documentação do seaborn.
    x = "original_language") # Legenda do eixo horizontal do gráfico.

plt.title('Distribuição da língua original nos filmes exceto em inglês')    
plt.show()

total_de_outros_filmes_por_lingua = tmdb.query("original_language != 'en' ")["original_language"].value_counts(normalize=True)
total_de_outros_filmes_por_lingua.head()
