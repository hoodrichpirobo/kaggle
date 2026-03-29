def prettify_graph(graph):
    """Modify the given graph according to Jimmy's requests: add a title, make the y-axis
    start at 0, label the y-axis. (And, if you're feeling ambitious, format the tick marks
    as dollar amounts using the "$" symbol.)
    """
    graph.set_title("Results of 500 slot machine pulls")
    graph.set_ylim(ymin = 0)
    graph.set_ylabel("Balance")
    graph.yaxis.set_major_formatter('${x:,.0f}')
    # ticks = graph.get_yticks()
    # new_labels = ['${}'.format(int(amt)) for amt in ticks]
    # graph.set_yticklabels(new_labels)
    # graph.set_yticks("$")

graph = jimmy_slots.get_graph()
prettify_graph(graph)
graph

# type(graph)
# dir(graph)
# help(graph)
# help(graph.set_ylim)
# help(graph.set_ylabel)
# help(graph.set_yticklabels)
#help(graph.set_yticks)

# Import luigi's full dataset of race data
from learntools.python.luigi_analysis import full_dataset

# Fix me!
def best_items(racers):
    winner_item_counts = {}
    for i in range(len(racers)):
        # The i'th racer dictionary
        racer = racers[i]
        # We're only interested in racers who finished in first
        if racer['finish'] == 1:
            for j in racer['items']:
                # Add one to the count for this item (adding it to the dict if necessary)
                if j not in winner_item_counts:
                    winner_item_counts[j] = 0
                winner_item_counts[j] += 1

        # Data quality issues :/ Print a warning about racers with no name set. We'll take care of it later.
        if racer['name'] is None:
            print("WARNING: Encountered racer with unknown name on iteration {}/{} (racer = {})".format(
                str(i+1), str(len(racers)), str(racer['name']))
                 )
    return winner_item_counts

# Try analyzing the imported full dataset
# full_dataset
best_items(full_dataset)

def countHand(hand):
    ansHand = 0
    # aces = []
    aces = 0
    for each in hand:
        if each == 'J' or each == 'Q' or each == 'K':
            ansHand += 10
        elif each == 'A':
            # aces.append(each)
            aces += 1
        else:
            ansHand += int(each)
    for i in range(aces):
        ansHand = ansHand + 1 if ansHand + 11 > 21 else ansHand + 11
#        if ansHand + 11 > 21:
#            ansHand += 1
#        else:
#            ansHand += 11

    return ansHand

def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    firstHand = countHand(hand_1)
    secondHand = countHand(hand_2)
    return firstHand <= 21 and (firstHand > secondHand or secondHand > 21)

#    if firstHand <= 21:
#        if firstHand > secondHand or secondHand > 21:
#            return True
#        else:
#            return False
#    else:
#        return False

# Check your answer
q3.check()
