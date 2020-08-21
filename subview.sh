#！/bin/bash

for row in $(seq 1 $4);
do 
	for col in $(seq 1 $4);
	do 
		echo "$row  $col"
		lfptool raw -i $1 --dir-out $2 --imagerep png --recipe-in $3/${row}_${col}.json --image-out --threads 12
		# recipetool perspective-u -i /Users/zhangge/Documents/MATLAB_CV/LF_standford_data/recipe_5x5/${row}_${col}.json -v ${value}

	done
done