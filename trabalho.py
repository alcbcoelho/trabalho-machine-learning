# Alunos:
# Pedro Henrique da S Rocha 2124290005
# Ranom Morais Ruiz 2124290027
# Alisson Silva dos Santos 2214290086
# André Luís Costa Bandeira Coelho 2124290028

import pandas as pd
import statistics
import matplotlib.pyplot as plt

##########################################
# EXERCÍCIO 1
# 
# Ajuste as idades que não são válidas ou estão vazias para a moda da amostra. Grave a saída no arquivo Resposta01.txt.
# 
##########################################

# lê o arquivo
df = pd.read_csv('dados4.csv')

# remove valores inválidos
idadeValidas = df['age'].dropna()

# calcula a moda das idades
modaIdade = statistics.mode(idadeValidas)

# substitui as idades inválidas pela moda
df['age'].fillna(modaIdade, inplace=True)

# salva um arquivo
df.to_csv('Resposta01.txt', index=False)

##########################################
# EXERCÍCIO 2
# 
# Apresente no terminal o somatório de homens (male) e de mulheres (female)
# 
##########################################

df = pd.read_csv('dados4.csv')

# fazendo a contagem
contGenero = df['sex'].value_counts()

# Retorna a quantidade separada de homens e mulheres
print(f'Quantidade de homens e mulheres:\n{contGenero}')

##########################################
# EXERCÍCIO 3
# 
# Considerando a coluna "survived", sendo 0 como não sobrevivente e 1 como sobrevivente, apresente em um gráfico de pizza
# a porcentagem de sobreviventes e não sobreviventes.
# 
##########################################

df = pd.read_csv('dados4.csv')

# fazendo a contagem dos vivos e mortos
contSobrevivencia = df['survived'].value_counts()

# cria a figura 5x5
plt.figure(figsize=(5, 5))

# cria o grafico pizza(torta) e o autopct da o valor em porcentagem
plt.pie(contSobrevivencia, labels=['Mortos', 'Sobreviventes'], autopct='%1.0f%%')

# Nomes do grafico
plt.title('Mortos e Sobreviventes')

# Reproduz o grafico
plt.show()

##########################################
# EXERCÍCIO 4
# 
# Apresente o gráfico de dispersão da Idade pela tarifa.
# 
#########################################

df = pd.read_csv('dados4.csv')

# cria a figura 5x5
plt.figure(figsize=(5, 5))

# cria o grafico de dispersão com a coluna da idade e da tarifa
plt.scatter(df['age'], df['fare'])

# cria o titulo do eixo x
plt.xlabel('Idade')

# cria o titulo do eixo y
plt.ylabel('Tarifa')

# cria o titulo do grafico
plt.title('Dispersão da Idade pela Tarifa')

# exibição do grafico
plt.show()