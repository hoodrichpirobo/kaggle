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
    # Your code here: Amend the agent!
    import random
    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]
    for move in valid_moves:
        if check_winning_move(obs, config, move, obs.mark):
            return move

    opp_mark = (obs.mark%2)+1
    n = len(valid_moves) - 1

    for i in range(n):
        move = valid_moves[n - i]
        if check_winning_move(obs, config, move, opp_mark):
            return move
            
    return random.choice(valid_moves)

import inspect
import os

def write_agent_to_file(function, file):
    with open(file, "a" if os.path.exists(file) else "w") as f:
        f.write(inspect.getsource(function))
        print(function, "written to", file)

write_agent_to_file(my_agent, "submission.py")

# Check that submission file was created
q_5.check()


