<h1>Desafio: </h1>  

![Curso de Data Science](https://img.shields.io/badge/Curso%20de%20Data%20Science-blue?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDhcAAADiSURBVDiNpZM7SwNBEEWnps7QYWJlIZWEV1LZ9DcdzH+gQEIBQ8BBcREzUwstLIaA0ILeQNLEwkjRRVybqulZs2trzL6qbvd+aBCKZHq7D7l9zvsDAB/gNQwI2MErmL3uL92FeQJ6AwDVro0ZjXomEN4p7MOuUAK5/hfQ7HsLMBBJYAu5QMykqlcA6Db6vMTvDpFMDloLKae4DsMQkmHgMYhMAMyrzOtcXZgQgSB0OA98PM23HddIbBfYEoMB8FZKzCCPLmjV4VmPHOs1ALiW4os75FbkpFgCrFLXQOg0PhUTjHZ/FavXcQe4RnmEgAAAABJRU5ErkJggg==)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

![Matplotlib Pyplot](https://img.shields.io/badge/Matplotlib%20Pyplot-11557C?style=for-the-badge&logo=matplotlib&logoColor=white)


<h2>Desafio: visualizando dados de vendas de diferentes lojas</h2>

<p>
    Você trabalha como Analista de Dados em uma empresa de varejo e recebeu a tarefa de criar uma figura com subplots que apresente a variação no número de vendas em quatro diferentes lojas ao longo de um ano. A gerência da empresa precisa visualizar de forma clara as tendências de vendas em cada loja, para que possam tomar decisões estratégicas sobre os estoques e ações de marketing. Para isso, você deve criar quatro subplots dispostos em duas linhas e duas colunas, onde cada subplot representa uma loja diferente. Nesse desafio, cada subplot deve apresentar um gráfico de linhas que mostre a variação do número de vendas ao longo dos meses do ano.
</p>

<p>
    Agora, chegou a hora de mostrar suas habilidades em análise de dados e visualização! Para criar o DataFrame com o número de vendas das lojas e criar a figura, utilize as informações abaixo:
</p>

<p>
    lojas =  ['A', 'B', 'C', 'D']

    vendas_2022 = {'Jan': [100, 80, 150, 50],
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
</p>

<p>
    <b>Dica:</b> Para facilitar a criação dos subplots, você pode definir a coluna "Lojas" como índice do DataFrame e utilizar a propriedade loc da biblioteca Pandas para plotar cada uma das lojas.
</p>