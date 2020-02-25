#!/bin/bash
#SBATCH --time=360:00:00
#SBATCH --account=def-copland
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=16G
#SBATCH --mail-user=<will.kochtitzky@uottawa.ca>
#SBATCH --mail-type=ALL
#SBATCH --job-name="LowDus_S3_dense"

#Remove the lock file, if it exists (unlikely it exists, but you don’t want your job to quit because of this)
cd *.files
rm lock
cd ..

metashape.sh -r metashape_dense_cloud.py -platform offscreen
sbatch metashape_setp4.sh

