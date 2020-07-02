from feed import FeedCli
from cli import Cli, Command
import unittest
from unittest import mock


class TestCliFeed(unittest.TestCase):
    def test_display_command(self):
        str_cmd = "Josh"
        spy = mock.Mock(wraps=FeedCli())
        cli = Cli(spy)
        cli.run(str_cmd)
        spy.get_messages_of.assert_called()

    def test_post_message(self):
        str_cmd = "Josh -> Hello!"
        spy = mock.Mock(wraps=FeedCli())
        cli = Cli(spy)
        cli.run(str_cmd)
        spy.post_message.assert_called_once_with(username="Josh", message="Hello!")
        spy.get_messages_of.assert_not_called()

    def test_parse_command(self):
        cli = Cli(None)
        res = cli.parse("Josh -> Hello!")
        parsed_cmd = Command(
            action="write", actor="Josh", arg_dependant_on_action="Hello!"
        )
        self.assertEqual(parsed_cmd, res)

    def test_hash_command(self):
        cmd = Command(action="write", actor="Josh", arg_dependant_on_action="Hello!")
        cmd_1 = Command(action="write", actor="Josh", arg_dependant_on_action="Hello!")
        self.assertEqual(cmd, cmd_1)
        self.assertEqual(hash(cmd), hash(cmd_1))

    def test_parse_display_command(self):
        parsed_cmd = Command(
            action="display_own_posts", actor="Jonny", arg_dependant_on_action=None
        )
        self.assertEqual(parsed_cmd, Cli(None).parse("Jonny"))


if __name__ == "__main__":
    unittest.main()
