# YOUR CODE HERE: Define a kernel with 3 rows and 3 columns.
kernel = tf.constant([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0],
])
# Uncomment to view kernel
visiontools.show_kernel(kernel)

# Check your answer
q_1.check()

# YOUR CODE HERE: Give the TensorFlow convolution function (without arguments)
conv_fn = tf.nn.conv2d

# Check your answer
q_2.check()

# YOUR CODE HERE: Give the TensorFlow ReLU function (without arguments)
relu_fn = tf.nn.relu

# Check your answer
q_3.check()

# View the solution (Run this code cell to receive credit!)
# it will return features of vertical lines since the pattern of positive numbers will tell you the kind of features the kernel will extract 
q_4.check()


