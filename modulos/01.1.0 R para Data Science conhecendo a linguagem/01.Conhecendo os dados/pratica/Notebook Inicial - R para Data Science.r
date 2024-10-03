# ## Aula 1 - Conhecendo os dados

# #### Projeto do curso

# # Nós estamos trabalhando em um projeto de uma empresa de People Analytics chamada Tech Safe.

# # O nosso objetivo principal será realizar uma análise exploratória e responder perguntas levantadas pela Tech Safe.

# # Ao longo do curso iremos responder diversas perguntas sobre os dados fornecidos pela empresa.

# # Notebook Inicial - R para Data SciencePara isso, vamos utilizar a linguagem de programação R.




# ### Projeto da aula
# 1 - col A primeira tabela que vamos criar, será a de Colaboradores. Nessa tabela, teremos informações como: Nome, Idade, Salário, Telefone Fixo e Trabalho Remoto.

# # Segue abaixo a tabela que a Tech passou para trabalharmos:

# # | Nome            | Idade | Salário | Telefone Fixo    | Trabalho Remoto |
# # |-----------------|-------|---------|------------------|-----------------|
# # | Ana Silva       | 28    | 6230.50 | Não possui       | Sim             |
# # | Carlos Oliveira | 35    | 7500.75 | \(11\) 1234-5678 | Sim             |
# # | Maria Santos    | 40    | 8000.25 | \(21\) 9876-5432 | Não             |
# # | João Costa      | 32    | 2460.80 | Não possui       | Sim             |
# # | Fernanda Lima   | 27    | 4230.35 | \(31\) 8765-4321 | Sim             |


# RESOLVENDO O EXERCICIO 1 - CRIANDO A TABELA  ⬇️-----------------------------------------------------------------
ana_silva <- c('Ana Silva', 28, 6230.50, 'Não possui', TRUE)
carlos_oliveira <- c('Carlos Oliveira', 35, 7500.75, '(11) 1234-5678', TRUE)
maria_santos <- c('Maria Santos', 40, 8000.25, '(21) 9876-5432', TRUE)
joao_costa <- c('Joao Costa', '32', 2460.80, 'Não possui', FALSE)
fernanda_lima <- c('Fernanda Lima', 27, 4230.35, '(31) 8765-4321', TRUE)

colab_combinado <- c(ana_silva, carlos_oliveira, maria_santos, joao_costa, fernanda_lima)

matriz_colab <- matrix(colab_combinado, nrow = 5, byrow = TRUE)

rownames(matriz_colab) <- c('Colaboradora Ana', 'Colaborador Carlos Oliveira', 'Colaboradora Maria Santos', 'Colaborador Joao Costa', 'Colaboradora Fernanda Lima')

colnames(matriz_colab) <- c('Nome', 'Idade', 'Salario', 'Telefone', 'Trabalho Remoto')

print(matriz_colab)
# ----------------------------------------------------------------------------------------------------------------



# ## Aula 2 - Manipulando os dados

# ### Projeto da aula

# # Nesta aula, vamos utilizar uma tabela de vendas, contendo os valores das vendas de 5 colaboradores referentes a 6 meses de vendas.

# ```{r}
# # Vetor com valores das vendas
# vendas_jan <- c(20, 18, 25, 16, 23)
# vendas_fev <- c(15, 20, 22, 18, 19)
# vendas_mar <- c(25, 23, 20, 17, 21)
# vendas_abr <- c(18, 15, 19, 20, 24)
# vendas_mai <- c(22, 25, 21, 15, 18)
# vendas_jun <- c(21, 22, 19, 17, 20)
# ```

# ```{r}
# # Nomes das pessoas
# pessoas <- c("Pedro Santos", "Carla Nunes", "Maria Eduarda", "Luiz Felipe", "Julio Costa")

# # Nomes dos meses
# meses <- c("Janeiro", "Fevereiro", "Marco", "Abril", "Maio", "Junho")
# ```

# ```{r}
# # Combinar as vendas
# vendas_semestre <- c(vendas_jan, vendas_fev, vendas_mar, vendas_abr, vendas_mai, vendas_jun)

# # Vendas de cada pessoa por mês (em milhares)
# matriz_vendas <- matrix(vendas_semestre, nrow = 5, byrow = FALSE)
# ```

# ```{r}
# # Nomear a matriz
# rownames(matriz_vendas) <- pessoas
# colnames(matriz_vendas) <- meses
# ```

# ```{r}
# # Exibir a matriz
# matriz_vendas
# ```

# Vamos tentar descobrir o seguinte:

# -   Qual colaborador teve o maior faturamento nas vendas?

# -   Qual mês teve maior faturamento?


# ## Aula 3 - Estruturas condicionais e de repetição

# ### Projeto da aula

# Suponha que estamos lidando com dados de um armazém que vende produtos eletrônicos e tem um estoque representado por uma matriz de preços unitários e quantidades em estoque.

# ```{r}
# preco <- c(50, 100, 150, 25, 75)

# qtd_estoque <- c(10, 5, 20, 30, 7)

# preco_estoque <- c(preco, qtd_estoque)

# matriz_estoque <- matrix(preco_estoque, ncol = 2)

# rownames(matriz_estoque) <- c('Notebook', 'Tablet', 'Monitor', 'Smartphone', 'Headset')
# colnames(matriz_estoque) <- c('Produto', 'Estoque')

# matriz_estoque
# ```

# A partir dessa matriz, vamos buscar descobrir o seguinte:

# -   Calcular o valor total em estoque.

# -   Identificar produtos com estoque baixo (menos de 15 unidades).

# -   Classificar o valor total em estoque em alto ou baixo.

# -   Aplicar desconto de 10% em todos os produtos do estoque.

# -   Descobrir qual o produto mais vendido.


# ## Aula 4 - Funções matemáticas e estatísticas

# ### Projeto da aula

# Vamos criar uma nova matriz de vendas. Dessa vez, vamos incluir a receita das vendas na matriz.

# A partir dessa matriz, vamos responder às seguintes :

# -   Quantos produtos com preço acima de 600 foram vendidos?

# -   Qual a receita média das vendas?

# -   Existe uma diferença muito grande entre a média e a mediana das receitas?

# -   Qual o produto mais caro e qual o mais barato?

# Primeiramente, vamos criar a matriz:

# ```{r}
# dados_vendas <- matrix(c(
#   1230.75, 20, 24615,
#   840.46, 35, 29416.10,
#   110.20, 15, 1653,
#   519.67, 10, 5196.70,
#   650.90, 25, 16272.50

# ), ncol = 3, byrow = TRUE)

# rownames(dados_vendas) <- c('Ar Condicinado', 'Cama', 'Mesa', 'Refrigerador', 'Sofa')
# colnames(dados_vendas) <- c("Preco", "Quantidade", "Receita")

# dados_vendas
# ```



# ## Aula 5 - Fatores

# ### Projeto da aula

# Suponha que você tenha um conjunto de dados que representa o status de entrega de diferentes produtos.

# ```{r}
# status_entrega <- c("Entregue", "Em Trânsito", "Pendente", "Entregue", "Em Trânsito")

# nomes_produtos <- c("Smartphone", "Notebook", "Monitor", "Mouse", "Tablet")

# names(status_entrega) <- nomes_produtos

# status_entrega
# ```

