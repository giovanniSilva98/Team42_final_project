"""Example on how to use the graph to command image brightness
to illustrate the sun luminosity and activity short term variability"""
import random as rnd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.animation as animation
from PIL import Image, ImageEnhance,ImageOps
# import os
# import imageio as io
#read the image
# im = Image.open("Assets\\The_Sun_in_high_resolution_pillars.jpg")
# im = Image.open("Assets\\The_sun2.jpg")
#add rotation simulation:
im1 = Image.open("Assets\\sun_seq2\\sun_rot1.PNG")
im2 = Image.open("Assets\\sun_seq2\\sun_rot2.PNG")
im3 = Image.open("Assets\\sun_seq2\\sun_rot3.PNG")
im4 = Image.open("Assets\\sun_seq2\\sun_rot4.PNG")
im5 = Image.open("Assets\\sun_seq2\\sun_rot5.PNG")
# im6 = Image.open("Assets\\sun_seq2\\sun_rot6.PNG")
im7 = Image.open("Assets\\sun_seq2\\sun_rot7.PNG")
im8 = Image.open("Assets\\sun_seq2\\sun_rot8.PNG")


im=[im1,im2,im3,im7,im8,im4,im5]
NUM_IN=len(im)


rnd.shuffle(im)

my_list = [ picture.size for picture in im]
max_tuple = max(my_list, key=lambda tup: tup[1])
EXPECTED_SIZE=[1,2]
EXPECTED_SIZE[0] = max_tuple[0]+500
EXPECTED_SIZE[1] = max_tuple[1]+500
def pad_black(image, size):
    """try to pad with black color"""
    im_out= ImageOps.pad(image, size, color="black", centering=(0.4, 0.5))
    return im_out

im=[pad_black(picture,EXPECTED_SIZE) for picture in im] 
# #solve padding problem
# def padding(img, expected_size):
#     desired_size = expected_size
#     delta_width = desired_size - img.size[0]
#     delta_height = desired_size - img.size[1]
#     pad_width = delta_width // 2
#     pad_height = delta_height // 2
#     padding1 = (pad_width, pad_height, delta_width - pad_width, delta_height - pad_height)
#     return ImageOps.expand(img, padding1)

# def resize_with_padding(img, expected_size):
#     """function for resizing"""
#     img.thumbnail((expected_size[0], expected_size[1]))
#     # print(img.size)
#     delta_width = expected_size[0] - img.size[0]
#     delta_height = expected_size[1] - img.size[1]
#     pad_width = delta_width // 2
#     pad_height = delta_height // 2
#     padding1 = (pad_width, pad_height, delta_width - pad_width, delta_height - pad_height)
#     return ImageOps.expand(img, padding1, fill=0)


# #I want image to have this size:
# #Create list tuple
# my_list = [ picture.size for picture in im]
# max_tuple = max(my_list, key=lambda tup: tup[1])
# EXPECTED_SIZE=max_tuple
# # EXPECTED_SIZE[0] = max_tuple[0]+100
# # EXPECTED_SIZE[1] = max_tuple[1]+100

# im=[resize_with_padding(picture,EXPECTED_SIZE) for picture in im] 
# #brightness enanchement cycle 
seq_factor=[np.arange(0.5,1.5,0.1),np.arange(1.5,0.5,-0.1)]
seq_factor=np.concatenate(seq_factor)

###create "video output"
img_files = []

for i,factor in enumerate(seq_factor):
    im_input=im[i%NUM_IN]
    enhancer = ImageEnhance.Brightness(im_input)
    im_output = enhancer.enhance(factor)
    img_files.append(im_output)
    # print(im_output.size)
# #loop cycle
# for pic in im:
#     #image brightness enhancer
#     enhancer = ImageEnhance.Brightness(im)
#     factor=seq_factor(i%max_bright)

# factor = 1 #gives original image
# im_output = enhancer.enhance(factor)
# im_output0.show()

# factor = 0.5 #darkens the image
# im_output = enhancer.enhance(factor)
# im_output1.show()

# factor = 1.5 #brightens the image
# im_output = enhancer.enhance(factor)
# im_output2.show()





# for factor in seq:  #jist need to insert here the correct factor form the graph
#     im_output = enhancer.enhance(factor)
#     img_files.append(im_output)

# import pylab as pl
# img = None
# for f in files:
#     im=pl.imread(f)
#     if img is None:
#         img = pl.imshow(im)
#     else:
#         img.set_data(im)
#     pl.pause(.1)
#     pl.draw()


# ##ALTERNATIVE WAY
frames = [] # for storing the generated images
fig = plt.figure()
for i,_ in enumerate(img_files):
    frames.append([plt.imshow(img_files[i], cmap=cm.Greys_r,animated=True)])

ani = animation.ArtistAnimation(fig, frames, interval=50, blit=True,
                                repeat_delay=10)
# ani.save('movie.mp4')
plt.show()
ax = plt.gcf()
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)


#NOTE : se si trova una immagine altrettanto bella del sole mentre ruota si
#puo anche ingannare l'occhio (ed esistno queste immagini in effetti ho visto il video)
# https://www.youtube.com/watch?v=l3QQQu7QLoM&ab_channel=NASAGoddard