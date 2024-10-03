# Mão na massa: criando uma matriz

# Você recebeu um conjunto de dados sobre temperaturas em diferentes cidades durante quatro trimestres do ano. 
# Cada cidade é representada por um vetor e cada trimestre é representado por outro vetor.

# A sua tarefa é criar uma matriz que organize essas informações de maneira adequada. 
# Aqui estão os vetores representando as cidades e os trimestres:
  
tri_1 <- c(25, 30, 22, 28, 18)
tri_2 <- c(20, 15, 22, 28, 32)
tri_3 <- c(30, 35, 10, 15, 8)
tri_4 <- c(12, 28, 25, 20, 22)
tri_5 <- c(10, 08, 25, 30, 35)



# Minha resposta para o exercicio:

colab_numero_somados <- c(tri_1, tri_2, tri_3, tri_4)
colab_numero_somados

matriz_numero_somados <- matrix(colab_numero_somados, nrow = 4, byrow = TRUE)
matriz_numero_somados

rownames(matriz_numero_somados)  <- c('Trimestre 1','Trimestre 2','Trimestre 3','Trimestre 4')
matriz_numero_somados

colnames(matriz_numero_somados) <- c('São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador', 'Porto Alegre')
matriz_numero_somados
















# Gabarito:

# Vetores representando cidades e trimestres
cidades <- c("São Paulo", "Rio de Janeiro", "Belo Horizonte", "Salvador", "Porto Alegre")
trimestres <- c("1º Trimestre", "2º Trimestre", "3º Trimestre", "4º Trimestre")

# Combinar os vetores
trimestres_comb <- c(tri_1, tri_2, tri_3, tri_4)

# Criar a matriz combinando os vetores
dados_temperatura <- matrix(trimestres_comb,
                            nrow = 4, # ou nrow = length(trimestres)
                            ncol = 5, # ou ncol = length(cidades)
                            byrow = TRUE,
)

# Nomeando a matriz
rownames(dados_temperatura) <- trimestres 
colnames(dados_temperatura) <- cidades 

# Exibir a matriz
print(dados_temperatura)