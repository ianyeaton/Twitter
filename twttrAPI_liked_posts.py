import requests
import os
import json
import pandas as pd
import sqlalchemy as db
from IPython.display import display

# Set the environment variables before hand in the terminal with this line of code:
# export 'BEARER_TOKEN'='<your_bearer_token>'

bearer_token = os.environ.get("BEARER_TOKEN")


racist_dict = {
        "marjorie taylor greene": "1344356576786866176",
        "jim jordan": "18166778",
        "john cornyn": "13218102",
        "donald trump": "822215679726100480"
 }


def create_url():
    """
    Creating the url in order to make the request to the API
    """
    
    # these are adjustable, see README.md for other tweet fields
    tweet_fields = "tweet.fields=author_id,text"
    print("Enter a valid Twitter User's id number or name, we might already have the info you need!")
    print()
    print("To find Twitter User IDs, please go this website and enter the user's Twitter username: %s" % 'https://tweeterid.com/')
    print()
    info = input("Enter a Twitter ID or a name (first and last if you do): ")
    while info.lower() not in racist_dict and info.isalpha():
        info = input("Sorry, that was either not a saved name or not a valid Twitter ID. Please try again: ")
    if info.lower() in racist_dict.keys():
        frmt = info.lower()
        id = racist_dict[frmt]
    else:
        id = info

    url = "https://api.twitter.com/2/users/{}/liked_tweets".format(id)
    return url, tweet_fields


def bearer_oauth(r):

    """
    Bearer token authentication step
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2LikedTweetsPython"
    return r


def get_response(url, tweet_fields):
    response = requests.request(
        "GET", url, auth=bearer_oauth, params=tweet_fields)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def main():
    url, tweet_fields = create_url()
    
    # this is the dict
    json_response = get_response(url, tweet_fields)

    # this is a string representation of it
    formated_str = (json.dumps(json_response, indent=4, sort_keys=True))
    
    # this is a list of dictionaries
    list_of_data = json_response["data"]
    
    # empty dict to add the tweet id (key) and tweet content (val) from list_of_data
    new_dict = {}
    for i in range(len(list_of_data)):
        new_dict[list_of_data[i]["id"]] = list_of_data[i]["text"]
    

    tweets_tbl = pd.DataFrame.from_dict(new_dict, orient='index', columns=['Tweet'])

    engine = db.create_engine('sqlite:///Liked_Tweets.db')
    tweets_tbl.to_sql('tweets', con=engine, if_exists='replace', index=False)
    display(tweets_tbl)
    # query_result = engine.execute("SELECT * FROM tweets;").fetchall()
    # print(pd.DataFrame(query_result))


if __name__ == "__main__":
    main()
