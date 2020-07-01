from feed import FeedCli
import unittest


class TestCliFeed(unittest.TestCase):
    def test_adding_user(self):
        feed = FeedCli()
        username = "John"
        feed.add_user(username)
        actual = feed.get_usernames()
        self.assertEqual([username], actual)

    def test_link_message_to_user(self):
        feed = FeedCli()
        username = "John"
        message = "Hello!"
        feed.add_user(username)
        feed.post_message(username, message)
        actual_messages = feed.get_messages_of(username)
        self.assertEqual([message], actual_messages)


if __name__ == "__main__":
    unittest.main()
