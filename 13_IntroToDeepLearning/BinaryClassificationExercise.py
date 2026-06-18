from tensorflow import keras
from tensorflow.keras import layers

# YOUR CODE HERE: define the model given in the diagram
model = keras.Sequential([
    layers.BatchNormalization(input_shape = input_shape),
    layers.Dense(256, activation = "relu"),
    layers.BatchNormalization(),
    layers.Dropout(0.3),
    layers.Dense(256, activation = "relu"),
    layers.BatchNormalization(),
    layers.Dropout(0.3),
    layers.Dense(1, activation = "sigmoid"),
])

# Check your answer
q_1.check()

# YOUR CODE HERE
model.compile(
    optimizer = "adam",
    loss = "binary_crossentropy",
    metrics = ["binary_accuracy"],
)

# Check your answer
q_2.check()

# View the solution (Run this cell to receive credit!)
# I think they look great, i think it was a good fit, we can see around 20-25 a clear early stopping to prevent overfitting. 
# Yeah, i think the cross-entropy loss was a good stand-in for accuracy
q_3.check()
