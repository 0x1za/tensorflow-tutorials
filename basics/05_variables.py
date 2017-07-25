import tensorflow as tf

x = tf.constant([[3, 5]], dtype=tf.float32)
y = tf.constant(5, dtype=tf.float32)

op = tf.Variable(x*y, dtype=tf.float32)
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print sess.run(op)

sess.close()