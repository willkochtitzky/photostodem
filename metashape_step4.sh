#!/bin/bash
#SBATCH --time=620:00:00
#SBATCH --account=def-copland
#SBATCH --cpus-per-task=32
#SBATCH --mem-per-cpu=24G
#SBATCH --mail-user=<will.kochtitzky@uottawa.ca>
#SBATCH --mail-type=ALL
#SBATCH --job-name="LowDus2_DEM"

#Remove the lock file, if it exists (unlikely it exists, but you don’t want your job to quit because of this)
cd *.files
rm lock
cd ..

metashape.sh -r metashape_DEM.py -platform offscreen
sbatch metashape_step5.sh
