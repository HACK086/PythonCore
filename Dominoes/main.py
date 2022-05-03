import random


class Domino:

    def __init__(self):
        self.set = [[i, j] for i in range(7) for j in range(i, 7)]
        self.stock = []
        self.players = [[], []]
        self.snake = []
        self.status = 0
        self.end_game = False

        self.split_set()
        self.state_game()

    def split_set(self):
        while True:
            random.shuffle(self.set)
            self.stock = self.set[:14]
            self.players = [self.set[14:21], self.set[21:]]
            if self.calc_snake():
                break

    def calc_snake(self):
        max_d = max(d for d in (self.players[0] + self.players[1]) if d[0] == d[1])
        if max_d:
            self.snake.append(max_d)
            if max_d in self.players[0]:
                self.status = 1
            self.players[[1, 0][self.status]].remove(max_d)
        return len(self.snake) > 0

    def input_action(self, action):
        if self.status:
            try:
                self.players[1][abs(int(action)) - 1]
            except (ValueError, IndexError):
                print("Invalid input. Please try again.")
            else:
                if not self.make_move(int(action)):
                    print("Illegal move. Please try again.")
        else:
            self.sort_ai_set()
            for i in range(len(self.players[0]), -1, -1):
                if self.make_move(i):
                    break

    def make_move(self, choice):
        if choice == 0:
            self.take_from_stock()
        else:
            d = self.players[self.status][abs(choice) - 1]
            if self.wrong_move(choice, d):
                return False
            self.players[self.status].remove(d)
            d = self.adopt_piece(choice, d)
            self.snake.append(d) if choice > 0 else self.snake.insert(0, d)
            if self.players.count([]) or self.error_snake():
                self.end_game = True
        self.status = [1, 0][self.status]
        self.state_game()
        return True

    def wrong_move(self, choice, d):
        return choice > 0 and self.snake[-1][1] not in d or choice < 0 and self.snake[0][0] not in d

    def adopt_piece(self, choice, d):
        if choice > 0 and self.snake[-1][1] != d[0] or choice < 0 and self.snake[0][0] != d[1]:
            return d[::-1]
        return d

    def take_from_stock(self):
        if len(self.stock) > 0:
            choice = random.choice(self.stock)
            self.players[self.status].append(choice)
            self.stock.remove(choice)

    def error_snake(self):
        first_d = self.snake[0][0]
        return first_d == self.snake[-1][1] and str(self.snake).count(str(first_d)) == 8

    def sort_ai_set(self):
        def get_score(item):
            return item[1]

        scores = self.get_scores()
        sorted_set = []
        for d in self.players[0]:
            sorted_set.append([d, scores[d[0]] + scores[d[1]]])
        sorted_set.sort(key=get_score)
        self.players[0] = [d[0] for d in sorted_set]

    def get_scores(self):
        scores = dict()
        numbers = str(self.snake + self.players[0])
        for i in range(7):
            scores[i] = numbers.count(str(i))
        return scores

    def state_game(self):
        print("======================================================================")
        print(f"Stock size: {len(self.stock)}")
        print(f"Computer pieces: {len(self.players[0])}\n")
        self.print_snake()
        print("\nYour pieces:")
        for i in range(len(self.players[1])):
            print(f"{i + 1}:{self.players[1][i]}")

        if self.end_game:
            if len(self.players[0]) == 0:
                print("\nStatus: The game is over. The computer won!")
            elif len(self.players[1]) == 0:
                print("\nStatus: The game is over. You won!")
            else:
                print("\nStatus: The game is over. It's a draw!")
        else:
            statuses = ["\nStatus: Computer is about to make a move. Press Enter to continue...",
                        "\nStatus: It's your turn to make a move. Enter your command."]
            print(statuses[self.status])

    def print_snake(self):
        if len(self.snake) > 6:
            print(f"{self.snake[0]}{self.snake[1]}{self.snake[2]}...{self.snake[-3]}{self.snake[-2]}{self.snake[-1]}")
        else:
            print(f"{''.join(str(x) for x in self.snake)}")


game = Domino()
while not game.end_game:
    game.input_action(input())
