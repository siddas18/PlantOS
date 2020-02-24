import os
import kmeans_skl
jpeg_dir=r'C:\Users\Siddharth\Documents\PlantOS\backend\leaf_jpg'
os.chdir(jpeg_dir)

for flower in os.listdir():
    os.chdir(flower)    
    for ftype in os.listdir():
        os.chdir(ftype)
        for img in os.listdir():
            new_name='_'.join([flower,ftype,img.split('.')[0].split('_')[1]])+'.jpg'
            kmeans_skl.leaf_cluster(os.path.join(os.getcwd(),img))
            print('\n' * 10)
        os.chdir('..')
    os.chdir('..')
