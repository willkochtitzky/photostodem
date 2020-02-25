import Metashape
import glob
import os

#1
#os.chdir('/home/wkoch063/scratch/photos/Ward_Hunt/July15_2019/Ward_Hunt_Lake')#direcotry of all photos and reference info

doc = Metashape.app.document
doc.open(path="./metashape_output_Lowell_Dusty.psx")#This must be .psx
chunk = doc.chunk

#Dense cloud
task = Metashape.Tasks.BuildDenseCloud()
task.point_colors = True
task.store_depth = True
task.network_distribute = True
task.apply(chunk)
doc.save()
