import Metashape
import glob
import os

#1
#os.chdir('/home/wkoch063/scratch/photos/Ward_Hunt/July15_2019/Ward_Hunt_Lake')#direcotry of all photos and reference info

doc = Metashape.app.document
doc.open(path="./metashape_output_Lowell_Dusty.psx")#This must be .psx
chunk = doc.chunk

# Orthomosaic
task = Metashape.Tasks.BuildOrthomosaic()
task.ortho_surface = Metashape.DataSource.ElevationData
task.resolution = 1
task.projection = chunk.crs
task.fill_holes = False
task.blending_mode = Metashape.BlendingMode.DisabledBlending
task.network_distribute = True
task.apply(chunk)
doc.save()


chunk.exportReport('Lowell_Dusty_July2019_report.pdf')
