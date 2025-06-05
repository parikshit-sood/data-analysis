import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

sns.set_theme(style="whitegrid")

df = pd.read_csv("cs188-survey-data.tsv", sep="\t")

responses = df.columns[3:22]
filtered_responses = [col for col in responses if "you're paying attention" not in col]
study_habits = df[filtered_responses]

fig, axes = plt.subplots(6, 3, figsize=(12, 10))
axes = axes.ravel()

for i, column in enumerate(study_habits.columns):
    counts = study_habits[column].value_counts().sort_index()
    counts = counts.reindex(range(1, 6), fill_value=0)  # Fill missing with 0

    title = re.search(r"\[(.*?)\]", column).group(1)

    sns.barplot(
        x=counts.index,
        y=counts.values,
        ax=axes[i],
        hue=counts.index,
        palette=["#2E1065", "#4C1D95", "#7C3AED", "#A855F7", "#C084FC"],
        legend=False,
    )
    axes[i].set_title(title, wrap=True, fontsize=8)
    axes[i].set_xlabel("Response (1-5)", fontsize=8)
    axes[i].set_ylabel("Count", fontsize=8)
    axes[i].tick_params(labelsize=8)

    # Set custom x-axis labels
    axes[i].set_xticks(range(5))  # 0-4 for zero-indexed xtick positions
    axes[i].set_xticklabels(
        ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"],
        rotation=30,
    )

for j in range(len(study_habits.columns), len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()
