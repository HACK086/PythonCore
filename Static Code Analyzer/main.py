import ast
import os
import string
import sys


def process_file(path):
    with open(path, 'r') as f:
        text = f.read()

    empty_lines = 0
    for i, line in enumerate(text.splitlines()):
        if len(line) > 79:
            print(f'{path}: Line {i + 1}: S001 Too long')
        if (len(line) - len(line.lstrip())) % 4 != 0:
            print(f'{path}: Line {i + 1}: S002 Wrong indentation')
        if (line[:line.find('#')] if '#' in line else line).strip().endswith(';'):
            print(f'{path}: Line {i + 1}: S003 Unnecessary semicolon')
        if '#' in line and not line.startswith('#') and '  #' not in line:
            print(f'{path}: Line {i + 1}: S004 Spaces before inline comments')
        if '#' in line and line.find('#') < line.lower().find('todo'):
            print(f'{path}: Line {i + 1}: S005 TODO found')
        if line.strip() == '':
            empty_lines += 1
        else:
            if empty_lines > 2:
                print(f'{path}: Line {i + 1}: S006 More than two empty lines')
            empty_lines = 0
        if line.strip().startswith('def  ') or line.startswith('class  '):
            print(f'{path}: Line {i + 1}: S007 Many spaces after construct')

    tree = ast.parse(text)
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            class_name = node.name
            if '_' in class_name or class_name[
                0] not in string.ascii_uppercase:
                print(f'{path}: Line {node.lineno}: S008 Class name CamelCase')
        elif isinstance(node, ast.FunctionDef):
            function_name = node.name
            if any(char in string.ascii_uppercase for char in function_name):
                print(f'{path}: Line {node.lineno}: S009 Function snake_case')
            for arg in node.args.args:
                if any(char in string.ascii_uppercase for char in arg.arg):
                    print(f'{path}: Line {node.lineno}: S010 Arg snake_case')
                    break
            for default in node.args.defaults:
                if isinstance(default, ast.List):
                    print(f'{path}: Line {node.lineno}: S012 Mutable default')
                    break
        elif isinstance(node, ast.Assign):
            for var in node.targets:
                if isinstance(var, ast.Name):
                    if any(char in string.ascii_uppercase for char in var.id):
                        print(f'{path}: Line {node.lineno}: S011 snake_case')
                elif isinstance(var, ast.Attribute):
                    if any(char in string.ascii_uppercase for char in var.attr):
                        print(f'{path}: Line {node.lineno}: S011 snake_case')


def main():
    if sys.argv[1].endswith('py'):
        process_file(sys.argv[1])
    else:
        for file_name in os.listdir(sys.argv[1]):
            if file_name.endswith('py'):
                process_file(os.path.join(sys.argv[1], file_name))


if __name__ == '__main__':
    main()