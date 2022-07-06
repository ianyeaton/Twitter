# *Some notes on this repository*

#### This is the style check which uses continuous integration to check for every commit: 


![example_workflow](https://github.com/ianyeaton/Twitter/actions/workflows/lint.yaml/badge.svg)


#### This is the unittester to make sure that all of the files pushed from the twttrAPI_liked_posts.py have the correct outputs:


![example_workflow](https://github.com/ianyeaton/Twitter/actions/workflows/tester.yaml/badge.svg)


#### **This is an example of how to use the repository**


* The file twttrAPI_liked_posts.py is used to retrieve all of the tweets liked by a specified user
> - *There is a link to find a person's twitter id number which is provided in the README.md*
> - *The program takes input from the user to make the request to find a specific user's liked tweets*
> - *There is a dictionary in the file which already has the names of some... characters... in today's society*
> - *This dictionary is useful in case a person inputs a specific name like John Cornyn or Marjorie Taylor Green*
> - *The purpose of this dictionary is to give people easy access to many racist peoples' Twitter history*


* In order to use this file, environment variables for the specified bearer token of the developer is required
> - *Set this environment variable in the .bashrc file of the terminal in order to prevent people from stealing the code*
> - *All generated info about tweets is stored in a database called Liked_Tweets.db*


#### Some examples of accessable tweet fields to tailor results to the user's wants and needs:
    attachments, author_id, context_annotations, conversation_id, created_at, entities, geo, id,
    in_reply_to_user_id, lang, non_public_metrics, organic_metrics, possibly_sensitive, 
    promoted_metrics, public_metrics, referenced_tweets, source, text, and withheld


#### These lines of code below are good in order to test the functionality of the generated Database:
    query_result = engine.execute("SELECT * FROM tweets;").fetchall()
    print(pd.DataFrame(query_result))

- **To access the Twitter API:**
> [Twitter API](https://developer.twitter.com/en/docs/twitter-api)

- **Access the link below to find a user's Twitter ID:**
> [Tweeter IDs](https://tweeterid.com/)