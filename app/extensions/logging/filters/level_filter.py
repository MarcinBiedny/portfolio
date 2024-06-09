import logging


class LevelFilter(logging.Filter):
    level = 0

    def __init__(self, level: int = logging.DEBUG) -> None:
        self.level = level
        super().__init__()

    def filter(self, record):
        return record.levelno == self.level
