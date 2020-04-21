#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from sklearn.model_selection import train_test_split
import pickle
from keras.utils import to_categorical

IMG_SIZE=100

# DATADIR="C:/Users/vitta/OneDrive/Desktop/CLEANED_DATA"
CATEGORIES =["Splenium of the corpus callosum","Pontine infarct on the right","Lacunar infarcts in the right parietal lobe","Left centrum semi ovale and right parietal lobe","Right cerebellar hemisphere","Right ganglio-capsular region","Right parietal lobe","Right corona radiata","Bilateral cerebellar hemispheres and vermis","Right fronto-parieto-temporo- occipital lobes","Right occipital lobe","Left frontal lobe","Lacunar infarct in left parietal lobe","Left frontal lobe in precentral gyral location","Right thalamus","Brainstem","Lacunar infarct in right putamen","Left fronto-temporo-parietal region","Right insula","Left insula","Bilateral occipital lobes","Right frontal lobe","Left occipital lobe","Left cerebellar lacunar infarcts","Right cerebellar hemisphere infarct","Lacunar infarcts in left corona radiata","Left parietal lobe","Lacunar infarct in dorsal aspect of pons","Lacunar infarct in posterior limb of left internal capsule","Bilateral cerebellar hemispheres","Lacunar infarct in right corona radiata", "Right anterior thalamic infarct","Lacunar infarct in medulla oblongata on the left","Lacunar infarct in pons on the left","Lacunar infarcts in bilateral occipital lobes","Bilateral frontal lobes","Right lentiform nucleus","Right parietal lacunar infarct","Left cerebellar hemisphere","Right fronto-parietal lobe","Left thalamic lacunar infarct","Right temporal lobe","Left fronto-parietal lobe","Medial part of right frontal and parietal lobes","Mid brain on right side","Left occipital and temporal lobes"]
np.save('categories', CATEGORIES)
# training_data=[]
# def create_training_data():
#     for category in CATEGORIES:
#         path=os.path.join(DATADIR,category)
#         class_num= CATEGORIES.index(category)
#
#         for img in os.listdir(path):
#             try:
#                 img_array=cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
#                 new_array=cv2.resize(img_array,(IMG_SIZE,IMG_SIZE))
#                 training_data.append([new_array,class_num])
#             except Exception as e:
#                 pass
#
# create_training_data()
# x2=[]
# y=[]
# for features, label in training_data:
#     x2.append(features)
#     y.append(label)
# #print(y)
# X1= np.array(x2).reshape(-1,IMG_SIZE,IMG_SIZE,1)
#
# #print(X1.shape,Y.shape)
#
# X_test=[]
# X_train=[]
# Y_test=[]
# Y_train=[]
#
# for num in range(50):
#     if (num==7) or (num==22) or (num==28) or (num==44):
#         X_test.append(x2[num])
#         Y_test.append(y[num])
#     else:
#         X_train.append(x2[num])
#         Y_train.append(y[num])
#
# print ( Y_train)
# print ( Y_test)
#
#
# x_train= np.array(X_train).reshape(-1,IMG_SIZE,IMG_SIZE,1)
# x_test= np.array(X_test).reshape(-1,IMG_SIZE,IMG_SIZE,1)
# y_train= np.array(Y_train)
# y_test= np.array(Y_test)
#
#
# #print (X_train.shape, Y_train.shape)
# #print (X_test.shape, Y_test.shape)
#
#
# pickle_out=open("X_train.pickle","wb")
# pickle.dump(x_train,pickle_out)
# pickle_out.close()
#
# pickle_out=open("Y_train.pickle","wb")
# pickle.dump(y_train,pickle_out)
# pickle_out.close()
#
#
# pickle_out=open("X_test.pickle","wb")
# pickle.dump(x_test,pickle_out)
# pickle_out.close()
#
# pickle_out=open("Y_test.pickle","wb")
# pickle.dump(y_test,pickle_out)
# pickle_out.close()
#
#
# # In[ ]:
#
#
# print (Y_train)
#
#
# # In[ ]:




