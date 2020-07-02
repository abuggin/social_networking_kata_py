from collections import defaultdict
from time import time
from collections import namedtuple

TimeAndMessage = namedtuple("TimeAndMessage", ("time", "message"))


class FeedCli:
    def __init__(self):
        self.messages_of_user = defaultdict(list)
        self.followed_by_user = defaultdict(set)

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
        wall_messages_for_this_user = self.messages_of_user[username].copy()
        all_people_followed_by_user = self.followed_by_user[username]
        for a_followed_user in all_people_followed_by_user:
            wall_messages_for_this_user += self.messages_of_user[a_followed_user]
        by_time = lambda t: t.time
        sorted_messages_by_time = sorted(wall_messages_for_this_user, key=by_time, reverse=True)
        return [t.message for t in sorted_messages_by_time]
