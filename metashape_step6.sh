#!/bin/bash
#SBATCH --time=8:00:00
#SBATCH --account=def-copland
#SBATCH --cpus-per-task=2
#SBATCH --mem-per-cpu=4G
#SBATCH --mail-user=<will.kochtitzky@uottawa.ca>
#SBATCH --mail-type=ALL
#SBATCH --job-name="LowDus_S6_ex_dem"

#Remove the lock file, if it exists (unlikely it exists, but you don’t want your job to quit because of this)
cd *.files
rm lock
cd ..

metashape.sh -r metashape_export_dem.py -platform offscreen
sbatch metashape_step7.sh
