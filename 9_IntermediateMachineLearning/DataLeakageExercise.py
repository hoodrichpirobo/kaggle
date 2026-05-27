# Check your answer (Run this code cell to receive credit!)
# The leather used is indeed the perfect example of data leakage unless you decide at the beginning of the month the amount.
q_1.check()

# Check your answer (Run this code cell to receive credit!)
# Yeah, this avoids the leakage problem as far as I know as long as the leather is ordered before the shoelaces prediction
q_2.check()

# Check your answer (Run this code cell to receive credit!)
# it's fine to me
q_3.check()

# Check your answer (Run this code cell to receive credit!)
# yeah, it's constantly being updated, so it can pose target leakage issue and also since it could be using the test-set data to update the rate this leads to train-test contamination
q_4.check()

# Fill in the line below with one of 1, 2, 3 or 4.
potential_leakage_feature = 2

# Check your answer
q_5.check()

