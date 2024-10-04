## Aula 1 - Conhecendo os dados

#### Projeto do curso

Nós estamos trabalhando em um projeto de uma empresa de People Analytics chamada Tech Safe.

O nosso objetivo principal será realizar uma análise exploratória e responder perguntas levantadas pela Tech Safe.

Ao longo do curso iremos responder diversas perguntas sobre os dados fornecidos pela empresa.

Para isso, vamos utilizar a linguagem de programação R.

### Projeto da aula

A primeira tabela que vamos criar, será a de Colaboradores. Nessa tabela, teremos informações como: Nome, Idade, Salário, Telefone Fixo e Trabalho Remoto.

Segue abaixo a tabela que a Tech passou para trabalharmos:

| Nome            | Idade | Salário | Telefone Fixo    | Trabalho Remoto |
|-----------------|-------|---------|------------------|-----------------|
| Ana Silva       | 28    | 6230.50 | Não possui       | Sim             |
| Carlos Oliveira | 35    | 7500.75 | \(11\) 1234-5678 | Sim             |
| Maria Santos    | 40    | 8000.25 | \(21\) 9876-5432 | Não             |
| João Costa      | 32    | 2460.80 | Não possui       | Sim             |
| Fernanda Lima   | 27    | 4230.35 | \(31\) 8765-4321 | Sim             |

RESOLUÇÃO EXERCICIO 1 CRIANDO A TABELA ⬇️ ------------------------------------------------------------

```{r}
ana_silva <- c('Ana Silva', 28, 6230.50, 'Não possui', TRUE)
carlos_oliveira <- c('Carlos Oliveira', 35, 7500.75, '(11) 1234-5678', TRUE)
maria_santos <- c('Maria Santos', 40, 8000.25, '(21) 9876-5432', TRUE)
joao_costa <- c('Joao Costa', '32', 2460.80, 'Não possui', FALSE)
fernanda_lima <- c('Fernanda Lima', 27, 4230.35, '(31) 8765-4321', TRUE)
```

```{r}
colab_combinado <- c(ana_silva, carlos_oliveira, maria_santos, joao_costa, fernanda_lima)
```

```{r}
matriz_colab <- matrix(colab_combinado, nrow = 5, byrow = TRUE)

```

```{r}
rownames(matriz_colab) <- c('Colaboradora Ana', 'Colaborador Carlos Oliveira', 'Colaboradora Maria Santos', 'Colaborador Joao Costa', 'Colaboradora Fernanda Lima')

colnames(matriz_colab) <- c('Nome', 'Idade', 'Salario', 'Telefone', 'Trabalho Remoto')

matriz_colab
```

## Aula 2 - Manipulando os dados

### Projeto da aula

Nesta aula, vamos utilizar uma tabela de vendas, contendo os valores das vendas de 5 colaboradores referentes a 6 meses de vendas.

```{r}
# Vetor com valores das vendas
vendas_jan <- c(20, 18, 25, 16, 23)
vendas_fev <- c(15, 20, 22, 18, 19)
vendas_mar <- c(25, 23, 20, 17, 21)
vendas_abr <- c(18, 15, 19, 20, 24)
vendas_mai <- c(22, 25, 21, 15, 18)
vendas_jun <- c(21, 22, 19, 17, 20)
```

```{r}
# Nomes das pessoas
pessoas <- c("Pedro Santos", "Carla Nunes", "Maria Eduarda", "Luiz Felipe", "Julio Costa")

# Nomes dos meses
meses <- c("Janeiro", "Fevereiro", "Marco", "Abril", "Maio", "Junho")
```

```{r}
# Combinar as vendas
vendas_semestre <- c(vendas_jan, vendas_fev, vendas_mar, vendas_abr, vendas_mai, vendas_jun)

# Vendas de cada pessoa por mês (em milhares)
matriz_vendas <- matrix(vendas_semestre, nrow = 5, byrow = FALSE)
```

```{r}
# Nomear a matriz
rownames(matriz_vendas) <- pessoas
colnames(matriz_vendas) <- meses
```

```{r}
# Exibir a matriz
matriz_vendas
```

-   Entendendo como acessar os elementos na prática:

    ```{r}
    vendas_jan 

    ```

    ```{r}
    vendas_jan[3]
    # Maior valor desse vetor
    ```

    ```{r}
    # Menor valor desse vetor
    vendas_jan[4]
    ```

    ```{r}

    # Utilizando ID do atributo para puxar todos os seus dados.
    # Obs: Essa estrutura [4, ] diz que: Você quer a 4º linha da tabela e o espaço vazio " , ] " quer dizer que você que todos os atributos de todas as colunas ligadas esse ID. No caso desse exemplo, todos os valores de todos os meses.

    matriz_vendas[4, ]
    ```

    ```         
    ```

    ```{r}
    # Utilizando o ATRIBUTO para puxar todos os seus dados.
    # Obs: Essa estrutura ['Luiz Felipe', ] diz que: Você quer especificamente o atributo 'Luiz Felipe' da tabela e o espaço vazio " , ] " quer dizer que você quer TODOS os atributos de todas as colunas ligadas esse atributo. No caso desse exemplo, todos os valores de todos os meses.
    matriz_vendas['Luiz Felipe', ]
    ```

    ```{r}

    ```

Vamos tentar descobrir o seguinte:

