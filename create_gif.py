# Imports the necessary libraries
import imageio.v3 as iio

# Add images to the same folder as this script and then update the filenames list using the names of your images
# I have an example with couple images in the same folder as this script
# PS make sure to use the sizes of the images are the same in order for it to work correctly
filenames = ['1.png', '2.png', '3.png', '4.png']
images = [ ]

# Appends all the images to the images list which was empty
for filename in filenames:
    images.append(iio.imread(filename))
    
# Creates a gif from the images list and saves it as anim.gif
# You can feel free to change the name of the file, duration, and loop parameters
iio.imwrite('anim.gif', images, duration=500, loop=0)

