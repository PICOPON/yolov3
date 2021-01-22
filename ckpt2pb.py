import tensorflow as tf

meta_path = './result_ckpt/model-epoch_490_step_18657_loss_0.6307_lr_1.9914e-05.meta'  # Your .meta file
output_node_names = ["concat_10","concat_11","concat_12"]  # Output nodes

with tf.Session() as sess:
    # Restore the graph
    saver = tf.train.import_meta_graph(meta_path)

    # Load weights
    saver.restore(sess, "./result_ckpt/model-epoch_490_step_18657_loss_0.6307_lr_1.9914e-05")

    # Freeze the graph
    frozen_graph_def = tf.graph_util.convert_variables_to_constants(
        sess,
        sess.graph_def,
        output_node_names)
    print(len(frozen_graph_def.node))
    # Save the frozen graph
    with open('./result_ckpt/output_graph.pb', 'wb') as f:
        f.write(frozen_graph_def.SerializeToString())
