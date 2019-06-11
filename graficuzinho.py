import pandas as pd
import matplotlib.pyplot as plt
import copy
import numpy as np
df = pd.read_csv("final-lin.csv", delimiter = ',')

# FILE_NAME,N_THREADS,CHUNK_SIZE,N_OBJ,MAX_WEIGHT,MAX_VALUE,TIME

sort_df = df.sort_values(['N_THREADS'])

df.describe()

#1-49 exponencial
# print sort_df.head()
# print sort_df.tail()

resumos = []
for i in range(9):
	sequencial = df.loc[df['N_THREADS'] == i]
	describo = sequencial.describe()

	saida = describo[['N_THREADS','N_OBJ', 'MAX_WEIGHT', 'TIME']]
	saida2 = saida.loc[['min', '25%', '50%','75%','max'], : ]
	resumos.append(copy.copy(saida2))


print resumos[0]

#gera qualquer grafico top
cores = ['#aed6f1','#a3e4d7', '#a2d9ce', '#f9e79f', '#f8c471', '#f0b27a','#d98880','#f1948a','#af7ac5']
# for i in range(9):
# 	plt.bar(resumos[i]['N_THREADS'],resumos[i]['TIME']['max'], color=cores[i])


# plt.xlabel("Threads usadas")
# plt.ylabel("Tempo Maior Entrada Exponencial")
# plt.title("Escalabilidade")	
# plt.show()
# #salva grafico em um arquivo de saida
# plt.savefig('./ThreadsxMaiorExp.png')


speedups_max = []
speedups_min = []

Eficiencia_max = []
Eficiencia_min = []

# tmpSeq/p*Tparalelo
for i in range(1,9):
	#calculo speedup
	s_max = resumos[0]['TIME']['max']/float(resumos[i]['TIME']['max'])
	s_min = resumos[0]['TIME']['min']/float(resumos[i]['TIME']['min'])

	#calculo eficiencia
	e_max = resumos[0]['TIME']['max']/(float(resumos[i]['TIME']['max']) * i)
	e_min = resumos[0]['TIME']['min']/(float(resumos[i]['TIME']['min']) * i)

	speedups_max.append(round(s_max, 2))
	speedups_min.append(round(s_min, 2))

	Eficiencia_max.append(round(e_max, 2))
	Eficiencia_min.append(round(e_min, 2))

print Eficiencia_min
print Eficiencia_max

for i in range(0,8):
	plt.bar(resumos[i+1]['N_THREADS'], Eficiencia_max[i], color=cores[i])


plt.xlabel("Threads usadas")
plt.ylabel("Eficiencia")
plt.title("Eficiencia Maior Entrada Linear")	
plt.savefig('./Ef_max_lin.png')
plt.show()


#FALTA MEDIA/DESVIO PADRAO
#Cálculo do speedup para 1, 2, 4, 8, 16 e infitos processadores, utilizando asleis de Amdahl.