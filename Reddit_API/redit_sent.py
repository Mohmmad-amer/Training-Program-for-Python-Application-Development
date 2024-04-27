import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
import praw

#connetion to reddit

user_agent= "Scraper 1.0 bu /u/python"
reddit= praw.Reddit(
    client_id="4IQsIWyxGdfKEIM7Kn6_7Q",
    client_secret="HW_krwLgogmTeFdlLcroRHu4VHi5Xg",
    user_agent=user_agent
)

# helper functions 
def plot1(df):
    fig, ax= plt.subplots(figsize=(8,8))
    counts = df.label.value_counts(normalize=True) * 100
    sns.barplot (x=counts.index, y= counts , ax=ax)
    ax.set_xticklabels (['negative','neutral', 'positive'])
    ax.set_ylabel('percentage')
    plt.show()

def csvgen(df, name_of_file):
    df.to_csv( name_of_file, encoding='utf-8' , index=False)


subreddit=input("enter your subreddit to analys please: ")

print ("analysing your subreddit : " ,subreddit)
headlines= set()
for submission in reddit.subreddit(subreddit).hot(limit=None):
    headlines.add(submission.title)

df= pd.DataFrame(headlines)
csvgen(df, "headlines.csv")

nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
sia= SIA()
results= []
for line in headlines:
    pol_score=sia.polarity_scores(line)
    pol_score['headline']= line
    results.append(pol_score)

df = pd .DataFrame.from_records(results)

df['label']=0
df.loc[df['compound'] > 0.2, 'label']= 1
df.loc[df['compound'] < -0.2, 'label']= -1
df2= df [['headline','label']]

csvgen(df2,"reddit_hedaline_label.csv")
plot1(df)
print("number of headline is = ", len (headlines))
print(df.label.value_counts(normalize=True) * 100)









