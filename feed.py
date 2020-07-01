from collections import defaultdict


class FeedCli:
    def __init__(self):
        self.messages_by_user = defaultdict(list)
        self.followed_by_user = defaultdict(set)

    def add_user(self, name: str):
        self.messages_by_user[name]

    def get_usernames(self):
        return list(self.messages_by_user.keys())

    def post_message(self, username, message):
        self.messages_by_user[username].append(message)

    def get_messages_of(self, username):
        return self.messages_by_user[username]

    def follow(self, follower: str, followed: str):
        self.followed_by_user[follower].add(followed)

    def users_followed_by(self, username: str):
        return self.followed_by_user[username]

    def get_wall_for(self, username: str):
        wall_messages = []
        for user in self.followed_by_user[username]:
            wall_messages += self.messages_by_user[user]
        wall_messages.reverse()
        return wall_messages