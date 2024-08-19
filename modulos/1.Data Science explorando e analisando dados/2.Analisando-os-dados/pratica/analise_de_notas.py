import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Carregar o dataset online
notas = pd.read_csv('https://raw.githubusercontent.com/alura-cursos/data-science-analise-exploratoria/main/Aula_0/ml-latest-small/ratings.csv')

# ou

# Carrega o dataset local, no meu caso, esse csv tá dentro da pasta do projeto, chama-se ''rating.csv'

# Primeiro você atribui uma variável ao arquivos:
caminho_arquivo_local = r'D:/CURSOS ONLINE NUNCA APAGAR/CURSO CIENCIA DE DADOS ALURA NUNCA APAGAR/data-science/modulos/1.Data Science explorando e analisando dados/1.Conhecendo-dados/pratica/bases de dados/ratings.csv'

# e depois carrega ele usando o paramentro de leitura:
notas = pd.read_csv(caminho_arquivo_local)

# Exibir o DataFrame
notas

notas.columns = ["usuarioId", "filmeId", "nota", "momento"]
notas.head()

notas['nota'].unique()

notas['nota'].value_counts()

notas['nota'].mean()



# notas['nota'].plot(kind='hist')
# plt.show()  # <-- Isso vai exibir o gráfico do comando "notas['nota'].plot(kind='hist')". Mas cheque se a biblioteca foi importada lá no topo corretamente, caso contrário não funcionará. 
# Exemplo de como deve estar corretamente importado: import matplotlib.pyplot as plt


notas['nota'].median() #Tira a média (O meio EXATO do valor da coluna selecionada para analisar) exata do valor da tabela. 

#Usando template string no Python para chamar a Média(.mean()) e a Médiana (.median()) da coluna "nota":
mediana = notas ['nota'].median()
media = notas ['nota'].mean()
print(f'A mediana é {mediana} e a média é {media}')

notas['nota'].describe() # Pede para o Python descreve a coluna selecionada 'nota' no minimos detalhes.
print(notas['nota'].describe())


# Biblioteca e graficos que mostram visualmente como está distribuido esse valor. Como ver a mediana visualmente e não só em números. Usaremos a biblioteca seaborn atráves do "import seaborn as sns" usando a sigla "sns" para ativa-lá. Lembrando que é preciso instalar ela no terminal através do "pip install seaborn" e importar ela lá no topo com o "import seaborn as sns" para ai sim usar os comandos abaixo para gerar o gráfico.
# sns.boxplot(notas['nota'])
# plt.show()


