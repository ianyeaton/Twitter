import requests
import os
import json

# Set the environment variables before hand in the terminal with:
# export 'BEARER_TOKEN'='AAAAAAAAAAAAAAAAAAAAAIcNeQEAAAAAKQessa1SWX%2FXKCLWdzF%2B8Rj1FPA%3DN2obgg63K4RQmn6kDj4aIbXbmLeWnD2RJPDiHpYb6U2fDxKpPy'
bearer_token = os.environ.get("BEARER_TOKEN")

racist_dict = {
        "marjorie taylor greene": "1344356576786866176 ",
        "jim jordan": "18166778",
        "john cornyn": "13218102",
        "donald trump": "822215679726100480"
 }


link_to_twitter_id_finder = 'https://tweeterid.com/'


def create_url():
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    tweet_fields = "tweet.fields=attachments,author_id,created_at,public_metrics"
    # Be sure to replace your-user-id with your own user ID or one of an authenticating user
    # You can find a user ID by using the user lookup endpoint
    info = input("Enter a valid Twitter User's id number or name, we might already have the info you need! : ")
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
    json_response = connect_to_endpoint(url, tweet_fields)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
