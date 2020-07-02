from collections import defaultdict
from time import time
from collections import namedtuple

TimeAndMessage = namedtuple("TimeAndMessage", ("time", "message"))


class FeedCli:
    def __init__(self):
        self.messages_of_user = defaultdict(list)
        self.followed_by_user = defaultdict(set)

    def get_usernames(self):
        return list(self.messages_of_user.keys())

    def post_message(self, username, message):
        timeAndMsg = TimeAndMessage(time(), message)
        self.messages_of_user[username].append(timeAndMsg)

    def get_messages_of(self, username):
        return [t.message for t in self.messages_of_user[username]]

    def follow(self, follower: str, followed: str):
        self.followed_by_user[follower].add(followed)

    def users_followed_by(self, username: str):
        return self.followed_by_user[username]

    def get_wall_for(self, username: str):
        wall_messages_relevant_for_this_user = []
        people_followed_by_user = self.followed_by_user[username]
        for user in people_followed_by_user:
            wall_messages_relevant_for_this_user += self.messages_of_user[user]
        byTime = lambda t: t.time
        wall_messages_relevant_for_this_user.sort(key=byTime, reverse=True)
        return [t.message for t in wall_messages_relevant_for_this_user]
