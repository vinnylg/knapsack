import pandas as pd
import matplotlib.pyplot as plt
import copy
import numpy as np
df = pd.read_csv("results-final.csv", delimiter = ',')

# FILE_NAME,N_THREADS,CHUNK_SIZE,N_OBJ,MAX_WEIGHT,MAX_VALUE,TIME

sort_df = df.sort_values(['N_THREADS'])



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



print resumos[6]['TIME']
# resumos[6].plot()

#fica tudo com uma so cor
# for i in range(9):
# 	plt.bar(resumos[i]['N_THREADS'],resumos[i]['TIME'], color='#aed6f1')

# #tempo de processamento maior entrada
# plt.bar(resumos[0]['N_THREADS'],resumos[0]['TIME'], color='#aed6f1')
# plt.bar(resumos[1]['N_THREADS'],resumos[1]['TIME'], color='#a3e4d7')
# plt.bar(resumos[2]['N_THREADS'],resumos[2]['TIME'], color='#a2d9ce')
# plt.bar(resumos[3]['N_THREADS'],resumos[3]['TIME'], color='#f9e79f')
# plt.bar(resumos[4]['N_THREADS'],resumos[4]['TIME'], color='#f8c471')
# plt.bar(resumos[5]['N_THREADS'],resumos[5]['TIME'], color='#f0b27a')
# plt.bar(resumos[6]['N_THREADS'],resumos[6]['TIME'], color='#d98880')
# plt.bar(resumos[7]['N_THREADS'],resumos[7]['TIME'], color='#f1948a')
# plt.bar(resumos[8]['N_THREADS'],resumos[8]['TIME'], color='#af7ac5')

# plt.xlabel("Threads usadas")
# plt.ylabel("Tempo Maior Entrada")
# plt.title("Escalabilidade")
# plt.show()


#tempo de processamento menor entrada
plt.bar(resumos[0]['N_THREADS'],resumos[0]['TIME']['min'], color='#aed6f1')
plt.bar(resumos[1]['N_THREADS'],resumos[1]['TIME']['min'], color='#a3e4d7')
plt.bar(resumos[2]['N_THREADS'],resumos[2]['TIME']['min'], color='#a2d9ce')
plt.bar(resumos[3]['N_THREADS'],resumos[3]['TIME']['min'], color='#f9e79f')
plt.bar(resumos[4]['N_THREADS'],resumos[4]['TIME']['min'], color='#f8c471')
plt.bar(resumos[5]['N_THREADS'],resumos[5]['TIME']['min'], color='#f0b27a')
plt.bar(resumos[6]['N_THREADS'],resumos[6]['TIME']['min'], color='#d98880')
plt.bar(resumos[7]['N_THREADS'],resumos[7]['TIME']['min'], color='#f1948a')
plt.bar(resumos[8]['N_THREADS'],resumos[8]['TIME']['min'], color='#af7ac5')

plt.xlabel("Threads usadas")
plt.ylabel("Tempo Menor Entrada")
plt.title("Escalabilidade")
plt.show()


#CALCULAR SPEEDUP CADA VERSAO