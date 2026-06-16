# View the solution (Run this cell to receive credit!)
# I would say this model is underfitting since there's not much gap between them and validation loss never increases
q_1.check()

# View the solution (Run this cell to receive credit!)
# that's overfitting because the val_loss starts to go up back again
q_2.check()

from tensorflow.keras import callbacks


# YOUR CODE HERE: define an early stopping callback
early_stopping = callbacks.EarlyStopping(
    min_delta = 0.001,
    patience = 5,
    restore_best_weights = True
)

# Check your answer
q_3.check()

# View the solution (Run this cell to receive credit!)
# Although, the overfitted model had lower training loss, the model with the best validation loss is the one with early stopping
q_4.check()