-   Qual colaborador teve o maior faturamento nas vendas?

-   Qual mês teve maior faturamento?

    ```{r}
    # Resolvendo a atividade:


    # Calculando o maior faturamento entre os colaboradores:
    rowSums(matriz_vendas)
    ```

    ```{r}
    # Calculando qual mês teve o maior faturamento:
    colSums(matriz_vendas)
    ```

    ```{r}
    # Adicionando mais uma coluna e mais uma linha na tabela de vendas para mostrar o total de vendas e faturamento na tabela principal:


    # Criando primeiro a coluna total_colab para os colaboradores:
    total_colab <- rowSums(matriz_vendas)
    matriz_total_colab <- cbind(matriz_vendas, total_colab)
    matriz_total_colab
    ```

    ```{r}
    # Criando a coluna total_meses para os meses:
    total_meses <- colSums(matriz_vendas)
    matriz_total_meses <- rbind(matriz_vendas, total_meses)
    matriz_total_meses
    ```

    # EXERCICIO \#

    Suponha que você esteja trabalhando com dados de temperatura média mensal de diversas cidades ao redor do mundo, armazenados em uma matriz no R. Cada linha representa um trimestre do ano, e cada coluna representa uma cidade específica. O objetivo é realizar operações de análise e extração de informações nessa matriz.

    Abaixo temos o código para criar a matriz:

    ```{r}

    # Criando a matriz de temperaturas
    temperaturas <- matrix(c(25, 30, 22, 28, 18, 20, 15, 22, 28, 32, 30, 35, 10, 15, 8, 12, 28, 25, 20, 22), 
                           nrow = 4, ncol = 5, byrow = TRUE)

    # Atribuindo nomes às linhas
    rownames(temperaturas) <- c('1 Tri', '2 Tri', '3 Tri', '4 Tri')

    # Atribuindo nomes às colunas
    colnames(temperaturas) <- c('SP', 'BA', 'PA', 'MG', 'RS')

    # Exibindo a matriz
    print(temperaturas)

    ```

    Considerando essa matriz, gostaria de realizar as seguintes seleções:

    -   Temperatura de SP ao longo de todos os trimestres do ano;

    -   Temperatura do 2º trimestre de todas as cidades;

    -   Temperatura de MG no 3º trimestre.

    ```{r}

    # Resolvendo a atividade: 

    temperaturas[1:4, 'SP']
    temperaturas[2, ]
    temperaturas['3 Tri', 4]
    ```

    # Atribuindo nomes às linhas

    rownames(temperaturas) \<- c('1 Tri', '2 Tri', '3 Tri', '4 Tri')

    # Atribuindo nomes às colunas

    colnames(temperaturas) \<- c('SP', 'BA', 'PA', 'MG', 'RS')

    # Exibindo a matriz

    print(temperaturas)

    \`\`\`

## Aula 3 - Estruturas condicionais e de repetição

### Projeto da aula

Suponha que estamos lidando com dados de um armazém que vende produtos eletrônicos e tem um estoque representado por uma matriz de preços unitários e quantidades em estoque.

```{r}
preco <- c(50, 100, 150, 25, 75)

qtd_estoque <- c(10, 5, 20, 30, 7)

preco_estoque <- c(preco, qtd_estoque)

matriz_estoque <- matrix(preco_estoque, ncol = 2)

rownames(matriz_estoque) <- c('Notebook', 'Tablet', 'Monitor', 'Smartphone', 'Headset')
colnames(matriz_estoque) <- c('Produto', 'Estoque')

matriz_estoque
```

A partir dessa matriz, vamos buscar descobrir o seguinte:

-   Calcular o valor total em estoque.

-   Identificar produtos com estoque baixo (menos de 15 unidades).

-   Classificar o valor total em estoque em alto ou baixo.

-   Aplicar desconto de 10% em todos os produtos do estoque.

-   Descobrir qual o produto mais vendido.

## Aula 4 - Funções matemáticas e estatísticas

### Projeto da aula

Vamos criar uma nova matriz de vendas. Dessa vez, vamos incluir a receita das vendas na matriz.

A partir dessa matriz, vamos responder às seguintes :

-   Quantos produtos com preço acima de 600 foram vendidos?

-   Qual a receita média das vendas?

-   Existe uma diferença muito grande entre a média e a mediana das receitas?

-   Qual o produto mais caro e qual o mais barato?

Primeiramente, vamos criar a matriz:

```{r}
dados_vendas <- matrix(c(
  1230.75, 20, 24615,
  840.46, 35, 29416.10,
  110.20, 15, 1653,
  519.67, 10, 5196.70,
  650.90, 25, 16272.50

), ncol = 3, byrow = TRUE)

rownames(dados_vendas) <- c('Ar Condicinado', 'Cama', 'Mesa', 'Refrigerador', 'Sofa')
colnames(dados_vendas) <- c("Preco", "Quantidade", "Receita")

dados_vendas
```

## Aula 5 - Fatores

### Projeto da aula

Suponha que você tenha um conjunto de dados que representa o status de entrega de diferentes produtos.

```{r}
status_entrega <- c("Entregue", "Em Trânsito", "Pendente", "Entregue", "Em Trânsito")

nomes_produtos <- c("Smartphone", "Notebook", "Monitor", "Mouse", "Tablet")

names(status_entrega) <- nomes_produtos

status_entrega
```
