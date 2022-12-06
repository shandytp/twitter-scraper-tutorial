import snscrape.modules.twitter as sntwitter
import pandas as pd
from tqdm import tqdm

def scrape_tweets(query, num_of_tweet):
    """
    Function untuk melakukan scrape twitter dengan library snscrape

    Parameters
    ----------
    query (string): parameter untuk advanced search dari twitter
    num_of_tweet (int): jumlah tweets yang ingin di scraping
    
    Returns
    -------
    result_df (DataFrame): hasil scrape dalam bentuk dataframe
    """
    # Creating list to append tweet data to
    tweets = []

    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i,tweet in enumerate(tqdm(sntwitter.TwitterSearchScraper(query).get_items())):
        if i > num_of_tweet:
            break
        tweets.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
        
    # Creating a dataframe from the tweets list above
    result_df = pd.DataFrame(tweets, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

    return result_df