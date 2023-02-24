import cv2
import numpy as np

def getOtsuThreshold(im):
    size = 256 
    buckets = np.zeros([size]) 
    image_size = img.shape[0] * img.shape[1]
    
    for index in range(size):
        numberofpixel = np.count_nonzero(img==index)
        buckets[index] = numberofpixel

    in_class_variance_list = []
    
    for i in range(1,size): 
        wf = np.sum(buckets[i:]) / image_size 
        wb = 1-wf 
        mf = np.sum(np.dot(range(i,size),buckets[i:])) / np.sum(buckets[i:])
        mb = np.sum(np.dot(range(i),buckets[:i])) / np.sum(buckets[:i])
        varf = np.sum( np.dot( np.power( range(i, size) - mf, 2 ),buckets[i:size] ) )/ np.sum(buckets[i:])
        varb = np.sum( np.dot( np.power( range(i) - mb, 2 ),buckets[:i] ) )/ np.sum(buckets[:i])
        in_class_variance = varf * wf + varb * wb
        in_class_variance_list.append(in_class_variance)
        
    return in_class_variance_list.index(min(in_class_variance_list))

img = cv2.imread("../doc/images/swan.jpeg") # read to image
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # rgb2gray

print(getOtsuThreshold(img))
