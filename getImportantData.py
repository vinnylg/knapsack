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
    result = result[['N_THREADS','n_obj','max_weight','time']]
    return result

timeSum = 0

def rate_objs_weight(df):
    global timeSum
    objs = df[['n_obj']].values.tolist()
    weights = df[['max_weight']].values.tolist()
    times = df[['time']].values.tolist()
    threads = df[['N_THREADS']].values.tolist()

    objs = np.concatenate(objs, axis = 0)
    weights = np.concatenate(weights, axis = 0)
    times = np.concatenate(times, axis = 0)
    threads = np.concatenate(threads, axis = 0)

    timeSum += sum(times)

    objs = np.array(objs, dtype = np.float)
    weights = np.array(weights, dtype = np.float)
    rate = objs/weights

    list_of_tuples = list(zip(threads,objs,weights,rate,times))

    new_df = pd.DataFrame(list_of_tuples, columns=['N_THREADS','n_obj','max_weight','obj/wgt','time'])

    return new_df

def main():

    global timeSum

    if len(sys.argv) != 3:
        print("./getImportantData <dir> <file*>")
        sys.exit()

    files = read_files(sys.argv[1],sys.argv[2])
    for file in files:
        df = pd.read_csv(file,delimiter=',')
        weights = getWeights(df)
        for weight in weights:
            data = getDataForWeights(df,weight)
            data = data[['N_THREADS','n_obj','time']]
            print(data)
            #data.to_csv("graphs/graph_weight-{}.csv".format(weight), encoding='utf-8',index = False)

    # result = result[['n_obj','max_weight']]

    # n_obj = result['n_obj'].values.tolist()
    # max_weight = result['max_weight'].values.tolist()

    # th = []
    # objs = []
    # weights = []
    # time = []

    # for i in range(len(n_obj)):
    #     #os.system("./createItem mochila_final/mf{}-{} {} {}".format(n_obj[i],max_weight[i],n_obj[i],max_weight[i]))
    #     result = df.loc[(df['n_obj'] == n_obj[i]) & (df['max_weight'] == max_weight[i])]
    #     result = result[['N_THREADS','n_obj','max_weight','time']]
    #     th.append(result['N_THREADS'].values.tolist())
    #     objs.append(result['n_obj'].values.tolist())
    #     weights.append(result['max_weight'].values.tolist())
    #     time.append(result['time'].values.tolist())
        

    # th = np.concatenate(th,axis = 0)
    # objs = np.concatenate(objs,axis = 0)
    # weights = np.concatenate(weights,axis = 0)
    # time = np.concatenate(time,axis = 0)
    # time.all()


    # data_tuple = (list(zip(th,objs,weights,time)))

    # saida = pd.DataFrame(data_tuple,columns=['N_THREADS','n_obj','max_weight','time'])

    # saida.to_csv(sys.argv[1].replace('.csv','_')+'relevantes.csv', encoding='utf-8',index = False)

if __name__== "__main__":
  main()