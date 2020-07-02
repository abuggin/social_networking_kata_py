class Cli:
    def __init__(self, feed):
        self.feed = feed

    def run(self, command):
        self.feed.get_messages_of(command)
