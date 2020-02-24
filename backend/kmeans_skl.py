import matplotlib.pyplot as plt
import cv2
from sklearn.cluster import KMeans
from time import time
import func_def

def leaf_cluster(input_img):
    t0=time()
    img=cv2.imread(input_img)
    img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img=cv2.resize(img,(640,480),interpolation = cv2.INTER_AREA)
    width=img.shape[1]
    height=img.shape[0]
    
    img=img.reshape(width*height,3)
    kmeans = KMeans(n_clusters=2, random_state=0).fit(img)
    labels=kmeans.labels_.reshape(height,width)
    img=img.reshape(height,width,3)
    cluster=func_def.fill_holes(img.copy(),labels)
    
    plt.figure()
    plt.axis('off')
    plt.imshow(cluster)
    plt.show()
    t1=time()
    print("Time elapsed :",t1-t0,"seconds.")