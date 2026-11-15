<div align="center">

# Intro to Game AI and Reinforcement Learning

**Course 16 of 17 - Connect Four agents from immediate tactics to adversarial search and deep reinforcement learning.**

[![Kaggle](https://img.shields.io/badge/Kaggle-Game%20AI%20and%20Reinforcement%20Learning-20BEFF.svg)](https://www.kaggle.com/learn/intro-to-game-ai-and-reinforcement-learning)
![Status](https://img.shields.io/badge/Status-Complete-success.svg)
![Exercise exports](https://img.shields.io/badge/Lesson%20exports-4%20of%204-blue.svg)
[![Certificate](https://img.shields.io/badge/Certificate-November%2015%2C%202026-20BEFF.svg)](./Cux%20Prada%20-%20Intro%20to%20Game%20AI%20and%20Reinforcement%20Learning.png)

`TACTICS → HEURISTICS → ADVERSARIAL SEARCH → LEARNING FROM REWARDS`

[Course Snapshot](#course-snapshot) · [Lessons](#lesson-tracker) · [Tactics](#play-the-game) · [Heuristics](#one-step-lookahead) · [Search](#n-step-lookahead) · [Deep RL](#deep-reinforcement-learning) · [Skills](#skills-practiced) · [Artifacts](#artifacts) · [Certificate](#certificate-of-completion) · [Next Steps](#next-steps)

</div>

---

## Course Snapshot

| Field | Detail |
|-------|--------|
| Position | Course 16 of 17 |
| Estimated time | 4 hours |
| Status | **Complete - November 15, 2026** |
| Latest archived lesson | Deep Reinforcement Learning |
| Running environment | Kaggle ConnectX; `obs` and `config` agents plus a Gym training wrapper |
| Core tools | Python, NumPy, `random`, `inspect`, Kaggle Environments, Gym, PyTorch, and Stable-Baselines3 |
| Work represented | Immediate tactics, weighted board heuristics, three-ply minimax with alpha-beta pruning, reward shaping, and a PPO training setup with a custom CNN |
| Repository artifacts | 4 exercise exports and the completion certificate |
| Course page | [Kaggle Learn: Intro to Game AI and Reinforcement Learning](https://www.kaggle.com/learn/intro-to-game-ai-and-reinforcement-learning) |

The four lessons approach one problem - choosing a useful move in Connect Four - through immediate tactics, heuristic scoring, adversarial search, and learning from rewards. The first agent reacts to immediate wins and threats. The second scores candidate boards. The third explores the opponent's replies. The fourth sets up a neural policy to learn through games against `negamax`.

All four lesson exports and the certificate are archived. The deep RL export records a training configuration and call; trained model weights, training logs, and agent evaluation results are not saved here.

## Lesson Tracker

| # | Lesson | Repository status | Evidence |
|:-:|--------|-------------------|----------|
| 1 | Play the Game | Exercise archived | [PlayTheGameExercise.py](./PlayTheGameExercise.py) |
| 2 | One-Step Lookahead | Exercise archived | [One-StepLookaheadExercise.py](./One-StepLookaheadExercise.py) |
| 3 | N-Step Lookahead | Exercise archived | [N-StepLookaheadExercise.py](./N-StepLookaheadExercise.py) |
| 4 | Deep Reinforcement Learning | Exercise archived | [DeepReinforcementLearningExercise.py](./DeepReinforcementLearningExercise.py) |

The tracker describes the files saved here. The [completion certificate](#certificate-of-completion) establishes course completion; the preserved Kaggle answer-check calls do not include their output.

## Play the Game

[PlayTheGameExercise.py](./PlayTheGameExercise.py) builds a tactical agent around the notebook's `check_winning_move` helper. Its final `my_agent` follows this order:

1. Collect columns whose top cell is empty.
2. Take an immediate winning move if one exists.
3. Otherwise, block an immediate win for the opponent.
4. Choose randomly among legal moves when neither rule applies.

The board arrives as a flattened list. Looking at `obs.board[col]` checks the top cell of a column, while `obs.mark` identifies the current player's pieces. The opponent's mark is `3 - obs.mark`.

The exercise also writes a `submission.py` from function source using `inspect.getsource`. It includes `drop_piece`, `check_winning_move`, and `my_agent`, plus the imports those functions need. That generated submission is not archived in this directory.

The saved reflection identifies the limit of immediate tactics: an opponent can create two winning threats, and blocking one does not remove the other. This motivates evaluating future positions.

## One-Step Lookahead

[One-StepLookaheadExercise.py](./One-StepLookaheadExercise.py) converts the flat observation to a NumPy grid and evaluates the result of every legal move:

```text
Current board
    ↓
Copy the board and drop one piece into each legal column
    ↓
Count useful and threatening windows in each resulting position
    ↓
Compute a weighted score
    ↓
Choose randomly among the highest-scoring columns
```

`drop_piece` copies the grid before placing the piece in the lowest available row. Keeping each simulated board separate prevents one candidate move from changing the evaluation of another.

`count_windows` scans horizontal, vertical, and both diagonal directions. A counted window contains exactly the requested number of a player's pieces and enough empty cells to fill `config.inarow`; mixed-player windows do not qualify.

The saved heuristic uses these weights:

| Window feature | Weight |
|----------------|-------:|
| Own four pieces | `1e6` |
| Own three pieces | `1e3` |
| Own two pieces | `1` |
| Opponent's two pieces | `-1e1` |
| Opponent's three pieces | `-1e2` |

This turns board evaluation into an explicit design decision: wins dominate, opportunities add value, and opposing threats subtract value. The weights are manually chosen. The saved comments about possible win rates are predictions, not benchmark results.

## N-Step Lookahead

[N-StepLookaheadExercise.py](./N-StepLookaheadExercise.py) extends the search to `N_STEPS = 3`. The initial candidate move consumes one step; recursive search examines the opponent's response and the agent's next move.

The minimax structure is:

- **Maximizing turn:** choose the continuation with the highest score for the agent.
- **Minimizing turn:** model the opponent choosing the lowest-scoring continuation for the agent.
- **Leaf evaluation:** stop at the depth limit or a terminal position and evaluate from the original agent's perspective.
- **Alpha-beta pruning:** stop exploring a branch when the current bounds show it cannot improve the decision at an ancestor.

The saved tree-size answer is `7**3`, or 343 leaves, for three levels with seven choices at every level. This is the full branching example; full columns, terminal positions, and pruning can reduce the explored tree.

This exercise uses a different heuristic from the one-step agent:

```python
score = (
    num_threes
    - 1e2 * num_threes_opp
    - 1e4 * num_fours_opp
    + 1e6 * num_fours
)
```

`is_terminal_node` checks a full top row for a draw and scans all four directions for a winning line. The recursive function then uses the heuristic at terminal positions and at the depth limit. The code stores no timing measurements or match results for this agent.

## Deep Reinforcement Learning

[DeepReinforcementLearningExercise.py](./DeepReinforcementLearningExercise.py) moves from manually scoring positions to a neural policy trained through interaction. It wraps Kaggle's ConnectX environment in `ConnectFourGym`, then configures Stable-Baselines3's Proximal Policy Optimization (PPO) with a custom PyTorch feature extractor.

```text
Board observation → Custom CNN → PPO policy → Column choice
        ↑                                         ↓
        └──── New board + reward ← ConnectX vs. negamax
```

### Environment and rewards

The action space is `Discrete(columns)`: one action per column. Observations are integer boards reshaped to `(1, rows, columns)` with values from 0 to 2. Although the wrapper defaults to a random opponent, the saved training setup explicitly selects `agent2="negamax"`.

The implementation assigns these rewards:

| Outcome | Reward | Episode handling |
|---------|-------:|------------------|
| Agent wins (`old_reward == 1`) | `+1` | Uses the environment's terminal flag |
| Any other terminal result after a valid move | `-1` | Ends the episode |
| Valid move with play continuing | `1 / (rows * columns)` | Continues the episode |
| Invalid move into a full column | `-10` | Ends the episode immediately |

The continuing-play reward is `1/42` on a 6 × 7 board; the earlier exercise comment says `1/100`, but `change_reward` defines the behavior used by the wrapper. Its terminal branch does not distinguish a draw from a loss. Full columns remain in the action space: this implementation penalizes invalid choices instead of masking them out.

### Policy and training setup

`CustomCNN` extracts board features with two `3 × 3` convolutions, using 32 then 64 output channels, each followed by ReLU. Flattening and a linear layer produce 128 features. A sample forward pass determines the flattened size before constructing the linear layer.

The saved training configuration is:

```python
policy_kwargs = dict(features_extractor_class=CustomCNN)
model = PPO("CnnPolicy", env, policy_kwargs=policy_kwargs, verbose=0)
model.learn(total_timesteps=50000)
```

The 50,000 timesteps are the requested training budget. The export contains no output confirming how the run finished, no saved checkpoint, and no match evaluation. It documents the environment, reward design, neural feature extractor, and training call without establishing the resulting policy's playing strength.

## Skills Practiced

| Area | Saved work |
|------|------------|
| Agent interface | Read `obs.board` and `obs.mark`; use board dimensions and target line length from `config`; return a column |
| Tactical decisions | Prioritize winning now, then blocking an immediate opposing win |
| State simulation | Reshape a flattened board; copy before mutation; simulate gravity when dropping a piece |
| Heuristic design | Count unblocked windows; weight opportunities and threats; compare candidate scores |
| Adversarial reasoning | Alternate maximizing and minimizing turns; evaluate positions from a fixed player's perspective |
| Search efficiency | Reason about branching growth, depth limits, terminal states, and alpha-beta cutoffs |
| Tie-breaking | Randomly choose among equal-scoring legal moves |
| Submission preparation | Export agent and helper function source into a Kaggle submission file |
| RL environment design | Wrap ConnectX in Gym; define action and observation spaces; handle resets, steps, and terminal states |
| Reward shaping | Assign rewards for wins, continuing play, other terminal results, and invalid actions |
| Neural policy setup | Build a PyTorch CNN feature extractor and connect it to a PPO `CnnPolicy` |
| Training evidence | Distinguish a configured training budget from saved weights, training logs, and measured performance |

## Artifacts

```text
16_IntroToGameAIAndReinforcementLearning/
├── README.md
├── PlayTheGameExercise.py
├── One-StepLookaheadExercise.py
├── N-StepLookaheadExercise.py
├── DeepReinforcementLearningExercise.py
└── Cux Prada - Intro to Game AI and Reinforcement Learning.png
```

### Execution context

The Python files preserve solved cells and exploratory work from Kaggle notebooks. They are study references, not complete standalone programs. Kaggle supplies the `q_*` answer-checking objects and surrounding setup; the first exercise also relies on notebook-provided helpers, and the one-step exercise relies on its NumPy import.

The deep RL export also contains notebook-only syntax (`%matplotlib inline` and `!pip install`) and an unpinned Stable-Baselines3 installation. Its Gym wrapper returns only an observation from `reset()` and a four-item tuple from `step()`. The archive includes no dependency lockfile, so those interfaces and the selected package versions need to be checked together before rerunning training.

To revisit the work, open [the course on Kaggle](https://www.kaggle.com/learn/intro-to-game-ai-and-reinforcement-learning), run the relevant notebook's setup cells, and use the matching export as a reference. Running these exports directly with `python` does not recreate their notebook environment.

## Completion Standard

All four lesson exercise exports and the dated certificate are present.

- [x] Play the Game
- [x] One-Step Lookahead
- [x] N-Step Lookahead
- [x] Deep Reinforcement Learning
- [x] Completion certificate archived

## Certificate of Completion

<div align="center">

<a href="./Cux%20Prada%20-%20Intro%20to%20Game%20AI%20and%20Reinforcement%20Learning.png"><img src="./Cux%20Prada%20-%20Intro%20to%20Game%20AI%20and%20Reinforcement%20Learning.png" width="600" alt="Cux Prada's Intro to Game AI and Reinforcement Learning completion certificate, dated November 15, 2026" /></a>

*Completed November 15, 2026.*

</div>

## Next Steps

- Continue to [Intro to AI Ethics](https://www.kaggle.com/learn/intro-to-ai-ethics), the final course in this repository's Kaggle roadmap.
- For a reproducible agent comparison, preserve package versions, random seeds, trained weights, and win/draw/loss results against named opponents, with games from both player positions.

The overall learning sequence after Kaggle is maintained in the [root roadmap](../README.md#after-kaggle-learn).

---

<div align="center">

[← Geospatial Analysis](../15_GeospatialAnalysis/) · [Back to Roadmap](../README.md) · [Intro to AI Ethics →](https://www.kaggle.com/learn/intro-to-ai-ethics)

*Last updated: November 15, 2026*

</div>
