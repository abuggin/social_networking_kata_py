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

if __name__ == "__main__":
    unittest.main()
