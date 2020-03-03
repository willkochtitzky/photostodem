# This is modified from a python script for Metashape Pro. Scripts repository: https://github.com/agisoft-llc/metashape-scripts

# Modified by Eleanor Bash, updated March 2020

import Metashape

## SET THE FOLLOWING VARIABLES:
project_name = 'Lowell_timelapse' # name to preceed tile number in saved files
tilesX = 2 # set number of tiles in X-direction
tilesY = 2 # set number of tiles in Y-direction
ovrlp = 10 # set percentage overlap between tiles

def isIdent(matrix):
    """
    Check if the matrix is identity matrix
    """
    for i in range(matrix.size[0]):
        for j in range(matrix.size[1]):
            if i == j:
                if matrix[i, j] != 1.0:
                    return False
            elif matrix[i, j]:
                return False
    return True

doc = Metashape.app.document

orig_path = doc.path

chunk = doc.chunk

original_chunk = chunk
temporary_chunks = []

if not chunk.transform.translation:
    chunk.transform.matrix = chunk.transform.matrix
elif not chunk.transform.translation.norm():
    chunk.transform.matrix = chunk.transform.matrix
elif chunk.transform.scale == 1:
    chunk.transform.matrix = chunk.transform.matrix
elif isIdent(chunk.transform.rotation):
    chunk.transform.matrix = chunk.transform.matrix

original_region = chunk.region
r_center = original_region.center
r_rotate = original_region.rot
r_size = original_region.size

x_scale = r_size.x / tilesX
y_scale = r_size.y / tilesY
z_scale = r_size.z

offset = r_center - r_rotate * r_size / 2.

c = 1 # index for saving chunks into new files

for j in range(1, tilesY + 1):  # creating new chunks and adjusting bounding box
    for i in range(1, tilesX + 1):
        new_chunk = chunk.copy(items=[])
        new_chunk.label = "Tile_" + str(i) + "_" + str(j)

        if new_chunk.model:
            new_chunk.model.clear()

        new_region = Metashape.Region()
        new_rot = r_rotate
        new_center = Metashape.Vector([(i - 0.5) * x_scale, (j - 0.5) * y_scale, 0.5 * z_scale])
        new_center = offset + new_rot * new_center
        new_size = Metashape.Vector([x_scale, y_scale, z_scale])
        new_region.size = new_size * (1 + ovrlp / 100)
        new_region.center = new_center
        new_region.rot = new_rot

        new_chunk.region = new_region

        Metashape.app.update()

        doc.save(project_name+new_chunk.label+".psx", chunks=[doc.chunks[c]])
        
        c = c+1

doc.save(orig_path)