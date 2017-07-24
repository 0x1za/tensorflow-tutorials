import tensorflow as tf
import numpy as np

# Create 1x2 matrix
x = tf.constant([[1, 2]], dtype=tf.float32)

# Negate it
neg_x = tf.neg(x, name="neg_x")

with tf.Session() as sess:
    print sess.run(neg_x)
