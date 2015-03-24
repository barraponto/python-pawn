class Player(object):
    """Creates a named player for the game.

    :param name: a name string for the player.
    """
    def __init__(self, name='John Doe'):
        self.name = name

    def __repr__(self):
        return 'Player(name={name!r})'.format(name=self.name)
