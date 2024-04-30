import os
import json
import random
import config as cfg
from model.input_tree import InputTree
from helper_functions import print_hint


mutation_log = {}
att_dict = {}


# Sample Generation: Construct + Mutate
class Generator:
    def __init__(self, verbose, seeds, outfilename, seedfile):
        self.verbose = verbose
        self.seeds = seeds
        # self.lock = threading.Lock()
        self.outfilename = outfilename
        self.seedfile = seedfile
        with open(cfg.grammar_path, "r") as fp_grammar:
            self.grammar = json.load(fp_grammar)
        with open(cfg.mutation_info_path, "r") as fp_mutation:
            self.mutation_info = json.load(fp_mutation)

    def generate_input(self, seed)->InputTree:
        # Construct ==============
        base_input = InputTree(self.grammar, seed, False)
        base_input.build_tree(base_input.root)          # complete request sample formed
        att_dict[seed] = base_input.att_list.copy()

        #sample_content = base_input.tree_to_msg()

        # if not os.path.exists(cfg.origin_dir):
        #     os.makedirs(cfg.origin_dir)
        # with open(os.path.join(cfg.origin_dir, str(seed) + "_origin.eml"), "wb") as fp_origin:
        #     fp_origin.write(sample_content)
        # if self.verbose:
        #     print(str(sample_content, encoding="utf8"))
        #     print_hint("===== Mutating Original Sample ... =====")
        return base_input


if __name__ == "__main__":
    seed_l = 18
    seed_r = seed_l + 1
    # seed_l, seed_r = 0, 20
    for seed in range(seed_l, seed_r):
        print_hint(">>> Random Seed: %d." % seed)
        sample_generator = Generator(True, [], cfg.out_file, cfg.seed_file)
        sample_generator.generate_input(seed, f_plot=True, verbose=sample_generator.verbose)

    with open(cfg.mutation_log_path, "w") as mutation_fp:
        for seed in range(seed_l, seed_r):
            for msg in mutation_log[seed]:
                mutation_fp.write("[{}] {}\n".format(seed, msg))
            mutation_fp.write("\n")

    with open(cfg.att_dict_path, "w") as att_fp:
        json.dump(att_dict, att_fp, indent=2)
