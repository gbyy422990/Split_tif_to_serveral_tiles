#coding:utf-8
#Bin GAO

import os,sys
import numpy as np
import glob
import cv2
from PIL import Image
import scipy.misc


data_path = './output/'

imgs = glob.glob(data_path + '*.tif')
i = 1
for img in imgs:
    print(img)
    midname = img.split('/')[2]

    im = cv2.imread(img)
    im = np.array(im)
    im *= 255
    print(im)
    im1 = Image.fromarray(im)
    im1.save('./gray_image/' + midname)
    i += 1



