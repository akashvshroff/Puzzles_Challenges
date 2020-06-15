class SnakesLadders():
    '''
    Python simulation of the classic snakes and ladders boardgame!
    See also: https://www.codewars.com/kata/587136ba2eefcb92a9000027/train/python
    '''
    def __init__(self):
        self.snakes = [(6,16),(11,49),(19,62),(25,46),(53,74),(60,64),(68,89),(75,95),(80,99),(88,92)]
        self.ladders = [(2,38),(7,14),(8,31),(15,26),(21,42),(28,84),(36,44)(51,67),(71,91),(78,98),(87,94)]
        self.player1_pos = 0
        self.player2_pos = 0
        self.turn = 0
        self.game_won = None


    def check_collision(self):
        # checks if it collides with a snake or with ladders
        for s,e in self.snakes:
            if not self.turn:
                if e == self.player1_pos:
                    self.player1_pos = s
            else:
                if e == self.player2_pos:
                    self.player2_pos = s

        for s,e in self.ladders:
            if not self.turn:
                if s == self.player1_pos:
                    self.player1_pos = e
            else:
                if s == self.player2_pos:
                    self.player2_pos = e


    def play(self, die1, die2):
        # Code Here
        another_turn = False
        if self.game_won:
            return 'Game over!'
        else:
            moves = die1 + die2
            if die1 == die2:
                another_turn = True
            if not self.turn: #player 1
                self.player1_pos += moves
                if self.player1_pos > 100:
                    self.player1_pos = 100 - (self.player1_pos - 100)
            else:
                self.player2_pos += moves
                if self.player2_pos > 100:
                    self.player2_pos = 100 - (self.player2_pos - 100)
            self.check_collision()
            if self.player1_pos == 100 or self.player2_pos == 100:
                self.game_won = True
                return 'Player {} Wins!'.format(1 if self.player1_pos == 100 else 2)
            player,square = (1,self.player1_pos) if not self.turn else (2,self.player2_pos)
            ret =  'Player {} is on square {}'.format(player,square)
            if not another_turn:
                self.turn = 1 if not self.turn else 0
            return ret
