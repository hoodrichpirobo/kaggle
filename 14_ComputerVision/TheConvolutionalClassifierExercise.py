# YOUR_CODE_HERE
pretrained_base.trainable = False

# Check your answer
q_1.check()

from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
    pretrained_base,
    layers.Flatten(),
    # YOUR CODE HERE. Attach a head of dense layers.
    layers.Dense(units = 6, activation = "relu"),
    layers.Dense(units = 1, activation = "sigmoid"),
])

# Check your answer
q_2.check()

# YOUR CODE HERE: what loss function should you use for a binary
# classification problem? (Your answer for each should be a string.)
optimizer = tf.keras.optimizers.Adam(epsilon=0.01)
model.compile(
    optimizer=optimizer,
    loss = "binary_crossentropy",
    metrics=["binary_accuracy"],
)

# Check your answer
q_3.check()

# View the solution (Run this code cell to receive credit!)
# Yes, this one had less overfitting. That means is learning more signal and less noise than the other model. 
# But, since it converges at a loss greater than the other model, is underfitting some, and could have some extra capacity
q_4.check()


