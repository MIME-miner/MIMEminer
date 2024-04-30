import config
import json
ops = [
    [".","remove_random_character",1],
    [".","replace_random_character",1],
    [".","insert_random_character",1],
    [".","change_character_case",1],
    [".","insert_character_pair",1]
]
with open("../../grammar/email_grammar.json", "r") as fp_grammar:
    grammar = json.load(fp_grammar)

black_list = ["entity-root"]

for node in grammar:
    if node in black_list:
        continue
    is_leaf = True
    for child in grammar[node]:
        # not leaf node
        if "<" in child:
            is_leaf = False
            break
    if is_leaf:
        ops.append([node,"remove_random_subtree",1])
        ops.append([node,"replace_random_subtree",1])
        ops.append([node,"insert_random_subtree",1])
    else:
        ops.append([node,"remove_random_character",1])
        ops.append([node,"replace_random_character",1])
        ops.append([node,"insert_random_character",1])
        ops.append([node,"change_character_case",1])
        ops.append([node,"insert_character_pair",1])



json.dump(ops,open("../../grammar/mutation_operators.json","w"))
