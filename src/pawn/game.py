from pawn.player import Player

class Game(object):
    player_class = Player
    supported_number_of_players = [2, 4]

    def __init__(self, number_of_players=2):
        if number_of_players not in self.supported_number_of_players:
            raise ValueError(
                'Unsupported number of players: {number}.'.format(
                    number=number_of_players))
        else:
            self.players = [self.player_class(name='Player {number}'.format(
                number=n)) for n in range(1, 1 + number_of_players)]
