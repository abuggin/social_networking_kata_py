from feed import FeedCli
from cli import Cli
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
        spy.post_message.assert_called()
        spy.get_messages_of.assert_not_called()


if __name__ == "__main__":
    unittest.main()
