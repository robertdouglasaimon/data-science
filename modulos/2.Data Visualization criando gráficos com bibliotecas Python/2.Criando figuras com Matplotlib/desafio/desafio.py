import pandas as pd
import matplotlib.pyplot as plt
# import numpy as np
# import seaborn as sns

lojas =  ['A', 'B', 'C', 'D']

vendas_2022 = {
    'Jan': [100, 80, 150, 50],
    'Fev': [120, 90, 170, 60],
    'Mar': [150, 100, 200, 80],
    'Abr': [180, 110, 230, 90],
    'Mai': [220, 190, 350, 200],
    'Jun': [230, 150, 280, 120],
    'Jul': [250, 170, 300, 140],
    'Ago': [260, 180, 310, 150],
    'Set': [240, 160, 290, 130],
    'Out': [220, 140, 270, 110],
    'Nov': [400, 220, 350, 190],
    'Dez': [300, 350, 400, 250]
}

df = pd.DataFrame(vendas_2022, index=lojas)
df.head()
print(df.head())

df['lojas'] = lojas # Define lojas como uma coluna
df.set_index('lojas', inplace=True) # Transforma Lojas no INDEX da tabela.
df.head() # Mostra os 5 primeiros itens do DF.
print(df.head())


# Criando o gráfico:
fig, axs = plt.subplots(2, 2, figsize=(10, 6)) # Inicia a criação dos gráficos.
fig.suptitle('Vendas por Loja ao Longo do Ano', fontsize=16) # Adiciona um titulo geral para todos os gráficos.
fig.subplots_adjust(hspace=0.5, wspace=0.3 ) # Adiciona um espaço entre os gráficos. hspace=0.5: Controla o espaçamento horizontal. wspace=0.3: Controla o espaçamento vertical.

# Chamando os atributos da tabela para os graficos:
axs[0,0].plot(df.loc['A'])
axs[0,0].set_title('Loja A')

axs[0,1].plot(df.loc['B'])
axs[0,1].set_title('Loja B')

axs[1,0].plot(df.loc['C'])
axs[1,0].set_title('Loja C')

axs[1,1].plot(df.loc['D'])
axs[1,1].set_title('Loja D')

for ax in axs.flat:  # Itera sobre os eixos do gráfico.
    ax.set(xlabel='Mês')  # Define o nome do eixo x.
    ax.set(ylabel='Vendas')  # Define o nome do eixo y.
    ax.grid(True)  # Adiciona uma grade ao gráfico.

plt.show()