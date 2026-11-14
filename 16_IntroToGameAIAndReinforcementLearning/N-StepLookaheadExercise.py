# imho it would perform worse because scoring three isn't as good as stopping an opponent three score. because it's almost certain 
# that when we score three, the opp will just stop our next move
q_1.hint()

# Fill in the blank
num_leaves = 7**3

# Check your answer
q_2.check()

# Fill in the blank
selected_move = 3

# Check your answer
q_3.check()

# Yeah, it will play the best of the worst possibilities

q_4.hint()

import random
import numpy as np

# Gets board at next step if agent drops piece in selected column
def drop_piece(grid, col, mark, config):
    next_grid = grid.copy()
    for row in range(config.rows-1, -1, -1):
        if next_grid[row][col] == 0:
            break
    next_grid[row][col] = mark
    return next_grid

# Helper function for get_heuristic: checks if window satisfies heuristic conditions
def check_window(window, num_discs, piece, config):
    return (window.count(piece) == num_discs and window.count(0) == config.inarow-num_discs)
    
# Helper function for get_heuristic: counts number of windows satisfying specified heuristic conditions
def count_windows(grid, num_discs, piece, config):
    num_windows = 0
    # horizontal
    for row in range(config.rows):
        for col in range(config.columns-(config.inarow-1)):
            window = list(grid[row, col:col+config.inarow])
            if check_window(window, num_discs, piece, config):
                num_windows += 1
    # vertical
    for row in range(config.rows-(config.inarow-1)):
        for col in range(config.columns):
            window = list(grid[row:row+config.inarow, col])
            if check_window(window, num_discs, piece, config):
                num_windows += 1
    # positive diagonal
    for row in range(config.rows-(config.inarow-1)):
        for col in range(config.columns-(config.inarow-1)):
            window = list(grid[range(row, row+config.inarow), range(col, col+config.inarow)])
            if check_window(window, num_discs, piece, config):
                num_windows += 1
    # negative diagonal
    for row in range(config.inarow-1, config.rows):
        for col in range(config.columns-(config.inarow-1)):
            window = list(grid[range(row, row-config.inarow, -1), range(col, col+config.inarow)])
            if check_window(window, num_discs, piece, config):
                num_windows += 1
    return num_windows

# Helper function for alphabeta: calculates value of heuristic for grid
def get_heuristic(grid, mark, config):
    num_threes = count_windows(grid, 3, mark, config)
    num_fours = count_windows(grid, 4, mark, config)
    num_threes_opp = count_windows(grid, 3, mark%2+1, config)
    num_fours_opp = count_windows(grid, 4, mark%2+1, config)
    score = num_threes - 1e2*num_threes_opp - 1e4*num_fours_opp + 1e6*num_fours
    return score

# Uses alphabeta to calculate value of dropping piece in selected column
def score_move(grid, col, mark, config, nsteps):
    next_grid = drop_piece(grid, col, mark, config)
    score = alphabeta(next_grid, nsteps-1, False, -np.inf, np.inf, mark, config)
    return score

# Helper function for alphabeta: checks if agent or opponent has four in a row in the window
def is_terminal_window(window, config):
    return window.count(1) == config.inarow or window.count(2) == config.inarow

# Helper function for minimax: checks if game has ended
def is_terminal_node(grid, config):
    # Check for draw 
    if list(grid[0, :]).count(0) == 0:
        return True
    # Check for win: horizontal, vertical, or diagonal
    # horizontal 
    for row in range(config.rows):
        for col in range(config.columns-(config.inarow-1)):
            window = list(grid[row, col:col+config.inarow])
            if is_terminal_window(window, config):
                return True
    # vertical
    for row in range(config.rows-(config.inarow-1)):
        for col in range(config.columns):
            window = list(grid[row:row+config.inarow, col])
            if is_terminal_window(window, config):
                return True
    # positive diagonal
    for row in range(config.rows-(config.inarow-1)):
        for col in range(config.columns-(config.inarow-1)):
            window = list(grid[range(row, row+config.inarow), range(col, col+config.inarow)])
            if is_terminal_window(window, config):
                return True
    # negative diagonal
    for row in range(config.inarow-1, config.rows):
        for col in range(config.columns-(config.inarow-1)):
            window = list(grid[range(row, row-config.inarow, -1), range(col, col+config.inarow)])
            if is_terminal_window(window, config):
                return True
    return False

# function alphabeta(node, depth, α, β, maximizingPlayer) is
#     if depth == 0 or node is terminal then
#         return the heuristic value of node
#     if maximizingPlayer then
#         value := −∞
#         for each child of node do
#             value := max(value, alphabeta(child, depth − 1, α, β, FALSE))
#             if value ≥ β then
#                 break (* β cutoff *)
#             α := max(α, value)
#         return value
#     else
#         value := +∞
#         for each child of node do
#             value := min(value, alphabeta(child, depth − 1, α, β, TRUE))
#             if value ≤ α then
#                 break (* α cutoff *)
#             β := min(β, value)
#         return value

# Alphabeta implementation
def alphabeta(node, depth, maximizingPlayer, alpha, beta, mark, config):
    valid_moves = [c for c in range(config.columns) if node[0][c] == 0]
    if depth == 0 or is_terminal_node(node, config):
        return get_heuristic(node, mark, config)
    if maximizingPlayer:
        value = -np.inf
        for col in valid_moves:
            child = drop_piece(node, col, mark, config)
            value = max(value, alphabeta(child, depth-1, False, alpha, beta, mark, config))
            if value >= beta:
                break #beta cutoff
            alpha = max(alpha, value)
        return value
    else:
        value = np.inf
        for col in valid_moves:
            child = drop_piece(node, col, mark%2+1, config)
            value = min(value, alphabeta(child, depth-1, True, alpha, beta, mark, config))
            if value <= alpha:
                break #alpha cutoff
            beta = min(beta, value)
        return value
        
N_STEPS = 3

def my_agent(obs, config):
    # Your code here: Amend the agent!
    import random
    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]
    grid = np.asarray(obs.board).reshape(config.rows, config.columns)
    scores = dict(zip(valid_moves, [score_move(grid, col, obs.mark, config, N_STEPS) for col in valid_moves]))
    max_cols = [key for key in scores.keys() if scores[key] == max(scores.values())]
    return random.choice(max_cols)
