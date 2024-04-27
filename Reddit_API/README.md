## Sentiment analysis for Reddit
in this section, I have written a script that connects to Reddit API and takes all hot posts of the subreddit 
and analyze all the posts, and sort them into positive posts, negative posts, and neutral posts. 

# whats in the script
the script has to helper function to show the data that has been collected from the API and analyzed 
I used nltk for the Sentiment Intensity Analyzer
there are 2 forms of data
1) graph that shows you the percentage of each category 
2) CSV file that has every headline and -1 of the post is negative, 1 if the post are positive, 0 otherwise
and we have more metadata that can be show in the stdout like number of posts etc...

## how to run it
you should make sure you have all the library in your system if not please download using 
pip install 
then just run the script, it will ask you what subreddit you would like to analyze and then wait few seconds and you will have 2 CSV files and the graph of the analysis