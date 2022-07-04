import requests
import os
import json
import pandas as pd
import sqlalchemy as db


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
    
    # Adjust tweet fields to your needs:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    tweet_fields = "tweet.fields=author_id,text"

    info = input("Enter a valid Twitter User's id number or name, we might already have the info you need!: ")
    if info.lower() in racist_dict.keys():
        frmt = info.lower()
        id = racist_dict[frmt]
    else:
        id = info
    # You can adjust ids to include a single Tweets.
    # Or you can add to up to 100 comma-separated IDs
    url = "https://api.twitter.com/2/users/{}/liked_tweets".format(id)
    return url, tweet_fields


def bearer_oauth(r):

    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2LikedTweetsPython"
    return r


def connect_to_endpoint(url, tweet_fields):
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
    json_response = connect_to_endpoint(url, tweet_fields)

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
    
    # Testing a query to see if data is correctly uploading to the database
    # query_result = engine.execute("SELECT * FROM tweets;").fetchall()
    # print(pd.DataFrame(query_result))

if __name__ == "__main__":
    main()




### Notes to be put in the README.md:

# BEARER_TOKEN = AAAAAAAAAAAAAAAAAAAAAIcNeQEAAAAAKQessa1SWX%2FXKCLWdzF%2B8Rj1FPA%3DN2obgg63K4RQmn6kDj4aIbXbmLeWnD2RJPDiHpYb6U2fDxKpPy
# api_key = 'yQeAcO4i2SdtfDBMum4ZQyg98'
# api_key_secret = '95XDKBk0fBwXmwWniLXUnnrkYSx7VQF07RobX8zrHj1FUGia1d'
# link_to_twitter_id_finder = 'https://tweeterid.com/'
