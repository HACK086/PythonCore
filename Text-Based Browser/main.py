import os
import sys


nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created "soft" magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''


# write your code here
def main():
    count = 0
    args = sys.argv
    directory = args[1]
    if not os.access(directory, mode=os.F_OK):
        os.mkdir(directory)
    while True:
        user_inp = input()
        if user_inp == "nytimes.com":
            print(nytimes_com)
            count = 1
            with open(f"{directory}/nytimes", 'w', encoding='utf-8') as file:
                file.write(nytimes_com)
        elif user_inp == "bloomberg.com":
            print(bloomberg_com)
            count = 2
            with open(f"{directory}/bloomberg", 'w', encoding='utf-8') as file:
                file.write(bloomberg_com)
        elif user_inp == "exit":
            break
        elif user_inp == 'back':
            if count == 1:
                print(bloomberg_com)
            else:
                print(nytimes_com)
        else:
            print("Error")
    if not bool(os.listdir(directory)):
        os.rmdir(directory)


if __name__ == "__main__":
    main()