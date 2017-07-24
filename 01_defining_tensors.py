import tensorflow as tf
import numpy as np

m1 = [[1.0, 0.2], [3.0, 4.0]]
m2 = np.array([[1.0, 2.0],
               [2.0, 4.0]], dtype=np.float32)
m3 = tf.constant([[1.0, 2.0],
                  [3.0, 4.0]])

print type(m1)
print type(m2)
print type(m3)

m1 = tf.convert_to_tensor(m1, dtype=tf.float32)
m2 = tf.convert_to_tensor(m2, dtype=tf.float32)
m3 = tf.convert_to_tensor(m3, dtype=tf.float32)

print ("---------------------------------------")
print type(m1)
print type(m2)
print type(m3)
