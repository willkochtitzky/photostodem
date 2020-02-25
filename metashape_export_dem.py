import Metashape
import glob
import os

#1
#os.chdir('/home/wkoch063/scratch/photos/Ward_Hunt/July15_2019/Ward_Hunt_Lake')#direcotry of all photos and reference info

doc = Metashape.app.document
doc.open(path="./metashape_output_Lowell_Dusty.psx")#This must be .psx
chunk = doc.chunk

#Export
task = Metashape.Tasks.ExportRaster()
task.data_source = Metashape.DataSource.ElevationData

#4-pick resolution in meters
task.resolution = 1
task.path='DEM.tif'
task.apply(chunk)

doc.save()
