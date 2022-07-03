import unittest
from twttrAPI_liked_posts import create_url, connect_to_endpoint


class TestTwttrAPI_liked_posts(unittest.TestCase):
    def test_create_url(self):
        self.assertEqual(type(create_url()), tuple)

    def test_connect_to_endpoint(self):
        user = '18166778'
        link = "https://api.twitter.com/2/users/{}/liked_tweets".format(user)
        twt_field = "tweet.fields=public_metrics"
        self.assertEqual(type(connect_to_endpoint(link, twt_field)), dict)

if __name__ == '__main__':
    unittest.main()
