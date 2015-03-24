class Player(object):
    def __init__(self, name='John Doe'):
        self.name = name

    def __repr__(self):
        return 'Player(name={name!r})'.format(name=self.name)
