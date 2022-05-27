import hashlib
import os
import sys

no_args_message = 'Directory is not specified'
file_format_message = 'Enter file format:'
sorting_option_menu_01 = 'Size sorting options:'
sorting_option_menu_02 = '1. Descending'
sorting_option_menu_03 = '2. Ascending'
sorting_option_message = 'Enter a sorting option:'
wrong_option_message = 'Wrong option'
asking_for_duplicates_message = 'Check for duplicates?'


def ask_sorting():
    print()
    print(sorting_option_menu_01, sorting_option_menu_02, sorting_option_menu_03, sep='\n')
    print()
    print(sorting_option_message)
    choice = int(input())
    assert 0 < choice < 3, wrong_option_message
    return choice


def build_sizes(main_dir, file_format):
    unsorted_sizes = {}
    no_file_format = len(file_format) == 0
    for root, _, files in os.walk(main_dir, topdown=True):
        for name in files:
            fullname = os.path.join(root, name)
            ext = os.path.splitext(fullname)[1]
            if (file_format == ext[1:]) or no_file_format:
                try:
                    (unsorted_sizes[os.path.getsize(fullname)]).append(fullname)
                except KeyError:
                    unsorted_sizes[os.path.getsize(fullname)] = [fullname]
    return unsorted_sizes


def sort_sizes(sizes, descending=True):
    sorted_sizes = []
    for key in sizes:
        sorted_sizes.append((key, sizes[key]))
    sorted_sizes.sort(reverse=descending)
    return sorted_sizes


def print_sizes(sizes):
    for size in sizes:
        print(f'\n{size[0]} bytes')
        print(*(size[1]), sep='\n')


def compute_file_hash(hash_name, file_name):
    m = hashlib.new(hash_name)
    with open(file_name, 'rb') as file_in:
        m.update(file_in.read())
    return m.hexdigest()


def build_hashes(sizes):
    full_list = []
    i = 1
    for size in sizes:
        hashes = {}
        max_n = 0
        for file_name in size[1]:
            digest = compute_file_hash('md5', file_name)
            try:
                ((hashes[digest])['files']).append(file_name)
                hashes[digest]['duplicates'] += 1
                max_n = max(max_n, hashes[digest]['duplicates'])
            except KeyError:
                hashes[digest] = {'files': [file_name], 'duplicates': 0}
        full_list.append((size[0], max_n, hashes))
        i += 1
    return full_list


def filter_duplicates(hashes):
    sizes_with_duplicates = [x for x in hashes if x[1] > 0]
    new_sizes = []
    for size in sizes_with_duplicates:
        new_sizes.append((size[0], size[1], {k: v for (k, v) in size[2].items() if size[2][k]['duplicates'] > 0}))
    return new_sizes


def print_duplicates(duplicates):
    i = 1
    for size in duplicates:
        print(f'\n{size[0]} bytes')
        for digest in size[2]:
            print(f'Hash: {digest}')
            for file_name in size[2][digest]['files']:
                print(f'{i}. {file_name}')
                i += 1


def asking_for_duplicates():
    print(f'\n{asking_for_duplicates_message}')
    choice = input()
    assert choice == 'yes' or choice == 'no', wrong_option_message
    return True if choice == 'yes' else False


def main():
    args = sys.argv
    choice = -1
    go_on = True
    ask_sorting_again = True
    ask_duplicates_again = True
    duplicate_choice = False
    try:
        assert len(args) > 1, no_args_message
    except AssertionError as ae:
        go_on = False
        print(ae)
    if go_on:
        print(file_format_message)
        file_format = input()
        while ask_sorting_again:
            try:
                choice = ask_sorting()
                ask_sorting_again = False
            except ValueError:
                ask_sorting_again = True
                print()
                print(wrong_option_message)
            except AssertionError as ae:
                ask_sorting_again = True
                print()
                print(ae)

        sizes = build_sizes(args[1], file_format)
        desc = True if choice == 1 else False
        sorted_sizes = sort_sizes(sizes, desc)
        print_sizes(sorted_sizes)

        while ask_duplicates_again:
            try:
                duplicate_choice = asking_for_duplicates()
                ask_duplicates_again = False
            except AssertionError as ae:
                ask_duplicates_again = True
                print()
                print(ae)
        if duplicate_choice:
            hashes = build_hashes(sorted_sizes)
            duplicates = filter_duplicates(hashes)
            print_duplicates(duplicates)


if __name__ == '__main__':
    main()