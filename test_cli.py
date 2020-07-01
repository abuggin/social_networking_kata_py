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

    def test_non_existing_user(self):
        feed = FeedCli()
        self.assertEqual([], feed.get_messages_of("John"))

    def test_follow_relationship(self):
        feed = FeedCli()
        feed.follow(follower="John", followed="Jamie")
        res = feed.users_followed_by(username="John")
        self.assertEqual({"Jamie"}, res)

    def test_follow_another_relationship(self):
        feed = FeedCli()
        feed.follow(follower="John", followed="Jamie")
        feed.follow(follower="John", followed="Jess")
        res = feed.users_followed_by(username="John")
        self.assertSetEqual({"Jess", "Jamie"}, res)

    def test_get_wall_messages_of_followed_user(self):
        feed = FeedCli()
        follower = "a"
        followed = "b"
        feed.follow(follower=follower, followed=followed)
        old_msg = "Sup?"
        feed.post_message(followed, old_msg)
        res = feed.get_wall_for(follower)
        self.assertEqual([old_msg], res)
        new_msg = "Busy day copy pasting from stackoverflow"
        feed.post_message(followed, new_msg)
        res = feed.get_wall_for(follower)
        self.assertEqual([new_msg, old_msg], res)


if __name__ == "__main__":
    unittest.main()
