#!/bin/bash

PAR=./p_knap
SEQ=./knap
DATE="$(date +"%H%M")"

L2=$(lscpu | grep  L2)
L2=${L2#*: }
L2=${L2%K}

L2=132

for subdir in {0,1}
do
	OUT=mochila_final/$subdir/result-

	if [ $subdir -eq 0 ]
	then
		knapsacks=(100000 200000 400000 800000)
	else
		knapsacks=(30000 60000 120000 240000)
	fi

	for i in {1..20}
	do
		DIR=./items/$subdir/
		for knapsack in "${knapsacks[@]}"
		do
			echo "N_THREADS,CHUNK_SIZE,n_obj,max_weight,max_value,time" > "$OUT$i-m$knapsack"
			ITEMS=$(ls -v $DIR"mf$knapsack"*)
			for ITEM in $ITEMS
			do
				echo "$SEQ $ITEM $OUT$i-m$knapsack" 
				time nice -n -20 $SEQ $ITEM >> "$OUT$i-m$knapsack"
				echo ""
				for TH in {2,4,8}
				do
					echo $PAR $ITEM $TH $L2 $OUT$i-m$knapsack
					time nice -n -20 $PAR $ITEM $TH $L2 >> "$OUT$i-m$knapsack"
					echo ""
				done
			done
		done
	done
done
	echo "sucess all"
echo ""
