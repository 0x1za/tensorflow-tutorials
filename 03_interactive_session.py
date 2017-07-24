import tensorflow as tf
"""
Interactive sessions help with creating a session without explicitly using Session before we run ops
"""
sess = tf.InteractiveSession()
x = tf.constant([1, 2], dtype=tf.float32)

print x.eval()

# Don't forget to close the session
sess.close()

