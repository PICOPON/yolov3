import cv2
import glob
import os
import random


# 从原图集img_save_dir中选取训练集样本数目图片保存到train_imgs_dir中

img_dir = "D://catchbest/ksjshow-dev_gp/x64/MT/Capture/"
img_save_dir = "D://catchbest/ksjshow-dev_gp/x64/MT/new_dataset/imgs"
train_imgs_dir = "D://catchbest/ksjshow-dev_gp/x64/MT/new_dataset/train_imgs"

a = 0
b = 0
outnum_imgs = 300  #抽取训练集数目
def getLength(number):
    Length = 0
    while number != 0:
        Length += 1
        number = number // 10    #关键，整数除法去掉最右边的一位
    return Length


for i in glob.glob(os.path.join(img_save_dir,"*.jpg")):
    temp = random.randint(0,1000)
    if b > outnum_imgs:
        break
    if temp % 4 == 0:
        b += 1
        print(b,"i=",i[-10:])
        temp_mat = cv2.imread(i)
        cv2.imwrite(os.path.join(train_imgs_dir,i[-10:]),temp_mat)
    a += 1
    #print(os.path.basename(i)[:-4])
