import pandas as pd

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


print(notas['nota'].mean())  # Nunca apagar esse print, ele quem renderiza os comandos dentro dos parenteses dele.

