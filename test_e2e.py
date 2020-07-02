from cli import Cli
from feed import FeedCli
import unittest


class TestE2E(unittest.TestCase):
    def test_e2e(self):
        cli = Cli(FeedCli())
        cmds = [
            "Josh -> As Josh used to say",
            "Josh",
            "Josh follows Bob",
            "Bob -> @Josh whats'up?",
            "John -> pancakes",
            "Bob -> @John you cooking pancakes?",
            "Josh -> mamma mia",
            "Josh wall",
        ]
        parsed = [cli.parse(cmd) for cmd in cmds]
        run = [cli.run(cmd) for cmd in parsed]
        expected = [
            "mamma mia",
            "@John you cooking pancakes?",
            "@Josh whats'up?",
            "As Josh used to say",
        ]

        self.assertEqual(expected, run[-1])
