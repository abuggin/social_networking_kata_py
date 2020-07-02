from feed import FeedCli
class Cli:
    def __init__(self, feed: FeedCli):
        self.feed = feed

    def run(self, command):
        idx_arrow = command.find("->")
        if idx_arrow != -1:
            username = command[:idx_arrow].strip()
            message = command[idx_arrow+2:].strip()
            self.feed.post_message(username=username,message=message)
        else:
            self.feed.get_messages_of(command)

    def parse(self, command):
        pass


class Command:
    def __init__(self, action, actor, arg_dependant_on_action):
        pass