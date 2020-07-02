from feed import Feed
import unittest


class TestFeed(unittest.TestCase):
    def test_link_message_to_user(self):
        feed = Feed()
        username = "John"
        message = "Hello!"
        feed.post_message(username, message)
        actual_messages = feed.get_messages_of(username)
        self.assertEqual([message], actual_messages)

    def test_non_existing_user(self):
        feed = Feed()
        self.assertEqual([], feed.get_messages_of("John"))

    def test_follow_relationship(self):
        feed = Feed()
        feed.follow(follower="John", followed="Jamie")
        res = feed.users_followed_by(username="John")
        self.assertEqual({"Jamie"}, res)

    def test_follow_another_relationship(self):
        feed = Feed()
        feed.follow(follower="John", followed="Jamie")
        feed.follow(follower="John", followed="Jess")
        res = feed.users_followed_by(username="John")
        self.assertSetEqual({"Jess", "Jamie"}, res)

    def test_get_wall_messages_of_followed_user(self):
        feed = Feed()
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

    def test_get_wall_msgs_when_following_multiple_users(self):
        feed = Feed()
        follower = "Alice"
        followed_b = "Bob"
        followed_c = "Charlie"
        feed.follow(follower=follower, followed=followed_b)
        feed.follow(follower=follower, followed=followed_c)
        old_msg_b = "Sup?"
        feed.post_message(followed_b, old_msg_b)
        old_msg_c = "Not much"
        feed.post_message(followed_c, old_msg_c)
        new_msg = "Busy day copy pasting from stackoverflow"
        feed.post_message(followed_b, new_msg)
        res = feed.get_wall_for(follower)
        self.assertEqual([new_msg, old_msg_c, old_msg_b], res)

    def test_get_wall_include_own_post(self):
        feed = Feed()
        own_message = "Message message message"
        feed.post_message("A", own_message)
        self.assertEqual([own_message], feed.get_wall_for("A"))

    def test_get_wall_own_post_and_newest_order(self):
        feed = Feed()
        own_message = "Message message message"
        feed.post_message("A", own_message)
        feed.follow("A", "B")
        B_msg = "it's your birthday"
        feed.post_message("B", B_msg)
        own_new_msg = "speechless"
        feed.post_message("A", own_new_msg)
        self.assertEqual([own_new_msg, B_msg, own_message], feed.get_wall_for("A"))


if __name__ == "__main__":
    unittest.main()