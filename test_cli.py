from feed import FeedCli
import unittest
class TestCliFeed(unittest.TestCase):
    def test_meta(self):
        self.assertEqual(2,1+1)

    def test_adding_user(self):
        feed = FeedCli()
        username = "John"
        feed.add_user(username)
        actual = feed.get_usernames()
        self.assertEqual([username], actual)
        

if __name__ == "__main__":
    unittest.main()