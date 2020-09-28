import configparser
import json


config = configparser.ConfigParser()
config.read('config/config.ini')


def find_def_var(variable):
    return config['DEFAULT'][variable]


def find_star_var(variable):
    string = config['STARSHIP'][variable]
    if string[0] == '[':
        word_list = []
        word = ""
        for letter in string:
            if letter == ',' or letter == ']':
                word = word.strip()
                word_list.append(word)
                word = ""
            elif not letter == '[':
                word += letter
        return word_list
    return string
