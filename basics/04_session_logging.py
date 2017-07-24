import tensorflow as tf
"""
The ConfigProto protocol buffer exposes various configuration options for a session. 
For example, to create a session that uses soft constraints for device placement, and log the resulting placement decisions
"""
x = tf.constant([[1, 2]], dtype=tf.float32)
neg_x = tf.neg(x)

with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as sess:
    print sess.run(neg_x)