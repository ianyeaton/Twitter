import requests
import twitter
import os
# from pytwitter import Api

# CLIENT_ID = os.environ.get('TIWTTER_CLIENT_ID')
# CLIENT_SECRET = os.environ.get('TWITTER_CLIENT_SECRET')

os.environ['TOKEN'] = 'AAAAAAAAAAAAAAAAAAAAAKnoeAEAAAAA8C4RVNk3yONexqxxV9h1Ir12ipc%3DJvIiR9vgrMMmAFIbBOecFvIfur6zgPAaMTvrE6eR9Ym99MFSyB'

CLIENT_ID = 'AwD5IGio7VSpEiVW6G9oaiWm0'
CLIENT_SECRET = 'b76SNhseu536CkINFR4rDm1f2sbTcaH89SplwyBJpwPU4HboP'
ACCESS_TOKEN = '1311899176968564737-K1Kn6DOT9cJ7euisLDidCTZgFwsgGH'
ACCESS_SECRET = 'IjvtxhJ8A4YKHux8pXbG56YmQFNs6TI3BETFH7BoTBFmq'

#BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAKnoeAEAAAAA8C4RVNk3yONexqxxV9h1Ir12ipc%3DJvIiR9vgrMMmAFIbBOecFvIfur6zgPAaMTvrE6eR9Ym99MFSyB'

# api = twitter.Api(
#  consumer_key=CLIENT_ID,
#  consumer_secret=CLIENT_SECRET,
#  access_token_key=ACCESS_TOKEN,
#  access_token_secret=ACCESS_SECRET 
# )

def auth():
  return os.getenv('TOKEN')

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def create_url(keyword, start_date, end_date, max_results=10):

  base_url = 'https://api.twitter.com/2/tweets/search/all'

  query_params = {
                'query': keyword,
                'start_time': start_date,
                'end_time': end_date,
                'max_results': max_results,
                'expansions': 'author_id,in_reply_to_user_id,geo.place_id',
                'tweet.fields': 'id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,public_metrics,referenced_tweets,reply_settings,source',
                'user.fields': 'id,name,username,created_at,description,public_metrics,verified',
                'place.fields': 'full_name,id,country,country_code,geo,name,place_type',
                'next_token': {}
              }
  return (base_url, query_params)

def get_response(url, headers, params, next_token=None):
  params['next_token'] = next_token
  response = requests.request("GET", url, headers = headers, params = params)
  print("Endpoint Response Code: " + str(response.status_code))
  if response.status_code != 200:
    raise Exception(response.status_code, response.text)
  return response.json()


bearer_token = auth()
headers = create_headers(bearer_token)
keyword = "xbox lang:en"
start_time = "2021-03-01T00:00:00.000Z"
end_time = "2021-03-31T00:00:00.000Z"
max_results = 15

url = create_url(keyword, start_time, end_time, max_results)

json_resp = get_response(url[0], headers, url[1])

print(json.dumps(json_response, indent=4, sort_keys=True))



# AUTH_URL = 'https://api.twitter.com/oauth2/request_token'

# auth_response = requests.post(AUTH_URL, {
#     'grant_type': 'client_credetial',
#     'client_id': CLIENT_ID,
#     'client_secret': CLIENT_SECRET,
#     })

# auth_response_data = auth_response.json()
# #print(auth_response_data)

# access_token = auth_response_data['access_token']

# headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}

# HEADER = {'Authorization': 'Bearer {token}'.format(token=ACCESS_TOKEN)}

# BASE_URL = 'https://api.twitter.com/2/'

# r = requests.get(BASE_URL + 'tweets/search/recent', headers=headers)
# res = requests.get('https://api.twitter.com/2/tweets/search/recent', headers=HEADER)

# print(r.json())
# print(res.json())

#ACCESS_SECRET = 'IjvtxhJ8A4YKHux8pXbG56YmQFNs6TI3BETFH7BoTBFmq'

#api = Api(
 # consumer_key=CLIENT_ID,
#  consumer_secret=CLIENT_SECRET,
 # access_token=ACCESS_TOKEN,
  #access_secret=ACCESS_SECRET 
#)


#I need to complete this tomorrow morning
