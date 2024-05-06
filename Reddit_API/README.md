# Sentiment analysis for Reddit
## overview
in this section, I have written a script that connects to Reddit API and takes all hot posts of the subreddit 
and analyze all the posts, and sort them into positive posts, negative posts, and neutral posts. 

# Installation
flow the folowing steps to use the project locally on your computer
1) Clone the repository: use this command to clone the repository 
    git clone https://github.com/Mohmmad-amer/Training-Program-for-Python-Application-Development.git

2) download all the requirements from the requirements.txt file by using this command
   pip install -r <path_for_requirements_file>

*note: make sure you have installed pip if not you can install it using

# Usage
after installing all the flowing you can simply run the main, it will ask you to choose subreddit to anlayz


#### Features
the script has api_tool file that contine tool class wihch hold helper function to show the data that has been collected from the API and analyzed 
I used nltk for the Sentiment Intensity Analyzer
there are 2 forms of results
1) graph that shows you the percentage of each category negtive, postive, and neutral posts 
2) CSV file that has every headline and -1 of the post is negative, 1 if the post are positive, 0 otherwise
and we have more metadata that can be show in the stdout like number of posts etc...