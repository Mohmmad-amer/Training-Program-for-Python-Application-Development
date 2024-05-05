import pandas as pd
from api_tools import Tool


def main():
    # connect to reddit API
    my_tool = Tool()
    user_agent, reddit = my_tool.coonect_to_reddit()

    # choose Subreddit to anlayz
    subreddit = input("enter your subreddit to analys please: ")
    print("analysing your subreddit : ", subreddit)

    # extract all hot headlines
    headlines = set()
    for submission in reddit.subreddit(subreddit).hot(limit=None):
        headlines.add(submission.title)

    df = pd.DataFrame(headlines)
    my_tool.csvgen(df, "headlines.csv")

    # anlayz the headlines for the hot reddit
    results = my_tool.nltk(headlines)

    df = pd.DataFrame.from_records(results)
    df['label'] = 0
    df.loc[df['compound'] > 0.2, 'label'] = 1
    df.loc[df['compound'] < -0.2, 'label'] = -1
    df2 = df[['headline', 'label']]
    my_tool.csvgen(df2, "reddit_hedaline_label.csv")

    # results for the analysis
    my_tool.plot1(df, f"result for {subreddit} subreddit", "posts type", "percentage")
    print("number of headline is = ", len(headlines))
    print(df.label.value_counts(normalize=True) * 100)


if __name__ == "__main__":
    main()
