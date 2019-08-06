#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 02:24:27 2019

@author: gp
"""
import numpy as np
import matplotlib.pyplot as plt
import cv2
bl_img = np.zeros((2,2),np.uint8)
img = cv2.imread('DATA/sammy.jpg')
plt.imshow(img)
plt.show()

sift = cv2.xfeatures2d.SIFT_create()