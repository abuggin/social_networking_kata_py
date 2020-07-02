from feed import Feed
from cli import Cli

if __name__ == "__main__":
    cli = Cli(Feed())
    while True:
        cmd_str = input(">> ")
        cmd = cli.parse(cmd_str)
        res = cli.run(cmd)
        if res:
            print(res)
