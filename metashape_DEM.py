import Metashape
import glob
import os

#1
#os.chdir('/home/wkoch063/scratch/photos/Ward_Hunt/July15_2019/Ward_Hunt_Lake')#direcotry of all photos and reference info

doc = Metashape.app.document
doc.open(path="./metashape_output_Lowell_Dusty.psx")#This must be .psx
chunk = doc.chunk

# DEM
task = Metashape.Tasks.BuildDem()
task.source_data = Metashape.DataSource.DenseCloudData
task.interpolation = Metashape.Interpolation.DisabledInterpolation
task.projection = chunk.crs
task.network_distribute = True
task.apply(chunk)
doc.save()
