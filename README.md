# gimp_plugins 
Additional GIMP plugins [custom plug-ins]

## 1. Crop and alpha.py:
When an image file is already loaded in GIMP, it

1. auto-crops the image,
2. removes its background, 
3. resizes the image to a user-defined dimension (maintaining the image's aspect-ratio), and
4. saves the file to a pre-determined folder.

### 1. Installation (Usage) under windows:

`crop_and_alpha.py` is a GIMP python plug-in. In order to use it in GIMP [windows], it just has
to be copied to the plug-ins directory, which is located at 'c:\users\<username>\\.gimp_VER\plug-ins'.

Once copied, the plug-in is under 'Image > Crop, alpha, resize and save (py)...'.

### 2. Usage:

On running the script with an image loaded in GIMP, the script asks the user what the desired minimum
dimension of the resulting image is. For example, if your image is 3cm-by-5cm (width-by-height), the 
minimum dimension is the width. So, when you provide 6 as the minimum dimension, the script scales the
input image such that the minimum dimension in the image meets the user-specified dimension. 

During this scaling, the aspect-ratio of the image is maintained and so is the original resolution of 
the image. So, make sure that the image is not blown-up by a very large amount. This will make the 
resulting image very pixelated.

The background (in case of an input PNG image) is removed and is also auto-cropped.

Once done, the image is saved under 'gimp_crop_resize' folder as a .PNG image.s