from helper_functions import print_hint
from generator import Generator
from model.input_tree import InputTree
from mutator  import Mutator
import config
from random import randint
from copy import deepcopy
from os import path
from subprocess import Popen
from diff_detect import valid_diff_among_parsers
from targets_config import fuzz_targets
import json
import random


def fuzzOneInput(sample, fuzz_targets, sample_id):
    # for target in fuzz_targets:
    #     target(sample)
    sample_path = path.join(config.mutated_dir, "sample_" + str(sample_id))
    open(sample_path, "wb").write(sample)

    for target_name in fuzz_targets:
        target = fuzz_targets[target_name]
        p = Popen(target["execute_str"].format(input_path=sample_path, output_path=path.join(config.extract_dest_path, target["name"])), cwd=target["cwd"], shell=True)
        p.wait()

    diff = valid_diff_among_parsers(config.extract_dest_path)
    return diff


def load_mutations_operators(path):
    with open(path, "r") as fp:
        return json.load(fp)


def generate_input(seed, count):
    sample_generator = Generator(True, [], config.out_file, config.seed_file)

    for i in range(count):
        input = sample_generator.generate_input(seed)
        yield input, i
    pass


def save_file(path, sample):
    with open(path, "w") as fp:
        fp.write(sample.tree_to_msg(sample))


def random_op_with_weights(possible_ops):
    probabilities = [0] * len(possible_ops)
    op_ids = range(len(possible_ops))
    for index, (selector, operator, priority) in enumerate(possible_ops):
        probabilities[index] = float(priority)

    probabilities = [(1 - sum(probabilities)) / probabilities.count(0) if elem == 0 else elem for elem in probabilities]

    op_id = random.choices(op_ids, weights=probabilities)[0]

    return op_id


def main():
    # seed_l, seed_r = 0, 20
    seed = randint
    TOTAL = 5000
    PUNISH_THRESHOLD = 10
    mutations_operators = load_mutations_operators(config.mutations_ops_path)
    reward_rate = 0.1
    punishment_rate = 0.1
    op_scoreboard = {}

    for sample, sample_id in generate_input(seed, TOTAL):
        op_id = random_op_with_weights(mutations_operators)

        selector = mutations_operators[op_id][0]
        operator = mutations_operators[op_id][1]

        mutator = Mutator(verbose=True, _input=sample)
        mutated_input: InputTree = mutator.mutate_input(selector, operator)

        data = mutated_input.tree_to_msg()

        ok = fuzzOneInput(data, fuzz_targets, sample_id)

        if ok:
            mutations_operators[op_id][3] += reward_rate
            save_file(config.filtered_result_path, sample)
        else:
            key = selector + operator
            if op_scoreboard.get(key) is None:
                op_scoreboard[key] = 1
            else:
                op_scoreboard[key] += 1
            if op_scoreboard[key] > PUNISH_THRESHOLD:
                mutations_operators[op_id][3] -= punishment_rate

    json.dump(op_scoreboard, open(config.mutations_ops_path, "w"), indent=2)


if __name__ == "__main__":
    main()
