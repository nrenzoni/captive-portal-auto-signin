class NoConfig(Exception):
    """
    raise when no jct config file found
    """
    pass


class MultipleConfig(Exception):
    """
    raise when multiple jct config files found in directory
    """
    def __init__(self, dir):
        self.dir = dir

class InvalidConfig(Exception):
    """
    raise when config file does not have username and password tags
    """
    def __init__(self, file):
        self.file = file


def quit():
    input('press any key to exit...')
    raise SystemExit(0)