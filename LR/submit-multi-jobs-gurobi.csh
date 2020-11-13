#!/bin/tcsh

# Set up python and cplex environment
conda activate /usr/local/usrapps/infews/CAPOW_env
module load gurobi
source /usr/local/apps/gurobi/gurobi810/linux64/bin/gurobi.sh

# Submit multiple jobs at once
@ totalFols = 1

set folNameBase = CA
set scenario = SNP/

@ folNum = 0

while ($folNum < $totalFols)

	set dirName = ${scenario}${folNameBase}${folNum}
   	cd $dirName

    		# Submit LSF job for the directory $dirName
   	bsub -n 8 -R "span[hosts=1]" -W 5000 -o out.%J -e err.%J "python ${folNameBase}_simulation.py"

    	#	bsub -W 5000 -o out.%J -e err.%J "python ${dirNameBase}_simulation.py"

# Go back to upper level directory
    	cd ../..

    	@ folNum = $folNum + 1
end

set scenario = all_tax/

@ folNum = 0

while ($folNum < $totalFols)

	set dirName = ${scenario}${folNameBase}${folNum}
   	cd $dirName

    		# Submit LSF job for the directory $dirName
   	bsub -n 8 -R "span[hosts=1]" -W 5000 -o out.%J -e err.%J "python ${folNameBase}_simulation.py"

    	#	bsub -W 5000 -o out.%J -e err.%J "python ${dirNameBase}_simulation.py"

# Go back to upper level directory
    	cd ../..

    	@ folNum = $folNum + 1
end

set scenario = no_tax/

@ folNum = 0

while ($folNum < $totalFols)

	set dirName = ${scenario}${folNameBase}${folNum}
   	cd $dirName

    		# Submit LSF job for the directory $dirName
   	bsub -n 8 -R "span[hosts=1]" -W 5000 -o out.%J -e err.%J "python ${folNameBase}_simulation.py"

    	#	bsub -W 5000 -o out.%J -e err.%J "python ${dirNameBase}_simulation.py"

# Go back to upper level directory
    	cd ../..

    	@ folNum = $folNum + 1
end

set scenario = CO2/

@ folNum = 0

while ($folNum < $totalFols)

	set dirName = ${scenario}${folNameBase}${folNum}
   	cd $dirName

    		# Submit LSF job for the directory $dirName
   	bsub -n 8 -R "span[hosts=1]" -W 5000 -o out.%J -e err.%J "python ${folNameBase}_simulation.py"

    	#	bsub -W 5000 -o out.%J -e err.%J "python ${dirNameBase}_simulation.py"

# Go back to upper level directory
    	cd ../..

    	@ folNum = $folNum + 1
end

conda deactivate

	
