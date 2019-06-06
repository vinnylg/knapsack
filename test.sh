#!/bin/bash
PAR=./p_knap
SEQ=./knap
ITEM=items/m16_160K
OUT=results.out
CPU_GREP=(processor,model\ name,cpu\ MHz,cache\ size,cpu\ cores)


echo "INFO-PC---------------------------" >> $OUT
date >> $OUT
lscpu >> $OUT
free -m >> $OUT
echo "END-------------------------------" >> $OUT
echo "$SEQ $ITEM"
$SEQ $ITEM >> $OUT
echo "sucess"

for TH in {1..8}
do
    echo "$PAR $ITEM $TH"
    $PAR $ITEM $TH >> $OUT
    echo "sucess"
done

echo "sucess all"
    

