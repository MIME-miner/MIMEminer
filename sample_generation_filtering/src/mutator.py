import random
import copy
import config
from model.input_tree_node import Node
from model.input_tree import InputTree
from helper_functions import _print_exception, random_choose_with_weights, print_hint
import json

class Mutator:

    def __init__(self, verbose, _input:InputTree,):
        with open(config.grammar_path, "r") as fp_grammar:
            self.grammar = json.load(fp_grammar)
        self.verbose = verbose
        self.input = _input
        self.mutation_messages = []

    def mutate_input(self,selector,operator):
        try:
            node_to_mutate_pool = []

            for node in self.input.nonterminal_node_list.values():
                if node.symbol == selector:
                    node_to_mutate_pool.append(node)


            node_to_mutate = random.choice(node_to_mutate_pool)

            self.__getattribute__(operator)(node_to_mutate, self.verbose)

        except Exception as exception:
            _print_exception()
            raise exception

    def remove_random_character(self, node, verbose=False):
        """Remove a character at a random position"""
        s = node.children[0].symbol  # why children[0] ?
        if s:
            pos = random.randint(0, len(s) - 1)
            self.mutation_messages.append(
                "Removing character {} at pos {} of {}.".format(repr(s[pos]), pos, node.symbol))
            node.children[0].symbol = s[:pos] + s[pos + 1:]
            return True
        else:
            return False

    def insert_random_character(self, node, verbose=False):
        """Insert a random character at a random position"""
        s = node.children[0].symbol
        if s:
            pos = random.randint(0, len(s) - 1)
            # random_character = chr(random.randrange(0, 127))
            random_character = random_choose_with_weights(config.char_pool)
            self.mutation_messages.append(
                "Inserting character {} at pos {} of {}.".format(repr(random_character), pos, node.symbol))
            node.children[0].symbol = s[:pos] + random_character + s[pos:]
            return True
        else:
            return False

    def replace_random_character(self, node, verbose=False):
        """Replace a character at a random position with a random character"""
        s = node.children[0].symbol
        if s:
            pos = random.randint(0, len(s) - 1)
            random_character = random_choose_with_weights(config.char_pool)
            self.mutation_messages.append(
                "Replacing character {} at pos {} with {}.".format(repr(node.symbol), pos, repr(random_character)))
            node.children[0].symbol = s[:pos] + random_character + s[pos + 1:]
            return True
        else:
            return False

    def change_character_case(self, node, verbose=False):
        """Change the case of a random character"""
        s = node.children[0].symbol
        if s:
            pos = random.randint(0, len(s) - 1)
            if not s[pos].isalpha():
                return False
            self.mutation_messages.append("Changing case of character {} at pos {}.".format(repr(node.symbol), pos))
            node.children[0].symbol = s[:pos] + s[pos].swapcase() + s[pos + 1:]
            return True
        else:
            return False

    def insert_character_pair(self, node, verbose=False):
        """Insert a character pair at a random position"""
        s = node.children[0].symbol
        if s:
            pos1 = random.randint(0, len(s))
            pos2 = random.randint(pos1, len(s))
            random_pair = random.choice(config.pair_pool)
            self.mutation_messages.append(
                "Inserting character pair {} at pos {}, {} of {}.".format(repr(random_pair[0] + random_pair[1]), pos1,
                                                                          pos2, node.symbol))
            node.children[0].symbol = s[:pos1] + random_pair[0] + s[pos1:pos2] + random_pair[1] + s[pos2:]
            return True
        else:
            return False

    def remove_random_subtree(self, node, verbose=False):
        """Remove a subtree at a random position under a given node"""
        if node.children:
            pos = random.randint(0, len(node.children) - 1)
            self.mutation_messages.append(
                "Removing subtree {} under {}.".format(repr(node.children[pos].symbol), repr(node.symbol)))

            # Remove the node and its children also from the node list
            self.input.remove_subtree_from_nodelist(node.children[pos])
            node.children = node.children[:pos] + node.children[pos + 1:]
            return True
        else:
            return False

    def replace_random_subtree(self, node, verbose=False):
        """Update a subtree at a random position under a given node
          with a subtree expanded from a symbol chosen randomly
          from the list of symbols"""
        if node.children:
            pos = random.randint(0, len(node.children) - 1)
            # if hasattr(config, 'symbol_pool'):
            #     random_symbol = random_choose_with_weights(config.symbol_pool)
            # else:
            #     random_symbol = random.choice([_node.symbol for _node in node.children])

            random_symbol_pool = [_node.symbol for _node in node.children]     # choose from existing nodes (repetition)
            if hasattr(config, 'symbol_pool'):
                random_symbol_pool = config.symbol_pool + random_symbol_pool

            random_symbol = None
            while random_symbol not in self.grammar:
                random_symbol = random_choose_with_weights(random_symbol_pool)

            random_subtree_root = Node(random_symbol, None)
            if random_symbol in self.input.grammar["entity-root"]:
                random_subtree_root.entity_root = random_subtree_root
            else:
                random_subtree_root.entity_root = node.entity_root
            random_subtree = self.input.build_tree(random_subtree_root, mode=1)

            self.mutation_messages.append(
                "Replacing subtree {} under {} with {}.".format(repr(node.children[pos].symbol), repr(node.symbol),
                                                                repr(random_symbol)))
            # Remove the node and its children also from the node list
            self.input.remove_subtree_from_nodelist(node.children[pos])
            node.children = node.children[:pos] + [random_subtree] + node.children[pos + 1:]
            return True
        else:
            return False

    def insert_random_subtree(self, node, verbose=False):                               # To be modified
        """Insert a subtree at a random position under a given node;
          inserted subtree is expanded from a symbol chosen randomly
          from the list of symbols"""
        if node.children:
            pos = random.randint(0, len(node.children) - 1)

            random_symbol_pool = [_node.symbol for _node in node.children]
            if hasattr(config, 'symbol_pool'):
                random_symbol_pool = config.symbol_pool + random_symbol_pool

            random_symbol = None
            while random_symbol not in self.grammar:
                random_symbol = random_choose_with_weights(random_symbol_pool)

            random_subtree_root = Node(random_symbol, None)
            if random_symbol in self.input.grammar["entity-root"]:
                random_subtree_root.entity_root = random_subtree_root
            else:
                random_subtree_root.entity_root = node.entity_root
            random_subtree = self.input.build_tree(random_subtree_root, mode=1)

            self.mutation_messages.append(
                "Inserting subtree {} at pos {} of {}.".format(repr(random_symbol), pos, repr(node.symbol)))
            node.children = node.children[:pos] + [random_subtree] + node.children[pos:]
            return True
        else:
            return False

    # is replace/insert random NODE necessary ? (instead of simply replace/insert the whole subtree)
