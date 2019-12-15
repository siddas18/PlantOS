import matplotlib.pyplot as plt
import numpy as np
from cv2 import imread, cvtColor, COLOR_BGR2RGB
from sklearn.cluster import KMeans
from scipy.ndimage.morphology import binary_fill_holes,binary_dilation
from time import time
t0=time()
img=imread('images/img_2143.jpg')
img=cvtColor(img, COLOR_BGR2RGB)
width=img.shape[1]
height=img.shape[0]
img=img.reshape(width*height,3)
kmeans = KMeans(n_clusters=2, random_state=0).fit(img)
labels=kmeans.labels_.reshape(height,width)
label1=1-binary_fill_holes(labels == 0).astype(int)
label2=binary_fill_holes(labels == 1).astype(int)
img=img.reshape(height,width,3)

cluster1=img.copy()
cluster2=img.copy()
cluster1[(labels * label1).astype(bool)] = np.asarray([0,0,0])
cluster2[((1-labels) * (1-label1)).astype(bool)] = np.asarray([0,0,0])
img[labels==1] = np.asarray([0,0,0])
#cluster2[label2] = np.asarray([0,0,0])
#cluster2=binary_dilation(cluster2)
#ret, thresh = cv2.threshold(img,0,255,6)
plt.figure()
plt.axis('off')
plt.imshow(cluster1)
#plt.imshow(thresh)
plt.show()
t1=time()
print("Time elapsed :",t1-t0,"seconds.")