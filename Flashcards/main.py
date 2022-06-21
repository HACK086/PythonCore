import random
import sys

cards = {}
errors = {}
log = ''


def log_input(message=None):
    global log
    if message is not None:
        log_print(message)
    user_input = input()
    log += user_input + '\n'
    return user_input


def log_print(message):
    global log
    print(message)
    log += message


def add_card():
    log_print(f'The card:')
    while True:
        term = log_input()
        if term not in cards:
            break
        log_print(f'The term "{term}" already exists. Try again:')
    log_print(f'The definition of the card!')
    while True:
        definition = log_input()
        if definition not in cards.values():
            break
        log_print(f'The definition "{definition}" already exists. Try again:')
    cards[term] = definition
    log_print(f'The pair ("{term}":"{definition}") has been added.\n')


def remove_card():
    term = log_input('Which card?')
    if cards.pop(term, None) is None:
        log_print(f'Can\'t remove "{term}": there is no such card.\n')
    else:
        log_print('The card has been removed.\n')


def import_cards(filename=None):
    try:
        with open(filename or log_input('File name:'), 'r') as f:
            new_cards = f.read().splitlines()
    except FileNotFoundError:
        log_print('File not found.\n')
        return
    for card in new_cards:
        term, definition = card.split('::')
        cards[term] = definition
    log_print(f'{len(new_cards)} cards have been loaded.\n')


def export_cards(filename=None):
    with open(filename or log_input('File name:'), 'w') as f:
        for term in cards:
            f.write(f'{term}::{cards[term]}\n')
    log_print(f'{len(cards)} cards have been saved.\n')


def ask_cards():
    for _ in range(int(log_input('How many times to ask?'))):
        term = random.choice(list(cards.keys()))
        guess = log_input(f'Print the definition of "{term}":')
        if guess == cards[term]:
            log_print('Correct!')
        else:
            correct_term = next((t for t in cards if cards[t] == guess), None)
            errors.setdefault(term, 0)
            errors[term] += 1
            if correct_term is not None:
                log_print(f'Wrong. The right answer is "{cards[term]}", but '
                          f'your definition is correct for "{correct_term}".')
            else:
                log_print(f'Wrong. The right answer is "{cards[term]}".')
    log_print('\n')


def save_log():
    with open(log_input('File name:'), 'w') as f:
        f.write(log)
    print('The log has been saved.\n')


def print_hardest_card():
    if errors:
        hardest_card = max(errors, key=lambda x: errors[x])
        log_print(f'The hardest card is "{hardest_card}. You have '
                  f'{errors[hardest_card]} errors answering it.')
    else:
        log_print('There are no cards with errors.\n')


def reset_stats():
    errors.clear()
    print('Card statistics have been reset.\n')


def main():
    import_file = next((arg[14:] for arg in sys.argv if 'import' in arg), None)
    export_file = next((arg[12:] for arg in sys.argv if 'export' in arg), None)
    if import_file is not None:
        import_cards(import_file)
    while True:
        command = log_input('Input the action (add, remove, import, export, '
                            'ask, exit, log, hardest card, reset stats):')
        if command == 'add':
            add_card()
        elif command == 'remove':
            remove_card()
        elif command == 'import':
            import_cards()
        elif command == 'export':
            export_cards()
        elif command == 'ask':
            ask_cards()
        elif command == 'log':
            save_log()
        elif command == 'hardest card':
            print_hardest_card()
        elif command == 'reset stats':
            reset_stats()
        else:
            log_print('Bye bye!')
            if export_file is not None:
                export_cards(export_file)
            return


if __name__ == '__main__':
    main()