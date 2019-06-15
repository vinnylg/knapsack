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
		print media
		for i  in range(len(threads)):
			speedUp[i] = media[0]/media[i]*threads[i]
			efficiency[i] = speedUp[i]/threads[i]
		
		df.insert(8,"spUp",speedUp)
		df.insert(9,"eff",efficiency)
		df = df.drop(['CHUNK_SIZE','max_weight','max_value'], axis=1)
		saida = df.round(4)
		saida.to_csv("result/metrics-m{}.csv".format(weight), encoding='utf-8',index = False)

		TH1 = df.loc[df['N_THREADS'] == 0]
		objs = TH1['n_obj'].values.tolist()
		CPU1 = TH1['time'].values.tolist()
		
		TH2 = df.loc[df['N_THREADS'] == 2]
		CPU2 = TH2['time'].values.tolist()
		
		TH4 = df.loc[df['N_THREADS'] == 4]
		CPU4 = TH4['time'].values.tolist()
		
		TH8 = df.loc[df['N_THREADS'] == 8]
		CPU8 = TH8['time'].values.tolist()


		graphTime = pd.DataFrame({
			'1 CPU' : CPU1,
			'2 CPU' : CPU2,
			'4 CPU' : CPU4,
			'8 CPU' : CPU8
		})
		
		width = .5
		graphTime.plot(kind='bar', width = width)
		ax = plt.gca()		
		plt.xlim([-width, len(graphTime['1 CPU'])-width])

		objs = list(map(str,objs))
		ax.set_xticklabels((objs))
		ax.set_xlabel('Numero de Objetos')
		ax.set_ylabel('Tempo')
		ax.set_title('Peso da mochila {}'.format(weight))
		plt.savefig('result/graphTime-m{}'.format(weight),transparent=True,bbox_inches='tight')


		spUp1 = TH1['spUp'].values.tolist()
		spUp2 = TH2['spUp'].values.tolist()
		spUp4 = TH4['spUp'].values.tolist()
		spUp8 = TH8['spUp'].values.tolist()


		graphSpeedUp = pd.DataFrame({
			'1 CPU' : spUp1,
			'2 CPU' : spUp2,
			'4 CPU' : spUp4,
			'8 CPU' : spUp8
		})
		
		width = .5
		graphSpeedUp.plot(kind='bar', width = width)
		ax = plt.gca()		
		plt.xlim([-width, len(graphSpeedUp['1 CPU'])-width])

		ax.set_xticklabels((objs))
		ax.set_xlabel('Numero de Objetos')
		ax.set_ylabel('Speed Up')
		ax.set_title('Peso da mochila {}'.format(weight))
		plt.savefig('result/graphSpUp-m{}'.format(weight),transparent=True,bbox_inches='tight')
		
	
		eff1 = TH1['eff'].values.tolist()
		eff2 = TH2['eff'].values.tolist()
		eff4 = TH4['eff'].values.tolist()
		eff8 = TH8['eff'].values.tolist()


		graphEff = pd.DataFrame({
			'1 CPU' : eff1,
			'2 CPU' : eff2,
			'4 CPU' : eff4,
			'8 CPU' : eff8
		})
		
		width = .5
		graphEff.plot(kind='bar', width = width)
		ax = plt.gca()		
		plt.xlim([-width, len(graphEff['1 CPU'])-width])

		ax.set_xticklabels((objs))
		ax.set_xlabel('Numero de Objetos')
		ax.set_ylabel('Eficiencia')
		ax.set_title('Peso da mochila {}'.format(weight))
		plt.savefig('result/graphEff-m{}'.format(weight),transparent=True,bbox_inches='tight')

main()



