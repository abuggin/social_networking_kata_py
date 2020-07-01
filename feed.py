from collections import defaultdict


class FeedCli:
    def __init__(self):
        self.user_to_messages = defaultdict(list)

    def add_user(self, name: str):
        self.user_to_messages[name]

    def get_usernames(self):
        return list(self.user_to_messages.keys())

    def post_message(self, username, message):
        self.user_to_messages[username].append(message)

    def get_messages_of(self, username):
        return self.user_to_messages[username]
