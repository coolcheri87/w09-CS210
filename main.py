

import sys
sys.path.append('.')
from game.scheduler import Scheduler


def main():
    scheduler = Scheduler()
    scheduler.playGame()


if __name__ == '__main__':
    main()