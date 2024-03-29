import random

moves = ['rock', 'paper', 'scissors']


class Player():
    my_move = None
    their_move = None

    def __init__(self):
        self.score = 0


    def move(self):
        return 'rock'


    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        choice = input('rock, paper, scissors? >')
        choice = choice.lower()
        while choice != 'rock'and choice != 'paper'and choice != 'scissors':
            print('Sorry, please try again')
            choice = input('rock, paper, scissors? >')
        return (choice)


class ReflectPlayer(Player):

    def learn(self, my_move, their_move):
        self.my_move = their_move

    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        else:
            return self.my_move


class Cycles(Player):
    def __init__(self):
        self.index = 0
        super(Cycles, self).__init__()

    def move(self):
        print(self.index)
        if self.index == len(moves):
            self.index = 0

        self.my_move = moves[self.index]
        self.index += 1
        return self.my_move
        if self.index > 2:
            self.index.clear()

class Game():

    def __init__(self, p2):
        self.p1 = HumanPlayer()
        self.p2 = p2

    def play_game(self):
        print("\nRock Paper Scissors, Go!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        if self.p1.score > self.p2.score:
            print("Player 1 won!")
        elif self.p1.score < self.p2.score:
            print("Player 2 won!")
        else:
            print('The game was a tie!')
        print("The final score is " + str(self.p1.score) + " to " +
              str(self.p2.score))

    def play_single(self):
        print("\nRock Paper Scissors, Go!")
        print(f"Round 1 of 1:")
        self.play_round()
        if self.p1.score > self.p2.score:
            print("Player 1 won!")
        elif self.p1.score < self.p2.score:
            print("Player 2 won!")
        else:
            print("The game was a tie!")
        print("The final score " + str(self.p1.score) + " to " +
              str(self.p2.score))

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        result = self.play(move1, move2)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)


    def play(self, move1, move2):
        print(f"You played {move1}")
        print(f"Opponent played {move2}")
        if beats(move1, move2):
            print("** PLAYER ONE WINS **")
            self.p1.score += 1
            print(f"Score: Player 1: {self.p1.score}, Player 2:\
             {self.p2.score}\n\n")
            return 1
        elif beats(move2, move1):
            print("** PLAYER TWO WINS **")
            self.p2.score += 1
            print(f"Score: Player 1: {self.p1.score}, Player 2:\
                {self.p2.score}\n\n")
            return 2
        else:
            print("**TIE **")
            print(f"Score: Player 1: {self.p1.score}, Player 2:\
             {self.p2.score}\n\n")
            return 0


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


if __name__ == '__main__':
    print("Welcome to a game of Rock Paper Scissors!\n")
    answer = [Player(), RandomPlayer(), Cycles(), ReflectPlayer()]
    p2 = input("What kind of opponents would you like to compete against?\n"
               "Enter r for a random player, l for a learning player, "
               "s for strategic player or just hit any key for a random "
               "choice of opponent. >")

    while p2 != "r" or p2 != "l" or p2 != "s":
        p2 = random.choice(answer)
        break

    if p2 == "r":
        p2 = RandomPlayer()
    elif p2 == "s":
        p2 = Cycles()
    elif p2 == "l":
        p2 = ReflectPlayer()

    rounds = input("\nDo you want to play a single round or "
                   "three rounds?\n"
                   "Enter for 1 for a single round or 3 for three rounds>")
    match = Game(p2)
    while True:
        if rounds == "1":
            match.play_single()
            break
        elif rounds == "3":
            match.play_game()
            break
        else:
            print("Sorry, please try again!")
            rounds = input("Enter 1 for a single\
             game and 3 for a full match: >")
