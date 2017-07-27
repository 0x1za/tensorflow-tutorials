import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# define hyper parameters
lr = 0.01
training_epochs = 100

# Training data
x_train = np.linspace(-1, 1, 100)
y_train = 2 * x_train + np.random.randn(*x_train.shape) * 0.33

# Uncomment the code below to preview the data
# plt.scatter(x_train, y_train)
# plt.show()

# Define data placeholders
X = tf.placeholder("float")
Y = tf.placeholder("float")

# Define the model
def model(X, w):
    return tf.mul(X, w)

# Define the weights
w = tf.Variable(0.0, name="weights")

# Cost function with mean squared error
y_model = model(X, w)
cost = tf.reduce_mean(tf.square(Y-y_model))

# Compute the loss and optimize the parameters
training_op = tf.train.GradientDescentOptimizer(lr).minimize(cost)

# Initialize all variables
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

# Interate over data
for epoch in range(training_epochs):
    for (x, y) in zip(x_train, y_train):
        sess.run(training_op, feed_dict={X:y, Y:y})

sess.close()

