import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
import praw


class Tool:
    #connetion to reddit
    def coonect_to_reddit(self):
        user_agent = "Scraper 1.0 bu /u/python"
        reddit = praw.Reddit(
            client_id="4IQsIWyxGdfKEIM7Kn6_7Q",
            client_secret="HW_krwLgogmTeFdlLcroRHu4VHi5Xg",
            user_agent=user_agent
        )
        return user_agent, reddit

    # helper functions
    def plot1(self, df, title, xlabel, ylabel):
        fig, ax = plt.subplots(figsize=(8, 8))
        counts = df.label.value_counts(normalize=True) * 100
        sns.barplot(x=counts.index, y=counts, ax=ax, palette=['red', 'blue', 'green'])
        ax.set_xticklabels(['negative', 'neutral', 'positive'])
        ax.set_ylabel('percentage')
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        plt.show()

    def csvgen(self, df, name_of_file):
        df.to_csv(name_of_file, encoding='utf-8', index=False)

    def nltk(self, headlines):
        nltk.download('vader_lexicon')
        from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

        sia = SIA()
        results = []
        for line in headlines:
            pol_score = sia.polarity_scores(line)
            pol_score['headline'] = line
            results.append(pol_score)
        return results
