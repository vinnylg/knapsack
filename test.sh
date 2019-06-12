#!/bin/bash

if [[ $# -eq 0 ]] ; then
    echo 'enter if whats itens do you wanna'
    echo './test.sh [mexp|mlin]'
    exit 1
fi

PAR=./p_knap
SEQ=./knap
DIR=./items/
ITEMS=$(ls -v $DIR$1*)
DATE="$(date +"%H%M%S")"
OUT=results/result.$1.$DATE.cv2
echo "INFO-PC" >> $OUT
lscpu | grep CPU* >> $OUT
lscpu | grep Thread >> $OUT
lscpu | grep cache >> $OUT

L2=$(lscpu | grep  L2)
L2=${L2#*: }
L2=${L2%K}

free -m >> $OUT

echo ""
echo "----------------------------------------------------------------" >> $OUT
echo "Cache memory: $L2" >> $OUT
echo "file,N_THREADS,CHUNK_SIZE,n_obj,max_weight,max_value,time" >> $OUT

	for ITEM in $ITEMS
	do
		echo "$SEQ $ITEM"
		nice -n -20 $SEQ $DIR$ITEM >> $OUT
		echo ""
		for TH in {1..8}
		do
			echo $PAR $DIR$ITEM $TH $L2
			nice -n -20 $PAR $DIR$ITEM $TH $L2 >> $OUT
			echo ""
		done
	done
echo "sucess all"
echo ""

