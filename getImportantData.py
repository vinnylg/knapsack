#!/usr/bin/env python

from matplotlib import pyplot as plt 
import pandas as pd
import numpy as np 
import os
import sys

if len(sys.argv) == 1:
    print("./getImportantData <file.csv>")
    sys.exit()

df = pd.read_csv(sys.argv[1],delimiter=',')

result = df.loc[(df['N_THREADS'] == 0) & (df['time'] >= 10)]

result = result[['n_obj','max_weight']]

n_obj = result['n_obj'].values.tolist()
max_weight = result['max_weight'].values.tolist()

th = []
objs = []
weights = []
time = []

for i in range(len(n_obj)):
    #os.system("./createItem mochila_final/mf{}-{} {} {}".format(n_obj[i],max_weight[i],n_obj[i],max_weight[i]))
    result = df.loc[(df['n_obj'] == n_obj[i]) & (df['max_weight'] == max_weight[i])]
    result = result[['N_THREADS','n_obj','max_weight','time']]
    th.append(result['N_THREADS'].values.tolist())
    objs.append(result['n_obj'].values.tolist())
    weights.append(result['max_weight'].values.tolist())
    time.append(result['time'].values.tolist())
    

th = np.concatenate(th,axis = 0)
objs = np.concatenate(objs,axis = 0)
weights = np.concatenate(weights,axis = 0)
time = np.concatenate(time,axis = 0)
time.all()


data_tuple = (list(zip(th,objs,weights,time)))

saida = pd.DataFrame(data_tuple,columns=['N_THREADS','n_obj','max_weight','time'])

saida.to_csv(sys.argv[1].replace('.csv','_')+'relevantes.csv', encoding='utf-8',index = False)