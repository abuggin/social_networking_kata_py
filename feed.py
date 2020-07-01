class FeedCli:
    def __init__(self):
        self.usernames = []

    def add_user(self, name: str):
        self.usernames.append(name)

    def get_usernames(self):
        return self.usernames
