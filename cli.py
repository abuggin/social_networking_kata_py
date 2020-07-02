class Cli:
    def __init__(self, feed):
        self.feed = feed

    def run(self, command):
        idx_arrow = command.find("->")
        if idx_arrow != -1:
            username = command[:idx_arrow]
            message = command[idx_arrow+1:]
            self.feed.post_message(username,message)
        else:
            self.feed.get_messages_of(command)
