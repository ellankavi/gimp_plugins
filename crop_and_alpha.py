#! /usr/bin/env python

import os
from gimpfu import *

def python_crop_and_alpha(image, layer, min_dim):
  pdb.gimp_image_undo_group_start(image)
  
  # 1. apply auto crop
  pdb.plug_in_autocrop(image, layer)

  # 2. remove background
  colormap = pdb.gimp_context_get_background()
  pdb.plug_in_colortoalpha(image, layer, colormap)
  
  # 3. resize image  
  [x_resolution, y_resolution] = pdb.gimp_image_get_resolution(image)
  aspect_ratio = y_resolution/x_resolution
  image_height = pdb.gimp_image_height(image)
  image_width  = pdb.gimp_image_width(image)
  # Assuming that a pixel is a square,
  # 1 cm in x and y directions are the same (require same number of pixels)
  pixels_in_1cm = x_resolution/2.54 # Numer of pixels in 1 cm.
  scale = 1.0
  if image_width < image_height:
    scale = min_dim/image_width
  else:
    scale = min_dim/image_height

  new_width  = image_width  * scale
  new_height = image_height * scale

  pixel_width  = pixels_in_1cm * new_width
  pixel_height = pixels_in_1cm * new_height
  
  pdb.gimp_image_scale(image, pixel_width, pixel_height)

  # 4. Save the image
  image_path_name = pdb.gimp_image_get_filename(image)
  image_path = os.path.dirname(os.path.realpath(image_path_name))
  image_name = image_path_name.split('\\')[-1]
  outputFile = image_name.split('.')[0] + '.png'
  # if the 'gimp_crop_resize' directory does not exist at the current path, create one
  destination_dir   = os.path.join(image_path,'gimp_crop_resize')
  if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)
    
  final_image = os.path.join(destination_dir, outputFile)

  if not os.path.isfile(final_image):
    pdb.file_png_save(image, layer, final_image, final_image,\
      # interlace, compression, save background color, gama, layer offset, save resolution, time 
                      0, 0, 1, 0, 0, 1, 0)



  pdb.gimp_displays_flush()
  pdb.gimp_image_undo_group_end(image)
  pdb.gimp_progress_end()
  return
  

register(
  "python_crop_and_alpha",
  "Crop-alpha-resize",
  "Apply auto crop, remove background, and resize image. Save the image in PNG format.",
  "Ellankavi Ramasamy",
  "Ellankavi Ramasamy",
  "2015",
  "_Crop, alpha, resize and save (py)...",
  "RGB*, GRAY*",
  [
    (PF_IMAGE, "image", "Input image", None),
    (PF_DRAWABLE, "layer", "Input drawable [layer]", None),
    (PF_FLOAT, "min_dim", "Minimim height or width of image [cm]", 10.0),
  ],
  [],
  python_crop_and_alpha, menu="<Image>/Image")

main()
