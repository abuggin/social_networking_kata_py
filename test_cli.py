from feed import FeedCli
from cli import Cli
from command import Command, Action
import unittest
from unittest import mock


class TestCliFeed(unittest.TestCase):
    josh_hello_cmd = Command(
        action=Action.WRITE, actor="Josh", arg_dependant_on_action="Hello!"
    )
    jonny_display_cmd = Command(
        action=Action.DISPLAY_OWN_POSTS, actor="Jonny", arg_dependant_on_action=None
    )

    def test_display_command(self):
        spy = mock.Mock(wraps=FeedCli())
        cli = Cli(spy)
        cli.run(self.jonny_display_cmd)
        spy.get_messages_of.assert_called()

    def test_post_message(self):
        spy = mock.Mock(wraps=FeedCli())
        cli = Cli(spy)
        cli.run(self.josh_hello_cmd)
        spy.post_message.assert_called_once_with(username="Josh", message="Hello!")
        spy.get_messages_of.assert_not_called()

    def test_parse_command(self):
        cli = Cli(None)
        res = cli.parse("Josh -> Hello!")
        parsed_cmd = self.josh_hello_cmd
        self.assertEqual(parsed_cmd, res)

    def test_hash_command(self):
        another_josh_hello_cmd = Command(
            action=Action.WRITE, actor="Josh", arg_dependant_on_action="Hello!"
        )
        self.assertEqual(another_josh_hello_cmd, self.josh_hello_cmd)
        self.assertEqual(hash(another_josh_hello_cmd), hash(self.josh_hello_cmd))

    def test_parse_display_command(self):
        parsed_cmd = self.jonny_display_cmd
        self.assertEqual(parsed_cmd, Cli(None).parse("Jonny"))

    def test_parse_follow_command(self):
        cmd_str = "Josh follows Bob"
        cmd = Command(Action.FOLLOW,"Josh","Bob")
        self.assertEqual(cmd,Cli().parse(cmd_str))

if __name__ == "__main__":
    unittest.main()
