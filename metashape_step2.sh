#!/bin/bash
#SBATCH --time=600:00:00
#SBATCH --account=def-copland
#SBATCH --cpus-per-task=16
#SBATCH --mem-per-cpu=8G
#SBATCH --mail-user=<will.kochtitzky@uottawa.ca>
#SBATCH --mail-type=ALL
#SBATCH --job-name="LowDus_S2_depth"

#Remove the lock file, if it exsists (unlikely it exists, but you don't want your job to quit because of this)
cd *.files
rm lock
cd ..

metashape.sh -r metashape_depth_map.py -platform offscreen
sbatch metashape_step3.sh
