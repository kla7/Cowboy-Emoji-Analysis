# Contributors: Kasey La

# To run this file, type the following into the Shell:
#   python3 scrapeTweets.py

# In order to use this script, you need to first install snscrape and the pandas packages. In your bash Shell (not the python interpreter), run:
#   pip3 install git+https://github.com/JustAnotherArchivist/snscrape.git
#   pip install pandas


# Imports
import os
import pandas


# Query by text search
# Setting variables to be used to format the command below

tweet_count = 1000
search_string = "\U0001F920"
start_date_list = ["2018-01-31", "2019-01-31", "2020-01-31", "2021-01-31", "2022-01-31"]
end_date_list = ["2018-02-01", "2019-02-01", "2020-02-01", "2021-02-01", "2022-02-01"]

count = 0
for x in range(len(start_date_list)):
  os.system("snscrape --jsonl --max-results {} --since {} twitter-search '{} until:{}'> {}-scrape.json".format(tweet_count, start_date_list[x], search_string, end_date_list[x], count))
  
  tweets_dataframe = pandas.read_json('{}-scrape.json'.format(count), lines=True)
  
  if len(tweets_dataframe) == 0 :
    print("Tweet Count of ", search_string, " : 0")
  else:
    tweets_dataframe.to_csv('{}-scrape.csv'.format(count), sep=',', index=False, columns=['date', 'content', 'id', 'url'])
  print("Tweet Count of ", search_string, "in", start_date_list[x], " : ", str(len(tweets_dataframe)))
  count += 1