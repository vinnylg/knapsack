#!/bin/bash
PAR=./p_knap
SEQ=./knap
ITEMS=items/m*
OUT=results.out

echo "INFO-PC---------------------------" >> $OUT
date >> $OUT
lscpu | grep CPU* >> $OUT
lscpu | grep *cache >> $OUT
free -m >> $OUT
echo "END-------------------------------" >> $OUT
echo "$SEQ $ITEM"
$SEQ $ITEM >> $OUT
echo "sucess"

for ITEM in $ITEMS
do
	echo $ITEM
	for TH in {1..8}
	do
    	  echo "$PAR $ITEM $TH"
    	  $PAR $ITEM $TH >> $OUT
    	  echo "sucess"
	done
done
echo "sucess all"

