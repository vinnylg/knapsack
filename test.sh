#!/bin/bash

PAR=./p_knap
SEQ=./knap
DIR=./items/$1
ITEMS=$(ls -v $DIR"mf"*)
DATE="$(date +"%H%M")"
OUT=mochila_final/result.$DATE-
OUT2=mochila_final/pcinfo.$DATE
echo "INFO-PC" >> $OUT2
lscpu | grep CPU* >> $OUT2
lscpu | grep Thread >> $OUT2
lscpu | grep cache >> $OUT2

L2=$(lscpu | grep  L2)
L2=${L2#*: }
L2=${L2%K}

free -m >> $OUT2

echo "Cache memory used: $L2" >> $OUT2

for i in {1..20}
do
	echo "N_THREADS,CHUNK_SIZE,n_obj,max_weight,max_value,time" >> "$OUT$i"
	for ITEM in $ITEMS
	do
		echo "$SEQ $ITEM $OUT$i" 
		time nice -n -20 $SEQ $ITEM >> "$OUT$i"
		echo ""
		for TH in {2,4,8}
		do
			echo $PAR $ITEM $TH $L2 $OUT$i
			time nice -n -20 $PAR $ITEM $TH $L2 >> "$OUT$i"
			echo ""
		done
	done
done
echo "sucess all"
echo ""
