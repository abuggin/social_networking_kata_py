from collections import defaultdict


class FeedCli:
    def __init__(self):
        self.user_to_messages = defaultdict(list)
        self.user_follows = defaultdict(set)

    def add_user(self, name: str):
        self.user_to_messages[name]

    def get_usernames(self):
        return list(self.user_to_messages.keys())

    def post_message(self, username, message):
        self.user_to_messages[username].append(message)

    def get_messages_of(self, username):
        return self.user_to_messages[username]

    def follow(self, username: str, wants_to_follow_username: str):
        self.user_follows[username].add(wants_to_follow_username)

    def users_followed_by(self, username: str):
        return self.user_follows[username]
