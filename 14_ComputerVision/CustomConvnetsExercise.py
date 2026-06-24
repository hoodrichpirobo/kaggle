from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
    # Block One
    layers.Conv2D(filters=32, kernel_size=3, activation='relu', padding='same',
                  input_shape=[128, 128, 3]),
    layers.MaxPool2D(),

    # Block Two
    layers.Conv2D(filters=64, kernel_size=3, activation='relu', padding='same'),
    layers.MaxPool2D(),

    # Block Three
    # YOUR CODE HERE
    layers.Conv2D(filters = 128, kernel_size = 3, activation = "relu", padding = "same"),
    layers.Conv2D(filters = 128, kernel_size = 3, activation = "relu", padding = "same"),
    layers.MaxPool2D(),

    # Head
    layers.Flatten(),
    layers.Dense(6, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(1, activation='sigmoid'),
])

# Check your answer
q_1.check()

model.compile(
    optimizer=tf.keras.optimizers.Adam(epsilon=0.01),
    # YOUR CODE HERE: Add loss and metric
    loss = "binary_crossentropy",
    metrics = ["binary_accuracy"]
)

# Check your answer
q_2.check()

# View the solution (Run this code cell to receive credit!)
# Although it overfits still, it's a little bit better than the one from the tutorial
# This was done because eventhough we added an additional layer, it was controlled better due to the Dropout layer
q_3.check()


