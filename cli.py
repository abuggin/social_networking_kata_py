from feed import Feed
from command import Command, Action


class Cli:
    def __init__(self, feed: Feed):
        self.feed = feed

    def run(self, command: Command):
        if command.action == Action.WRITE:
            return self.feed.post_message(
                username=command.actor, message=command.arg_dependant_on_action
            )
        elif command.action == Action.FOLLOW:
            return self.feed.follow(
                follower=command.actor, followed=command.arg_dependant_on_action
            )
        elif command.action == Action.DISPLAY_RELEVANT_POSTS:
            return self.feed.get_wall_for(command.actor)
        else:
            return self.feed.get_messages_of(command.actor)

    def parse(self, command_str):
        splitted = command_str.split()
        username = splitted[0]
        args = " ".join(splitted[2:])
        if username == command_str:
            command = Action.DISPLAY_OWN_POSTS
        elif splitted[1] == "follows":
            command = Action.FOLLOW
        elif splitted[1] == "wall":
            command = Action.DISPLAY_RELEVANT_POSTS
        else:
            command = Action.WRITE
        return Command(command, username, args if bool(args) else None)
