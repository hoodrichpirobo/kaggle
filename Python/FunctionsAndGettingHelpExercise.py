def round_to_two_places(num):
    """Return the given number rounded to two decimal places. 
    
    >>> round_to_two_places(3.14159)
    3.14
    """
    # Replace this body with your own code.
    # ("pass" is a keyword that does literally nothing. We used it as a placeholder
    # because after we begin a code block, Python requires at least one line of code)
    return round(num, 2)

# Check your answer
q1.check()

# Put your test code here
round(338424, ndigits = -1)

def to_smash(total_candies, n = 3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between n friends, whereas n is 3 by default.
    
    >>> to_smash(91)
    1
    """
    return total_candies % n

# Check your answer
q3.check()

print(round_to_two_places(9.999999)) # I'm kind confused with this one, it rounded only to one place

#nvm i figured the arg was the issue

print(round_to_two_places(9.3874083270493283743890))
print(round(9.3874083270493283743890, 2))

x = -10
y = 5
# Which of the two variables above has the smallest absolute value?
smallest_abs = min(abs(x), abs(y))
print(smallest_abs)

def f(x):
    y = abs(x)
    return y

print(f(-5))
