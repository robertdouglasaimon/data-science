# -*- coding: utf-8 -*-
"""Pandas: selecionando e agrupando dados - EXERCICIO 2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-jBxhs688uRn4uPZipQm_Pe62Ooaw98G

# Desafio: hora da prática

Chegou o momento de praticar! Vamos aplicar os conceitos aprendidos durante a aula a partir de algumas atividades. Solucione os problemas propostos através de códigos utilizando a base de dados disponibilizada no curso.


1. Faça um agrupamento de dados com base na coluna "Nível 1 - Setor" para visualizar o dicionário contendo as chaves de grupos formados e a lista de índices de cada grupo.

2. Faça um agrupamento de dados com base na coluna "Nível 1 - Setor" e localize os dados do grupo "Agropecuária".

3. Faça um agrupamento de dados com base na coluna "Nível 1 - Setor" para identificar a média de emissão de cada atividade econômica no ano de 2021.

4. Faça um agrupamento de dados com base na coluna "Nível 1 - Setor" para identificar a soma de emissão de cada atividade econômica. Ordene os dados da maior para menor emissão.

Caso precise de ajuda, opções de solução das atividades estarão disponíveis na seção [“Opinião da pessoa instrutora”](https://cursos.alura.com.br/course/pandas-selecao-agrupamento-dados/task/126755).
"""

!pip install pandas

import pandas as pd

from google.colab import drive
drive.mount('/content/drive')

dados = '/content/drive/MyDrive/Planilhas de estudo ALURA/SEEG10-BR_2022.10.27-FINAL.xlsx'

gases = pd.read_excel(dados, sheet_name = 'GEE Estados')
gases.head()

"""## Pronto, os dados foram devidamente carregados. Agora vamos começar o exercicio!"""

# 1. Faça um agrupamento de dados com base na coluna "Nível 1 - Setor" para visualizar o dicionário contendo as
# chaves de grupos formados e a lista de índices de cada grupo.

gases.groupby('Nível 1 - Setor').groups

# 2. Faça um agrupamento de dados com base na coluna "Nível 1 - Setor" e localize os dados do grupo "Agropecuária".
gases.groupby('Nível 1 - Setor').get_group('Agropecuária')

# 3. Faça um agrupamento de dados com base na coluna "Nível 1 - Setor" para identificar a média de emissão de cada atividade econômica no ano de 2021.

# Primeiro vamos preparar uma tabela para ultilizar os dados da coluna Nível 1 - Setor até a coluna 'Ano':

# Retonara um array com os anos de cada uma das colunas.
gases.loc[:,1970:2021].columns

# Retorna uma lista com os anos.
colunas_emissao = list(gases.loc[:,1970:2021].columns)
colunas_emissao

# Agora que ajustamos os anos, vamos ajustar os niveis:

# Essa linha de código retorna os nomes das colunas do DataFrame emissoes_gases que estão entre 'Nível 1 - Setor' e 'Produto'.
gases.loc[:,'Nível 1 - Setor':'Produto'].columns

# Retorna uma lista com o nome das colunas listadas que vão de  'Nível 1 - Setor' até 'Produto'.
gases.loc[:,'Nível 1 - Setor':'Produto'].columns
colunas_info = list(gases.loc[:,'Nível 1 - Setor':'Produto'].columns)
colunas_info

# Transformação do DataFrame, utilizamos o método melt(). Esse método tem o intuito de transformar um DataFrame de um formato amplo (wide) para o formato longo (long)
gases.melt(id_vars = colunas_info, value_vars = colunas_emissao, var_name = 'Ano', value_name = 'Emissao')

# Salvando a nova tabela em uma variável para usarmos daqui para frente nas analises :) :

emissoes_por_ano = gases.melt(id_vars = colunas_info, value_vars = colunas_emissao, var_name = 'Ano', value_name = 'Emissao')
emissoes_por_ano
# print(emissoes_por_ano)

# Agora sim vamos a resolução da questão 3:
emissoes_por_ano[emissoes_por_ano['Ano']==2021].groupby('Nível 1 - Setor')[['Emissao']].mean()

# 4. Faça um agrupamento de dados com base na coluna "Nível 1 - Setor" para identificar a soma de emissão de cada atividade econômica.
# Ordene os dados da maior para menor emissão.Faça um agrupamento de dados com base na coluna "Nível 1 - Setor" para identificar a soma de
# emissão de cada atividade econômica. Ordene os dados da maior para menor emissão.

emissoes_por_ano.groupby('Atividade Econômica')[['Emissao']].sum().sort_values(by='Emissao', ascending=False)