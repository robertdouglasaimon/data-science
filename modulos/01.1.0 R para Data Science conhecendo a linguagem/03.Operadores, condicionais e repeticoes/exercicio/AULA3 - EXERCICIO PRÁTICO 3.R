# Mão na massa: condicional e repetição

# Você está desenvolvendo um programa para auxiliar em uma competição de corrida. 
# Cada corredor tem sua própria velocidade média em metros por segundo (m/s). 
# Sua tarefa é calcular o tempo estimado que cada corredor levará para percorrer uma determinada distância, 
# que será fornecida como entrada.

# Para começar, temos definidas a variável com a distância em metros da corrida e o vetor 
# com as velocidades dos corredores:

# Definir a distância da corrida (metros)
distancia <- 200

# Lista de velocidades dos corredores em m/s
velocidades <- c(5, 7, 10, 12, 15)

# A partir dessas variáveis, você irá realizar as seguintes tarefas:

# Você irá iterar sobre o vetor de velocidades de corredores, representadas em m/s, utilizando o for.

# Para cada corredor, você deve calcular o tempo estimado (em segundos) para percorrer a distância definida.

# Durante a iteração, verifique as seguintes condições utilizando if() e else():

#  * Se o tempo estimado for inferior a 10 segundos, imprima "Rápido!".
#  * Se o tempo estimado estiver entre 10 e 20 segundos (inclusive), imprima "Bom desempenho!".
#  * Se o tempo estimado for superior a 20 segundos, imprima "Desempenho a melhorar!".



# Resposta da atividade:
for (velocidade in velocidades) {
  
  # Calcula o tempo estimado para percorrer a distância
  tempo_estimado <- distancia / velocidade
  
  # Verifica as condições com if() e else()
  if (tempo_estimado < 10) {
    print("Rápido!")
  } else if (tempo_estimado >= 10 && tempo_estimado <= 20) {
    print("Bom desempenho!")
  } else {
    print("Desempenho a melhorar!")
  }
}
