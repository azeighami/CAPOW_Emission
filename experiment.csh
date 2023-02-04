#!/bin/tcsh

# activate CAPOW environment
conda activate /usr/local/usrapps/infews/group_env
module load gurobi
source /usr/local/apps/gurobi/gurobi810/linux64/bin/gurobi.sh

# Submit multiple jobs at once
@ totalFols = 100

set folder = 1/
set map = UCED/LR/
set scenario = no_tax/
set base = CA

@ folNum = 0

while ($folNum < $totalFols)

	# set dirName = ${map}${scenario}${base}${folNum}
	set dirName = ${base}${folNum}
   	cd $dirName

    	# Submit LSF job for the directory $dirName
   	bsub -n 8 -R "span[hosts=1]" -W 5000 -o out.%J -e err.%J "python CA_simulation.py"

# Go back to upper level directory
    	cd ..

    	@ folNum = $folNum + 1
end

conda deactivate

	
