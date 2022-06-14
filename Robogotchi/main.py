import random


class NegativeNumberError(Exception):
    def __str__(self):
        return "The number can't be negative!"


class UpperBoundNumberError(Exception):
    def __str__(self):
        return "Invalid input! The number can't be bigger than 1000000."


class InvalidGameError(Exception):
    def __str__(self):
        return "\nPlease choose a valid option: " \
               "Numbers or Rock-paper-scissors?\n"


class Robogotchi:

    def __init__(self, battery, overheat, skills, boredom, name):
        self.battery = battery
        self.overheat = overheat
        self.skills = skills
        self.boredom = boredom
        self.name = name

    @classmethod
    def create_robopet(cls, name):
        return cls(100, 0, 0, 0, name)

    def play(self):
        new_boredom = 0 if self.boredom <= 20 else self.boredom - 20
        print(f"{self.name}'s level of boredom was {self.boredom}. "
              f"Now it is {new_boredom}.")
        self.boredom = new_boredom

        new_overheat = self.overheat + 10
        print(f"{self.name}'s level of overheat was {self.overheat}. "
              f"Now it is {new_overheat}.")
        self.overheat = new_overheat

        if self.boredom == 0:
            print(f'{self.name} is in a great mood!\n')

    def will_blow_up(self):
        return self.overheat + 10 >= 100

    def blow_up(self):
        print(f'The level of overheat reached 100, {self.name} has blown up!'
              f' Game over. Try again?')

    def recharge(self):
        if self.battery == 100:
            print(f'{self.name} is charged!\n')
        else:
            old_battery = self.battery
            self.battery += 10
            old_overheat = self.overheat
            self.overheat = 0 if self.overheat - 5 <= 0 else self.overheat - 5
            old_boredom = self.boredom
            self.boredom = 100 if self.boredom + 5 >= 100 else self.boredom + 5
            print(f"{self.name}'s level of overheat was {old_overheat}. "
                  f"Now it is {self.overheat}.")
            print(f"{self.name}'s level of battery was {old_battery}. "
                  f"Now it is {self.battery}.")
            print(f"{self.name}'s level of boredom was {old_boredom}. "
                  f"Now it is {self.boredom}.")
            print(f'{self.name} is recharged!')

    def sleep(self):
        if self.overheat > 0:
            print(f'{self.name} cooled off!')
            old_overheat = self.overheat
            self.overheat = 0 if self.overheat - 20 <= 0 else self.overheat - 20
            print(f"{self.name}'s level of overheat was {old_overheat}. "
                  f"Now it is {self.overheat}.\n")

        if self.overheat == 0:
            print(f'{self.name} is cool!\n')

    def get_info(self):
        print(f"{self.name}'s stats are:\n"
              f"battery is {self.battery},\n"
              f"overheat is {self.overheat},\n"
              f"skill level is {self.skills},\n"
              f"boredom is {self.boredom}.\n")


class Score:
    scores = {
        'win': 0,
        'loss': 0,
        'draw': 0
    }

    def __init__(self):
        self.reset_score()

    def reset_score(self):
        self.scores = {
            'win': 0,
            'loss': 0,
            'draw': 0
        }

    def print_score(self):
        print(f'\nYou won: {self.scores.get("win")},'
              f'\nThe robot won: {self.scores.get("loss")},'
              f'\nDraws: {self.scores.get("draw")}.\n')
        self.reset_score()

    def add_win_score(self):
        self.scores['win'] += 1
        print("You won!")

    def add_loss_score(self):
        self.scores['loss'] += 1
        print('The robot won!')

    def add_draw_score(self):
        self.scores['draw'] += 1
        print("It's a draw!")


def main():

    while True:
        print(f"Available interactions with {robot.name}:\n"
              f"exit - Exit\n"
              f"info - Check the vitals\n"
              f"recharge - Recharge\n"
              f"sleep - Sleep mode\n"
              f"play - Play\n")

        print("Choose:")
        user_choice = input()

        if user_choice not in robot_options:
            print('Invalid input, try again!')
        elif user_choice == 'exit':
            print('Game over')
            exit()
        elif user_choice == 'play':
            play_game()
        elif user_choice == 'recharge':
            robot.recharge()
        elif user_choice == 'sleep':
            robot.sleep()
        elif user_choice == 'info':
            robot.get_info()


def play_game():
    while True:
        try:
            print('Which game would you like to play?')
            user_input = input()

            if user_input == 'Numbers':
                play_numbers()
            elif user_input == 'Rock-paper-scissors':
                play_rps()
            else:
                raise InvalidGameError
        except InvalidGameError as err:
            print(err)


def play_rps():
    options = {'rock': {'wins': 'scissors', 'loses': 'paper'},
               'scissors': {'wins': 'paper', 'loses': 'rock'},
               'paper': {'wins': 'rock', 'loses': 'scissors'}}


    while True:
        print('\nWhat is your move?')
        user_input = input()
        if user_input == 'exit game':
            exit_game()
        elif user_input.lower() not in options:
            print('No such option! Try again!')
        else:
            robot_choice = random.choice(list(options.keys()))
            print(f'The robot chose {robot_choice}')

            if robot_choice == user_input:
                score.add_draw_score()
            elif options.get(robot_choice)['wins'] == user_input:
                score.add_loss_score()
            else:
                score.add_win_score()


def exit_game():
    if not robot.will_blow_up():
        score.print_score()
        robot.play()
        main()
    else:
        robot.blow_up()
        exit()


def play_numbers():
    random_number = random.randint(0, 1_000_000)
    while True:
        print('\nWhat is your number?')
        user_input = input()

        if user_input == 'exit game':
            exit_game()
        else:
            try:
                user_input = int(user_input)
                if user_input < 0:
                    raise NegativeNumberError
                elif user_input > 1_000_000:
                    raise UpperBoundNumberError
                else:
                    robot_input = random.randint(0, 1_000_000)
                    print(f'\nThe robot entered the number {robot_input}.')
                    print(f'The goal number is {random_number}.')

                    if (abs(user_input - random_number)
                            < abs(robot_input - random_number)):
                        score.add_win_score()
                    elif (abs(user_input - random_number)
                          > abs(robot_input - random_number)):
                        score.add_loss_score()
                    else:
                        score.add_draw_score()
            except ValueError:
                print("A string is not a valid input!")
            except NegativeNumberError as err:
                print(err)
            except UpperBoundNumberError as err:
                print(err)


if __name__ == '__main__':
    robot_options = ('play', 'exit', 'info', 'recharge', 'sleep')

    score = Score()
    print("How will you call your robot?")
    robot = Robogotchi.create_robopet(input())

    main()