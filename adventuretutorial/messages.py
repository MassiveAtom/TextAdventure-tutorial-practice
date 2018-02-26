#!python3
import random

def output(message):
    with open('resources/text/' + message + '.txt', 'r') as the_message:
        the_message = the_message.read()
    print('\n================================\n')
    print(the_message)
    print('\n================================\n')


def list_output(message):
    with open('resources/text/' + message + '.txt', 'r') as the_message:
        the_message = the_message.readlines()
    choice = random.randrange(0, len(the_message))
    print('\n================================\n')
    print(the_message[choice])
    print('\n================================\n')