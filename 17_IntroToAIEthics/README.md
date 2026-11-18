# Intro to AI Ethics

**Course 17 of 17 · In progress · 4 hours estimated**

[Repository roadmap](../README.md#roadmap) · [Course on Kaggle Learn](https://www.kaggle.com/learn/intro-to-ai-ethics/course)

Would a toxicity classifier change its prediction about an ordinary sentence if you changed just one word describing a person? The saved exercise uses that question to explore how a model can pick up associations between identity and toxicity.

## Lesson tracker

| # | Lesson | What you can find here |
|:-:|--------|------------------------|
| 1 | Introduction to AI Ethics | Opening tutorial on Kaggle. |
| 2 | Human-Centered Design for AI | [Empty exercise file](./Human-CenteredDesignForAIExercise.py). |
| 3 | Identifying Bias in AI | [Saved exercise cells and written responses](./IdentifyingBiasInAIExercise.py). |
| 4 | AI Fairness | Fairness criteria for a credit approval model. Exercise export pending. |
| 5 | Model Cards | Documenting a model's uses and limitations. Exercise export pending. |

The course certificate is pending.

## Inside the bias exercise

The exercise uses the sentence `"I have a ___ friend"`. It gives `christian` and `muslim` as one pair of substitutions, and `white` and `black` as another. The surrounding words stay the same, so any change in the prediction can be traced to the substitution. The saved cells call `classify_string` and look up the coefficients for the words in each input.

The written responses consider how hostile language in historical training data could influence a classifier. They also discuss measurement and aggregation bias across languages, whose data is represented, how the model is evaluated, and where it is deployed.

**To try the comparison**, run the setup cells in the Kaggle notebook, then change one term at a time and compare the printed predictions with the word coefficients. The notebook supplies the classifier, the `coefficients` table, and the answer checks. [Open the bias exercise on Kaggle](https://www.kaggle.com/code/alexisbcook/exercise-identifying-bias-in-ai).
