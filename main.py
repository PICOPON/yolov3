import tensorflow as tf
import argparse
import cv2
import numpy as np
from utils.data_aug import letterbox_resize
from tensorflow.python.platform import gfile


img_ori = cv2.imread("./test_imgs/1.jpg")
img, resize_ratio, dw, dh = letterbox_resize(img_ori, 416, 416)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = np.asarray(img, np.float32)
img = img[np.newaxis, :] / 255.

sess = tf.Session()
with gfile.FastGFile('./result_ckpt/output_graph.pb', 'rb') as f: #加载模型
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    sess.graph.as_default()
    tf.import_graph_def(graph_def, name='')  # 导入计算图

# 需要有一个初始化的过程
sess.run(tf.global_variables_initializer())

# 需要先复原变量
# 1

#下面三句，是能否复现模型的关键
# 输入
input = sess.graph.get_tensor_by_name('input_data:0')  #此处的x一定要和之前保存时输入的名称一致！
op = sess.graph.get_tensor_by_name('concat_10:0')  #此处的op_to_store一定要和之前保存时输出的名称一致！

ret = sess.run(op, feed_dict={input: img})
print(ret)
# 输出 26