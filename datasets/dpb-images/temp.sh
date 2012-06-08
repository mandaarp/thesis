#!/bin/bash
ext=jpg
if [ $# != 4 ]; then
echo "usage: ./auto_copy.sh <prefix> <suffix> <source_path> <destination_path>"
exit
fi

prefix=$1
suffix=$2
source=$3/*.$ext
destination=$4
echo "Copying from $source to $destination ..."

index=`ls -1 $destination | wc -l`
index=`expr $index + 1`
for i in $source;
do cp $i $destination/$prefix$index$suffix.$ext;
index=`expr $index + 1`
done

echo "copied! :)"
