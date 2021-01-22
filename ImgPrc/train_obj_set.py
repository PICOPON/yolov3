import os
import glob
import cv2

#  orginal_train_img_dir 图片中选取已经标记的图片存储到JPEGImages/*.jpg
#  根据已标记的图片写入train_txt
#  抽取训练样本集

base_dir = "./data/voc_data/VOCdevkit/VOC2007/ImageSets/Main/"
orginal_train_img_dir = "./data/voc_data/VOCdevkit/VOC2007/original_train_Imgs/"

voc_img_xml_dir = "./data/voc_data/VOCdevkit/VOC2007/Annotations/"
voc_img_dir = "./data/voc_data/VOCdevkit/VOC2007/JPEGImages/"

train_num = 180

train_loop = 0

# 3.写入已标记的图片xml到train_txt
'''
with open(base_dir + "train_val.txt", "w") as f:
    for i in glob.glob(os.path.join(voc_img_xml_dir,"*.xml")):
        train_loop += 1
        print(train_loop)
        f.write(i[-10:-4] + "\n")

num_train = 0
num_test = 0
# 4.随机抽取验证样本数。。。
# 。。。。
# 5.显示train_txt 和val_txt样本数
with open(base_dir + "train_val.txt", "r") as f:
    while True:
        line = f.readline()
        if line:
            pass
        else:
            break
        num_train += 1
    print("train_val:", num_train)
with open(base_dir + "test.txt", "r") as f:
    while True:
        line = f.readline()
        if line:
            pass
        else:
            break
        num_test += 1
    print("test:", num_test)
# 1. 标记图片
# 2. 从原训练图集选出已标记的图片

for i in glob.glob(os.path.join(voc_img_xml_dir,"*.xml")):
    train_loop += 1
    print("{0} loop".format(train_loop))
    img = cv2.imread(os.path.join(orginal_train_img_dir,i[-10:-4]+".jpg"))
    cv2.imwrite(os.path.join(voc_img_dir,i[-10:-4]+".jpg"),img)
'''

with open(base_dir + "train_val.txt", "w") as f:
    for i in glob.glob(os.path.join(voc_img_xml_dir,"*.xml")):
        print(i[-10:-4])
        f.write(i[-10:-4]+"\n")
