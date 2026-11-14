<div align="center">

# Intro to Game AI and Reinforcement Learning

**Course 16 of 17 - building Connect Four agents from immediate tactics to adversarial search.**

[![Kaggle](https://img.shields.io/badge/Kaggle-Game%20AI%20and%20Reinforcement%20Learning-20BEFF.svg)](https://www.kaggle.com/learn/intro-to-game-ai-and-reinforcement-learning)
![Status](https://img.shields.io/badge/Status-In%20progress-yellow.svg)
![Exercise exports](https://img.shields.io/badge/Lesson%20exports-3%20of%204-blue.svg)

`OBSERVE → LEGAL MOVES → SIMULATE → EVALUATE → CHOOSE`

[Course Snapshot](#course-snapshot) · [Lessons](#lesson-tracker) · [Tactics](#play-the-game) · [Heuristics](#one-step-lookahead) · [Search](#n-step-lookahead) · [Skills](#skills-practiced) · [Artifacts](#artifacts) · [Next Steps](#next-steps)

</div>

---

## Course Snapshot

| Field | Detail |
|-------|--------|
| Position | Course 16 of 17 |
| Estimated time | 4 hours |
| Status | **In progress - 3 of 4 lesson exercise exports archived** |
| Latest archived lesson | N-Step Lookahead |
| Running environment | Connect Four agents using Kaggle's `obs` and `config` interface |
| Core tools | Python, NumPy, `random`, and `inspect` |
| Work represented | Immediate wins and blocks, legal-move filtering, board simulation, weighted window heuristics, depth-limited adversarial search, and an alpha-beta pruning implementation |
| Repository artifacts | 3 exercise exports; no completion certificate yet |
| Course page | [Kaggle Learn: Intro to Game AI and Reinforcement Learning](https://www.kaggle.com/learn/intro-to-game-ai-and-reinforcement-learning) |

The saved work approaches one problem - choosing a useful move in Connect Four - through immediate tactics, heuristic scoring, and adversarial search. The first agent reacts to immediate wins and threats. The second scores the board after each possible move. The third explores the opponent's replies before choosing.

These exports document the game-search part of the course. Deep Reinforcement Learning remains to be archived; no trained policy or agent evaluation results are saved here yet.

## Lesson Tracker

| # | Lesson | Repository status | Evidence |
|:-:|--------|-------------------|----------|
| 1 | Play the Game | Exercise archived | [PlayTheGameExercise.py](./PlayTheGameExercise.py) |
| 2 | One-Step Lookahead | Exercise archived | [One-StepLookaheadExercise.py](./One-StepLookaheadExercise.py) |
| 3 | N-Step Lookahead | Exercise archived | [N-StepLookaheadExercise.py](./N-StepLookaheadExercise.py) |
| 4 | Deep Reinforcement Learning | Not yet archived | No local exercise export |

The tracker describes the files saved here. Kaggle answer-check calls are preserved in the exports, but their output is not; course completion is not inferred from those calls.

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

## Artifacts

```text
16_IntroToGameAIAndReinforcementLearning/
├── README.md
├── PlayTheGameExercise.py
├── One-StepLookaheadExercise.py
└── N-StepLookaheadExercise.py
```

### Execution context

The Python files preserve solved cells and exploratory work from Kaggle notebooks. They are study references, not complete standalone programs. Kaggle supplies the `q_*` answer-checking objects and surrounding setup; the first exercise also relies on notebook-provided helpers, and the one-step exercise relies on its NumPy import.

To reproduce the work, open [the course on Kaggle](https://www.kaggle.com/learn/intro-to-game-ai-and-reinforcement-learning), run the relevant notebook's setup cells, and use the matching export as a reference.

## Next Steps

- Complete Deep Reinforcement Learning and archive its exercise export.
- Record agent evaluation results before making performance claims.
- Add the completion certificate when earned, then update the root course count.

The overall learning sequence after Kaggle is maintained in the [root roadmap](../README.md#after-kaggle-learn).

---

<div align="center">

[← Geospatial Analysis](../15_GeospatialAnalysis/) · [Back to Roadmap](../README.md) · [Intro to AI Ethics →](https://www.kaggle.com/learn/intro-to-ai-ethics)

*Last updated: November 14, 2026*

</div>
