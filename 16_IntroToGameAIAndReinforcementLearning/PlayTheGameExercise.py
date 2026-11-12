import random

def agent_q1(obs, config):
    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]
    # Your code here: Amend the agent!
    for move in valid_moves:
        if check_winning_move(obs, config,  move, piece = obs.mark): 
            return move
    return random.choice(valid_moves)
    
# Check your answer
q_1.check()

def agent_q2(obs, config):
    # Your code here: Amend the agent!
    valid_moves = [col for col in range(config.columns) if obs.board[0] == 0]
    for move in valid_moves:
        if check_winning_move(obs, config, move, obs.mark):
            return move

    opp_mark = 2 if (obs.mark == 1) else 1
    for move in valid_moves:
        if check_winning_move(obs, config, move, opp_mark):
            return move
    return random.choice(valid_moves)

# Check your answer
q_2.check()

# Because the winning move might not always be available inmediately, and the opponent can have set up two  ways to win the game 

q_3.hint()

def my_agent(obs, config):
    import random

    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]

    # Win immediately if possible
    for move in valid_moves:
        if check_winning_move(obs, config, move, obs.mark):
            return move

    # Otherwise block the opponent
    opp_mark = 3 - obs.mark

    for move in valid_moves:
        if check_winning_move(obs, config, move, opp_mark):
            return move

    return random.choice(valid_moves)

import inspect

with open("submission.py", "w") as f:
    f.write("import numpy as np\n")
    f.write("import random\n\n")

    for func in (drop_piece, check_winning_move, my_agent):
        f.write(inspect.getsource(func) + "\n\n")

q_5.check()
