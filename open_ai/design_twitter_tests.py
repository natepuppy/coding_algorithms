import unittest
from design_twitter import Twitter
import logging

class Tests(unittest.TestCase):
    def test_post_tweet(self):
        twitter = Twitter()
        twitter.postTweet(1, 101)

        x = 1
        if x <= 0:
            raise Exception("Invalid input")

        logging.error("Something went wrong")
        logging.warning("Something might have went wrong")

        logging.basicConfig(level=logging.INFO)
        logging.info("Info")

        self.assertEqual(twitter.getNewsFeed(1), [101])

if __name__ == "__main__":
    unittest.main()
