# -*- coding: utf-8 -*-
"""Pandas: conhecendo a biblioteca - Desafio 2: bora praticar?

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1U5J84AU5H4aGQPUcA4n1BGMmH29ljJaQ

# Desafio 2: bora praticar?

O time de ML chegou com algumas demandas de última hora para resolvermos nesse momento da análise exploratória. Essas demandas são:

1) Calcular a média de quartos por apartamento;

2) Conferir quantos bairros únicos existem na nossa base de dados;

3) Analisar quais bairros possuem a média de valor de aluguel mais elevadas;

4) Criar um gráfico de barras horizontais que apresente os 5 bairros com as médias de valores de aluguel mais elevadas.

<br>

Caso queira, deixo disponibilizado um [notebook para resolver os desafios](https://cdn3.gnarususercontent.com.br/2925-introducao-pandas/desafios.ipynb). Você pode baixá-lo e fazer upload no Google Drive ou direto no Google Colab para realizar os desafios dessa e das outras aulas. Como vamos utilizar a mesma base de dados do nosso projeto, no notebook de resolução dos desafios, eu fiz novamente a importação da nossa base de dados e apliquei as alterações que já realizamos nela até aqui.

Se precisar de ajuda, na seção "Opinião do Instrutor" você pode encontrar algumas formas de resolver os desafios propostos acima.
"""

import pandas as pd
import matplotlib.pyplot as plt

url ='https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
pd.read_csv(url)

pd.read_csv(url, sep=';') # "sep=';' = Separa por ; os itens da tabela.

dados = pd.read_csv(url, sep=';') # "sep=';' = Separa por ; os itens da tabela.
dados

dados.Tipo.unique() # Mostra os tipos de imóveis.
imoveis_comerciais = ['Conjunto Comercial/Sala',
                      'Prédio Inteiro', 'Loja/Salão',
                      'Galpão/Depósito/Armazém',
                      'Casa Comercial', 'Terreno Padrão',
                      'Loja Shopping/ Ct Comercial',
                      'Box/Garagem', 'Chácara',
                      'Loteamento/Condomínio', 'Sítio',
                      'Pousada/Chalé', 'Hotel', 'Indústria'] # Cria uma váriavel com os tipos de imóveis comerciais.

dados.query('@imoveis_comerciais not in Tipo') # Cria uma tabela com os tipos de imóveis não comerciais.

df_imoveis_residenciais = dados.query('@imoveis_comerciais not in Tipo') # Cria uma tabela com os tipos de imóveis não comerciais e atribui ele a váriavel.
df_imoveis_residenciais.head()

df_imoveis_residenciais.query('Tipo == "Apartamento"') # Mostra apenas os imóveis do tipo apartamento.

df_apartamentos = df_imoveis_residenciais.query('Tipo == "Apartamento"') # Mostra apenas os imóveis do tipo apartamento e atribui ele a váriavel.
                                                                         # df_apartamentos.
df_apartamentos.head()

# Após estruturar os dados que serão necessarios, vamos resolver a atividade:

# 1)
df_apartamentos.Quartos.mean() # Mostra a média de quartos por apartamento.

# 2)
df_imoveis_residenciais.Bairro.unique() # Mostra os bairros únicos da tabela.

# 2.1)
df_bairro_unicos = len(df_imoveis_residenciais.Bairro.unique()) # Mostra o número de bairros únicos da tabela.
df_bairro_unicos

# 3)
df_imoveis_residenciais.groupby('Bairro')['Valor'].mean().sort_values(ascending=False) # Mostra os bairros com as médias de valores de aluguel mais elevadas.

# 4)
df_bairros_unicos = df_imoveis_residenciais.groupby('Bairro')['Valor'].mean().sort_values(ascending=False)
df_bairros_unicos.head()

# 4.1)
df_bairros_unicos.head(5).plot(kind='barh', figsize=(14,10), color='blue'); # Mostra o gráfico de barras horizontais dos 5 bairros com as médias de valores de aluguel mais elevadas.