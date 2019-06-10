#!/bin/bash
PAR=./p_knap
SEQ=./knap
DIR=./items/
ITEMS=$(ls -v $DIR)
DATE="$(date +"%H%M%S")"
OUT=results.$DATE

if [ "$1" == "L1" ] 
then
	CACHE=$L1
elif [ "$1" == "L2" ]
then 
	CACHE=$L2
else
	CACHE=$L3
fi

echo "INFO-PC" >> $OUT
lscpu | grep CPU* >> $OUT
lscpu | grep Thread >> $OUT
lscpu | grep cache >> $OUT

L1=$(lscpu | grep -m 1 L1)
L1=${L1#*: }
L1=${L1%K}
L2=$(lscpu | grep  L2)
L2=${L2#*: }
L2=${L2%K}
L3=$(lscpu | grep  L3)
L3=${L3#*: }
L3=${L3%[[:alpha:]]}

CACHES=($L3 $L2 $L1)

free -m >> $OUT

echo ""
echo "----------------------------------------------------------------" >> $OUT
echo "Cache memory: $CACHE" >> $OUT
echo "file,N_THREADS,CHUNK_SIZE,n_obj,max_weight,max_value,time" >> $OUT

for i in {0..2}
do
	for ITEM in $ITEMS
	do
		echo "$SEQ $ITEM"
		time $SEQ $DIR$ITEM >> $OUT
		echo ""
		for TH in {1..8}
		do
			echo $PAR $DIR$ITEM $TH ${CACHES[$i]}
			time $PAR $DIR$ITEM $TH ${CACHES[$i]} >> $OUT
			echo ""
		done
	done
done
echo "sucess all"
echo ""

