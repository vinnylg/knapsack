#!/bin/bash
PAR=./p_knap
SEQ=./knap
DIR=./items/
ITEMS=$(ls -v $DIR)
DATE="$(date +"%d%k%M%S")"
OUT=results.$DATE
echo "INFO-PC" >> $OUT
lscpu | grep CPU* >> $OUT
lscpu | grep cache >> $OUT
L2=$(lscpu | grep  L2)
L2=${L2#L*: }
L2=${L2%K}
L3=$(lscpu | grep  L3)
L3=${L3#L*: }
L3=${L3%[[:alpha:]]}

if [ "$1" == "L2" ] 
then
	CACHE=$L2
else 
	CACHE=$L3
fi

free -m >> $OUT

echo ""
echo "----------------------------------------------------------------" >> $OUT
echo "file,N_THREADS,CHUNK_SIZE,n_obj,max_weight,max_value,time" >> $OUT

for ITEM in $ITEMS
do
	echo "$SEQ $ITEM"
	time $SEQ $DIR$ITEM >> $OUT
	echo ""
	for TH in {1..8}
	do
    	  echo "$PAR $ITEM with $TH threads and $CACHE of cache"
    	  time $PAR $DIR$ITEM $TH $CACHE >> $OUT
		echo ""
	done
done
echo "sucess all"
echo ""

