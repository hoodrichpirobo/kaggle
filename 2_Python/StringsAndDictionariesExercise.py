a = ""
length = len(a)
q0.a.check()

b = "it's ok"
length = len(b)
print(length)
q0.b.check()

c = 'it\'s ok'
length = len(c)
print(length)
q0.c.check()

d = """hey"""
length = len(d)
q0.d.check()

e = '\n'
length = len(e)
print(length)
q0.e.check()

def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    return zip_code.isdigit() and len(zip_code) == 5

# Check your answer
q1.check()

def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    ans = []
    for i, token in enumerate(doc_list):
        tokenList = token.split()
        tokenList = [each.rstrip(',.').lower() for each in tokenList]

        if keyword.lower() in tokenList:
            ans.append(i)

    return ans

#    return [i for i in range(len(doc_list)) if(keyword in 
#                                               doc_list[i].replace(","," ").replace(".", " ").
#                                               lower().split())]

# Check your answer
q2.check()

def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.  
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    ans = {}
    for i in range(len(keywords)):
        ans[keywords[i]] = word_search(doc_list, keywords[i])
    return ans

# Check your answer
q3.check()
