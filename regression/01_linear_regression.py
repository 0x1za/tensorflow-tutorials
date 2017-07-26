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

# Create weights
w = tf.Variable(0.0, name='weights')

# Compute loss


