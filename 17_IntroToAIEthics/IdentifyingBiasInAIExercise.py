# Comment to pass through the model
# my_comment = "I love apples"
# my_comment = "Apples are stupid"
# my_comment = "The consequences of the industrial revolution have been disastrous for mankind"

my_comment = "Apples are lame bollocks"

# Do not change the code below
classify_string(my_comment)
q_1.check()

# Check your answer (Run this code cell to get credit!)
# nope, they all seem to make sense imho

q_2.check()

# Set the value of new_comment
# new_comment = "I have a christian friend"
new_comment = "I have a muslim friend"

# Do not change the code below
classify_string(new_comment)
coefficients[coefficients.word.isin(new_comment.split())]
q_3.check()

# Set the value of new_comment
# new_comment = "I have a christian friend"
# new_comment = "I have a muslim friend"
# new_comment = "I have a white friend"
new_comment = "I have a black friend"

# Do not change the code below
classify_string(new_comment)
coefficients[coefficients.word.isin(new_comment.split())]
q_3.check()

# Check your answer (Run this code cell to get credit!)
# that might be because usually when people talk about blacks and muslims they usually do it on a hateful way
# training the model in a biased way

q_4.check()

# Check your answer (Run this code cell to get credit!)

# It can make my model islamophobic too, creating a historical biased due to the online community hate against muslims

q_5.check()

# Check your answer (Run this code cell to get credit!)

# Measurement bias and also aggregation bias, each language should be treated in their own way

q_6.check()

# Check your answer (Run this code cell to get credit!)

# evaluation bias and representation bias, while also introducing deployment bias

q_7.check()


