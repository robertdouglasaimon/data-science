# Mão na massa: manipulando matrizes

# Você recebeu um conjunto de dados que representa as vendas mensais de produtos em diferentes 
# regiões. O conjunto de dados é uma matriz chamada dados_vendas:

# Matriz representando as vendas mensais (em milhares de unidades)
 dados_vendas <- matrix(c(50, 60, 45, 30, 55, 65, 40, 35, 60, 70, 55, 50), nrow = 3, byrow = TRUE)

 #Nomes das regiões e dos meses
 regioes <- c("Norte", "Sul", "Nordeste")
 meses <- c("Jan", "Fev", "Mar", "Abr")

 rownames(dados_vendas) <- regioes
 colnames(dados_vendas) <- meses
 
 dados_vendas

# Sua tarefa é realizar as seguintes operações:
  
# Indexação:
  
# Acesse o valor de vendas da região "Sul" no mês de "Fev".
# Somar Colunas:
 
 # Resposta:
  dados_vendas[2,2]
  
# Calcule o total de vendas para cada mês, utilizando a função colSums(). 
# Armazene os resultados em um vetor chamado total_por_mes.
# Somar Linhas:
 
 # Resposta:
  total_por_mes <- colSums(dados_vendas)
  total_por_mes
 
# Calcule o total de vendas para cada região, utilizando a função rowSums(). 
# Armazene os resultados em um vetor chamado total_por_regiao.
# Adicionar Nova Região:
  
  # Resposta:
  total_por_regiao <- rowSums(dados_vendas)
  total_por_regiao
  
# Adicione uma nova região chamada "Centro-Oeste" com as vendas mensais (em milhares de unidades) 
# de 35, 40, 30, 25 para os meses de "Jan", "Fev", "Mar", "Abr", respectivamente.

  # Resposta:
  nova_regiao <- c(35, 40, 30, 25)
  dados_vendas <- rbind(dados_vendas, nova_regiao)
  rownames(dados_vendas)[4] <- "Centro Oeste"
  dados_vendas


