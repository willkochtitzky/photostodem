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
task.data_source = Metashape.DataSource.OrthomosaicData
#4-pick resolution in meters
task.resolution = 0.5 #For geographic coordinate systems, you made need to use resoultion_x and _y (DEM too)
task.path='Orthomosaic2.tif'
task.apply(chunk)

doc.save()
