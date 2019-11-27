import sys
import os
import cv2
import glob
src_path = sys.argv[1]
tar_path = sys.argv[2]
if not os.path.exists(tar_path):
    os.makedirs(tar_path)

file_names = sorted(glob.glob(src_path+'/*.png'))
i=0
for file_name in file_names:
    img = cv2.imread(file_name,-1)
    print(img.shape)
    tar_img = cv2.cvtColor(img,cv2.COLOR_BAYER_GB2RGB)
    file_name_parse = file_name.split('/')
    print(file_name_parse)
    newfile_name = tar_path+'/'+file_name_parse[-1]
    print(newfile_name)
    cv2.imwrite(newfile_name,tar_img)
    i+=1
