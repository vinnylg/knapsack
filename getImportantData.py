#!/usr/bin/env python

from matplotlib import pyplot as plt 
import pandas as pd
import numpy as np 
import os
import sys

def natural_sort(l):
	convert = lambda text: int(text) if text.isdigit() else text.lower()
	alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key)]
	return sorted(l, key = alphanum_key)

def read_files(path,arqs):
	files = []
	for r, d, f in os.walk(path):
		for file in f:
			if arqs in file:
				files.append(os.path.join(r,file))
	files = natural_sort(files)
	return files	

def getWeights(df):
	result = df.drop_duplicates(subset='max_weight')
	result = result[['max_weight']].values.tolist()
	return np.concatenate(result,axis = 0)


def getDataForWeights(df,max_weight,):
	result = df.loc[(df['max_weight'] == max_weight)]
	result = result[['N_THREADS','n_obj','time']]
	return result


def main():

	if len(sys.argv) == 1:
		print("./getImportantData <file.csv>")
		sys.exit()
	
	df = pd.read_csv(sys.argv[1],delimiter=',')

	for i in [200000,400000,800000,1600000]:

		result = df.loc[(df['max_weight'] == i)]

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

	weights = getWeights(saida) 

		 data = getDataForWeights(saida,weight)
		 print(weight)
		 print(data)
		 th = data['N_THREADS'].values.tolist()
		 objs = data['n_obj'].values.tolist()
		 time = data['N_THREADS'].values.tolist()

		 #data.to_csv("graphs/graph_weight-{}.csv".format(weight), encoding='utf-8',index = False)










main()



