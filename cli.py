from feed import FeedCli
from command import Command, Action


class Cli:
    def __init__(self, feed: FeedCli):
        self.feed = feed

    def run(self, command: Command):
        if command.action == Action.WRITE:
            self.feed.post_message(
                username=command.actor, message=command.arg_dependant_on_action
            )
        else:
            self.feed.get_messages_of(command.actor)

    def parse(self, command_str):
        splitted = command_str.split()
        username = splitted[0]
        args = ''.join(splitted[2:]) 
        if username == command_str:
            command = Action.DISPLAY_OWN_POSTS
        elif splitted[1] == "follows":
            command = Action.FOLLOW
        elif splitted[1] == "wall":
            command = Action.DISPLAY_RELEVANT_POSTS
        else:
            command = Action.WRITE
        return Command(command, username, args if bool(args) else None)
