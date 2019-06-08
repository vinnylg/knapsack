#!/bin/bash
PAR=./p_knap
SEQ=./knap
ITEMS=items/m*
DATE="$(date +"%d%k%M%S")"
OUT=results.$DATE
echo "INFO-PC" >> $OUT
lscpu | grep CPU* >> $OUT
# CACHE=$(lscpu | grep  L2)
# CACHE=${CACHE#L*: }
# CACHE=${CACHE%K}
CACHE=$(lscpu | grep  L3)
CACHE=${CACHE#L*: }
CACHE=${CACHE%[[:alpha:]]}
echo "Cache L3 $CACHE K" >> $OUT
free -m >> $OUT


for ITEM in $ITEMS
do
	echo "$SEQ $ITEM"
	$SEQ $ITEM >> $OUT
	echo "sucess"

	for TH in {1..8}
	do
    	  echo "$PAR $ITEM $TH "
    	  $PAR $ITEM $TH $CACHE >> $OUT
    	  echo "sucess"
	done
done
echo "sucess all"

