# coding: utf-8

import xml.etree.ElementTree as ET
import os

names_dict = {}
cnt = 0
f = open('./data/my_data/mydata.names', 'r').readlines()
for line in f:
    line = line.strip()
    names_dict[line] = cnt
    cnt += 1

voc_07 = './data/voc_data/VOCdevkit/VOC2007/'
# voc_12 = '/data/VOCdevkit/VOC2012'

anno_path = [os.path.join(voc_07, 'Annotations')]  # , os.path.join(voc_12, 'Annotations')]
img_path = [os.path.join(voc_07, 'JPEGImages')]  # , os.path.join(voc_12, 'JPEGImages')]

trainval_path = [os.path.join(voc_07, 'ImageSets/Main/train_val.txt')]  # ,
# os.path.join(voc_12, 'ImageSets/Main/trainval.txt')]
test_path = [os.path.join(voc_07, 'ImageSets/Main/test.txt')]

def getLength(number):
    Length = 0
    while number != 0:
        Length += 1
        number = number // 10    #关键，整数除法去掉最右边的一位
    return Length


def parse_xml(path):
    tree = ET.parse(path)
    img_name = path.split('/')[-1][:-4]

    height = int(tree.findtext("./size/height"))
    width = int(tree.findtext("./size/width"))

    objects = []

    for obj in tree.findall('object'):
        difficult = obj.find('difficult').text
        if difficult == '1':
            continue
        name = obj.find('name').text
        bbox = obj.find('bndbox')
        xmin = int(bbox.find('xmin').text)
        ymin = int(bbox.find('ymin').text)
        xmax = int(bbox.find('xmax').text)
        ymax = int(bbox.find('ymax').text)
        xcenter = (xmin+xmax)/2
        ycenter = (ymin+ymax)/2
        bwidth = abs(xmax - xmin)
        bheight = abs(ymax - ymin)
        n_xc = round(xcenter/width,6)
        n_bw = round(bwidth/width,6)
        n_yc = round(ycenter/height,6)
        n_bh = round(bheight/height,6)

        name = str(names_dict[name])
        objects.extend([name,' ',str(n_xc),' ',str(n_yc),' ',str(n_bw),' ',str(n_bh),'\n'])
    if len(objects) > 1:
        return objects
    else:
        return None

def gen_test_txt(txt_path):
    for i, path in enumerate(test_path):
        img_names = open(path, 'r').readlines()
        for img_name in img_names:
            img_name = img_name.strip()
            f = open(txt_path + '/' + img_name + '.txt', 'w')
            xml_path = anno_path[i] + '/' + img_name + '.xml'
            objects = parse_xml(xml_path)
            objects = ''.join(objects)
            f.write(objects)
            f.close()


def gen_train_txt(txt_path):

    for i, path in enumerate(trainval_path):
        img_names = open(path, 'r').readlines()
        for img_name in img_names:
            img_name = img_name.strip()
            f = open(txt_path + '/' + img_name + '.txt', 'w')
            xml_path = anno_path[i] + '/' + img_name + '.xml'
            objects = parse_xml(xml_path)
            objects = ''.join(objects)
            f.write(objects)
            f.close()


gen_train_txt('./data/my_data/train')
gen_test_txt('./data/my_data/test')


