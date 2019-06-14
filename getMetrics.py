#!/usr/bin/env python

from matplotlib import pyplot as plt 
import pandas as pd
import numpy as np 
import os
import sys
import re

def natural_sort(l):
	convert = lambda text: int(text) if text.isdigit() else text.lower()
	alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key)]
	return sorted(l, key = alphanum_key)

def get_files(path,arq):
	files = []
	for r, d, f in os.walk(path):
		for file in f:
			if arq in file:
				files.append(os.path.join(r,file))
	files = natural_sort(files)
	return files	


def main():

	if len(sys.argv) != 2:
		print("./getImportantData <file.csv>")
		sys.exit()
	
	for weight in [100000,200000,400000,800000]:	
		knapsacks = get_files(sys.argv[1],str(weight))
		timeSum = 0.0
		times = []
		
		for knap in knapsacks: 		#percorre os testes de mesmo peso
			result = pd.read_csv(knap,delimiter=',')
			time = result[['time']].values.tolist()
			time = np.concatenate(time, axis=0)
			timeSum+= time
			times.append(time)
		
		media = np.divide(timeSum,len(knapsacks))
		times = np.subtract(times,media)
		times = map(lambda x: x**2, times)
		sd = np.sum(times,axis=0)
		sd = np.divide(sd,len(knapsacks))
		sd = np.sqrt(sd)
		
		df = pd.read_csv(knapsacks[0],delimiter=',')
		df.insert(6,"mean",media)
		df.insert(7,"dp",sd)
		
		threads = df['N_THREADS'].values.tolist()
		threads = map(lambda x: 1 if x==0 else x, threads)
		speedUp = [0.0]*len(threads)
		efficiency = [0.0]*len(threads)

		for i  in range(len(threads)):
			seq = 1.0
			if( threads[i] == 1 ):
				seq = media[i]
			speedUp[i] = seq/media[i]
			efficiency[i] = speedUp[i]/threads[i]
		
		df.insert(8,"spUp",speedUp)
		df.insert(9,"eff",efficiency)
		df = df.drop(['CHUNK_SIZE','max_weight','max_value'], axis=1)
		df = df.round(4)
		df.to_csv("result/metrics-m{}.csv".format(weight), encoding='utf-8',index = False)

main()



