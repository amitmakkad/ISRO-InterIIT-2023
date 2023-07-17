# -*- coding: utf-8 -*-
"""bright_image.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11wjAjPrRQl8rbuZp80Is1l85bauJ-exi
"""

import numpy as np
from PIL import Image
from numpy import asarray
import glob
import pandas as pd
import matplotlib.pyplot as plt
from os import path

#img = Image.open('/content/drive/MyDrive/Human_pose_estimation/images/im0001.jpg')
folder_path = '/home/cynaptics/isro/images'
save_path = '/home/cynaptics/isro/dark_removed/hr_train_dark_removed/'
'''
list1 = []
list2 = []
count = 1
'''
count_dark = 0
count_bright = 0
filenames = [filename for filename in glob.glob(folder_path+'/*.png')]

'''
for filename in filenames:
  img = Image.open(filename)
  numpyarray = asarray(img)
  list1.append(count)
  sum = np.sum(numpyarray)
  print(count,' : ',sum,'\n')
  #list2.append(sum)
  count = count + 1
#xpoints = np.array(list1)
#ypoints = np.array(list2)

#plt.plot(ypoints, xpoints)
#plt.show()
'''
c =0
for filename in filenames:
  img = Image.open(filename)
  numpyarray = asarray(img)
  #list1.append(count)
  sum = np.sum(numpyarray)
  if(sum>380000):
  # name, ext = path.splitext(filename.split('/')[-1])
    img.save(save_path + str(c) + '.png')
    c+=1
#print('Dark images count: ',count_dark,' Bright images count: ',count_bright)    
