from feed import FeedCli
from dataclasses import dataclass


class Cli:
    def __init__(self, feed: FeedCli):
        self.feed = feed

    def run(self, command):
        idx_arrow = command.find("->")
        if idx_arrow != -1:
            username = command[:idx_arrow].strip()
            message = command[idx_arrow + 2 :].strip()
            self.feed.post_message(username=username, message=message)
        else:
            self.feed.get_messages_of(command)

    def parse(self, command_str):
        username = command_str.split()[0]
        if username == command_str:
            command = "display_own_posts"
            args = None
        else:
            command = "write"
            args = "Hello!"
        return Command(command, username, args)


@dataclass(frozen=True)
class Command:
    action: str
    actor: str
    arg_dependant_on_action: str
