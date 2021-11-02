# -*- coding: utf-8 -*-
import json
import random

# Give a Json file and return a List

# voir https://www.reddit.com/r/CompetitiveHS/comments/dtintp/hearthstone_battlegrounds_composition_guide/


def read_values_from_json(path, key):
    values = []
    with open(path) as f:
        data = json.load(f)
        for entry in data:
            values.append(entry[key])
        return values

# Give a json and return a list


def clean_strings(sentences):
    cleaned = []
    # Store compo on a list. Create an empty list and add each sentence one by one.
    for sentence in sentences:
        # Clean compo from whitespace and so on
        clean_sentence = sentence  # .strip ????
        # don't use extend as it adds each letter one by one!
        cleaned.append(clean_sentence)
    return cleaned

# Return a random item in a list


def random_item_in(object_list):
    rand_numb = random.randint(0, len(object_list) - 1)
    return object_list[rand_numb]

# Return a random value from a json file


def random_value(source_path, key):
    all_values = read_values_from_json(source_path, key)
    clean_values = clean_strings(all_values)
    return random_item_in(clean_values)


#####################
###### compo #######
#####################


def random_compo():
    return random_value('compo.json', 'compo')

######################
#### CHARACTERS ######
######################

# Gather characters from Wikipedia


def random_character():
    return random_value('characters.json', 'character')


######################
#### INTERACTION ######
######################

# Print a random sentence.

def print_random_sentence():
    rand_compo = random_compo()
    rand_character = random_character()
    print("Si tu joues {} alors tente : {}".format(rand_character, rand_compo))


def main_loop():
    while True:
        print_random_sentence()
        message = ('Voulez-vous voir une autre compo ? '
                   'Pour sortir du programme, tapez [B].')
        choice = input(message).upper()
        if choice == 'B':
            break
            # This will stop the loop!


if __name__ == '__main__':
    main_loop()
