#!/bin/bash

ourPath="/home/paul/Documents/Machine_Learning/Bash_Predictions"

echo -n $PATH | xargs -d : -I {} find {} -maxdepth 1         -executable -type f -printf '%P\n' | sort -u >> $ourPath"/all_commands.txt"

for ourCommand in $(cat $ourPath/"all_commands.txt");
do
	ourTest=$(man $ourCommand | col -b)
	if [ ! -z "${ourTest}" ];
	then
		echo "$ourCommand" >> "$ourPath/possible_commands.txt"
		echo "$ourTest" >> "$ourPath/Man_Notes/$ourCommand.txt"

		echo "Writing out file: $ourCommand";


	fi

done;



rm -rf $ourPath"/all_commands.txt"
