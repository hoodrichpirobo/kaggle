# YOUR CODE HERE
input_shape = [red_wine.shape[1] - 1]

# Check your answer
q_1.check()

from tensorflow import keras
from tensorflow.keras import layers

# YOUR CODE HERE
model = keras.Sequential([
    layers.Dense(units = 1, input_shape = input_shape)
])

# Check your answer
q_2.check()

# YOUR CODE HERE
w, b = model.weights
print("Weights/n{}\n\nBias\n{}".format(w, b))

# Check your answer
q_3.check()


