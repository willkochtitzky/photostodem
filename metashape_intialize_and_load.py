import Metashape
import glob
import os

#THINGS YOU NEED TO CHANGE IN THIS DOCUMENT
#1. Where are all of your files?
#2. Do you have a mask?
#3. Where are your locations for each photo?

#MAKE SURE your columes in the csv file at the name, x, y, and then z (double check x and y are not flipped)

#In each other document you might change the path to the directory you are working in

#You might need to change the output resolution for our DEM and orthomosaic (different file)
#4. What resolution DEM and orthomosaic do you want?

doc = Metashape.app.document
doc.save(path="./metashape_output_Lowell_Dusty.psx") #This must be .psx
#                   ^this name must match on all other python documents



photo_file_names = glob.glob('DSC*') #pull all photos in the current dir into the model

#Add photos and reference data
chunk = doc.addChunk()
chunk.addPhotos([photo_file_names])
chunk.crs = Metashape.CoordinateSystem("EPSG::3714")#EDIT EPSG CODE HERE

#2
#chunk.importMasks(path='Ward_Hunt_July28_mask.jpg')#Only need this line if you need to mask the photos
#you would only mask if the aircraft is in the photo (mask is the same for all photos)

#import reference data
task = Metashape.Tasks.ImportReference()
task.columns='nxyz'
task.delimiter = ","

#3
task.path = 'processed_data_export_UTM.csv'
task.skip_rows=1
task.apply(chunk)

# Match photos
task = Metashape.Tasks.MatchPhotos()
task.downscale = Metashape.Accuracy.HighAccuracy
task.keypoint_limit = 70000
task.tiepoint_limit = 0
task.preselection_generic = True
task.preselection_reference = True
task.network_distribute = True
task.apply(chunk)

#Align cameras
task = Metashape.Tasks.AlignCameras()
task.adaptive_fitting = True
task.network_distribute = True
task.apply(chunk)

#Optimize Cameras
task = Metashape.Tasks.OptimizeCameras()
task.fit_f = True
task.fit_cx = True
task.fit_cy = True
task.fit_b1 = True
task.fit_k1 = True
task.fit_k2 = True
task.fit_k3 = True
task.fit_k4 = True
task.fit_p1 = True
task.fit_p2 = True
task.fit_p3 = True
task.fit_p4 = True
task.adaptive_fitting = True
task.tiepoint_covariance = True
task.apply(chunk)

doc.save()
