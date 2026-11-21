<div align="center">

# Intro to AI Ethics

**Course 17 of 17 - human-centered design, bias, fairness, and model cards.**

[![Kaggle](https://img.shields.io/badge/Kaggle-Intro%20to%20AI%20Ethics-20BEFF.svg)](https://www.kaggle.com/learn/intro-to-ai-ethics)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)
![Lessons](https://img.shields.io/badge/Lessons-5%20of%205-brightgreen.svg)

</div>

## Course Snapshot

| Field | Detail |
|-------|--------|
| Position | Course 17 of 17 |
| Estimated time | 4 hours |
| Status | **Complete - 5 of 5 lessons** |
| Completed | November 20, 2026 |
| Final lesson | Model Cards |
| Repository artifacts | 4 lesson exports and the completion certificate |
| Course page | [Kaggle Learn: Intro to AI Ethics](https://www.kaggle.com/learn/intro-to-ai-ethics) |

> **Repository truth:** the exports hold the written answers and the probes that were run, without their outputs. They need the Kaggle notebooks' data, models, and `q_*` answer checkers to run. Question 2 of [ModelCardsExercise.py](./ModelCardsExercise.py) calls `q_2.hint()` rather than `q_2.check()`.

## Lesson Tracker

| # | Lesson | Status | Evidence |
|:-:|--------|:------:|----------|
| 1 | Introduction to AI Ethics | **Complete** | Tutorial (no exercise) |
| 2 | Human-Centered Design for AI | **Complete** | [Human-CenteredDesignForAIExercise.py](./Human-CenteredDesignForAIExercise.py) |
| 3 | Identifying Bias in AI | **Complete** | [IdentifyingBiasInAIExercise.py](./IdentifyingBiasInAIExercise.py) |
| 4 | AI Fairness | **Complete** | [AIFairnessExercise.py](./AIFairnessExercise.py) |
| 5 | Model Cards | **Complete** | [ModelCardsExercise.py](./ModelCardsExercise.py) |

## Human-Centered Design for AI

One scenario for each of the tutorial's six steps:

| Step | Scenario | Saved answer |
|------|----------|--------------|
| 1. Understand people's needs to define the problem | Reducing plastic waste in the Mekong River System | Watch the people already working on it, interview them, or run focus groups |
| 2. Ask if AI adds value to any potential solution | A camera-based tool to help pathologists review breast-cancer tissue slides | Yes, computer vision could help, if patients' identities are protected in the training images |
| 3. Consider the potential harms that the AI system could cause | A bank's AI flags international transfers, including legitimate ones | Wrongful accusations; add human review, select data carefully, and don't deploy until bias is mitigated |
| 4. Prototype, starting with non-AI solutions | A public health agency's pandemic chatbot | Test a quick non-AI prototype with diverse users first; build the AI version only if it falls short |
| 5. Provide ways for people to challenge the system | A platform's AI removes posts it labels as misinformation | A "dispute" button that sends the case to human review |
| 6. Build in safety measures | Safer autonomous vehicles | All listed measures apply |

## Identifying Bias in AI

The notebook supplies a toxicity classifier: `CountVectorizer` features and `LogisticRegression`, trained on Civil Comments data.

- **Probes:** `"I have a christian friend"` vs `"I have a muslim friend"`, and `"I have a white friend"` vs `"I have a black friend"`, each with the learned word weights printed. Kaggle's feedback gives the expected result: the muslim and black versions are classified as toxic, the others are not. The saved answer blames hateful discussion of those groups in the training data.
- **Bias types named in the saved answers:**

| Scenario | Bias |
|----------|------|
| Training comments about Islam are more often toxic because the source community is islamophobic | Historical |
| Non-English comments are machine-translated and treated as English | Measurement and aggregation |
| A model trained and evaluated on UK users is deployed for an Australian company | Evaluation, representation, and deployment |

## AI Fairness

A decision tree approves or denies credit-card applicants in a synthetic dataset with two groups, A and B. Each model is compared on demographic parity, equal accuracy, and equal opportunity:

| Model | Saved answer |
|-------|--------------|
| Baseline, trained with `Group` | Group B is favored on all three criteria, and the same applicant would be denied as a member of Group A |
| Group-unaware (`Group` dropped) | Fairer, but demographic parity still favors Group B, while equal accuracy and equal opportunity now lean slightly toward Group A |
| Per-group approval thresholds | Almost fixed every criterion except equal opportunity, which got worse |

## Model Cards

The card describes *Simple Zoom*, an AI tool that zooms a camera onto a presenter. It is reviewed by its creator and by the product manager of *Presenter Pro*, a recording product that might integrate it.

| Question | Saved answer |
|----------|--------------|
| Who is the card for? | "Business people and average users with computer access" |
| What problem do you foresee in *Presenter Pro*? | Multiple presenters, handled with a warning in the interface. The hint points to the risk the card actually states: large props can hide the presenter, and *Simple Zoom* isn't suited to hidden presenters. |
| What would you check in the evaluation graphs? | That performance stays equal across demographic groups under different camera angles and lighting |

## Completion Standard

- [x] Introduction to AI Ethics (tutorial)
- [x] Human-Centered Design for AI
- [x] Identifying Bias in AI
- [x] AI Fairness
- [x] Model Cards
- [x] Completion certificate archived
- [x] Root roadmap updated from 16/17 to 17/17

## Takeaway

Dropping a sensitive column doesn't make a model fair, and fairness criteria can conflict, so the criterion a model is held to must be chosen deliberately and documented along with its limits.

## Certificate of Completion

<div align="center">

<a href="./Cux%20Prada%20-%20Intro%20to%20AI%20Ethics.png"><img src="./Cux%20Prada%20-%20Intro%20to%20AI%20Ethics.png" width="600" alt="Intro to AI Ethics certificate, dated November 20, 2026" /></a>

*Completed November 20, 2026.*

</div>

---

<div align="center">

[← Intro to Game AI and Reinforcement Learning](../16_IntroToGameAIAndReinforcementLearning/) · [Back to Roadmap](../README.md) · [After Kaggle Learn →](../README.md#after-kaggle-learn)

</div>
