# YOUR CODE HERE
image_condense = tf.nn.pool(
    input = image_detect,
    window_shape = (2, 2),
    pooling_type = "MAX",
    strides = (2, 2),
    padding = "SAME"
)

# Check your answer
q_1.check()

# View the solution (Run this code cell to receive credit!)
# none in the end, it only affects in the first iterations
q_2.solution()

# View the solution (Run this code cell to receive credit!)
# Not at all, they seem the same to me, but it seems that it does work for the model to classify the images
# Probably one squares represent a lot for trucks, and other trucks represent a lot for cars
# GlobalAvgPool2D allows us to only focus on highlighted squares instead of having to map raw features to classe
q_3.check()


