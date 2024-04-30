import os
import sys
import linecache
import random
import config as cfg
from model.input_tree_node import Node


def random_choose_with_weights(possible_expansions):
    probabilities = [0] * len(possible_expansions)
    for index, expansion in enumerate(possible_expansions):
        if isinstance(expansion, str) and "prob=" in expansion:
            probability = expansion[expansion.find("prob=") + 5:expansion.find(")")]
            probabilities[index] = float(probability)

    probabilities = [(1 - sum(probabilities)) / probabilities.count(0) if elem == 0 else elem for elem in probabilities]

    chosen_expansion = random.choices(possible_expansions, weights=probabilities)[0]
    if isinstance(chosen_expansion, str) and chosen_expansion.startswith('('):
        chosen_expansion = chosen_expansion.split(',')[0][1:]

    return chosen_expansion


def get_node_by_symbol(node_queue, symbol):
    for i in range(len(node_queue) - 1, -1, -1):
        if node_queue[i].symbol == symbol:
            return node_queue[i]


def print_hint(str, color="blue"):
    if color == "blue":
        print("\n\033[94m" + str + "\033[0m")
    elif color == "red":
        print("\n\033[91m" + str + "\033[0m")
    else:
        print("\n" + str)

def _print_exception(str):
    print_hint(str, "red")

cur_serial = "0"
