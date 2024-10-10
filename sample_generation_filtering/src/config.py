import os

grammar_path = "../grammar/email_grammar.json"
mutation_info_path = "../grammar/symbol_mutation_info.json"

seed_file = "seed.txt"
out_file = "out.txt"

sample_dir = "../out/sample/"
origin_dir = "../out/sample/origin/"
mutated_dir = "../out/sample/mutated/"
mutation_log_path = "../out/sample/mutation.txt"
att_dict_path = r"../out/sample/attachment.json"

refer_att_path = {
    "7bit": "../misc/reference/text_data",
    "base64": "../misc/reference/binary_data",
    "quoted-printable": "../misc/reference/binary_data"
}
standard_refer_path = "../misc/reference/eicar"

sample_stage = "mutated"
extract_source_path = sample_dir + sample_stage + "/"
# extract_dest_path = os.path.join("../extracts/", "att_extract_from_" + sample_stage + "/")
extract_dest_path = "../out/extract"
extract_err_path = os.path.join(extract_dest_path, "err.txt")

parser_diff_path = os.path.join("../out/", sample_stage + "_parser_diff.txt")
refer_diff_path = os.path.join("../out/", sample_stage + "_refer_diff.txt")
valid_diff_path = os.path.join("../out/", sample_stage + "_valid_diff.txt")

filtered_result_path = os.path.join("../out/","filtered_result")
mutations_ops_path = "../grammar/mutation_operators.json"


tree_graph_path = "../out/plot/"


# FOR MUTATOR ========

min_num_mutations = 1
max_num_mutations = 1
# The character pool to choose from for insert_random_char and replace_random_char operations.
char_pool = ['\x00', '\x01', '\x02', '\x03', '\t', '\n', '\x0b', '\x0c', '\r', '\x0e', '\x0f', '\x10', '\x11', '\x12', '\x13', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'Q', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'q', 'x', 'y', 'z', '{', '|', '}', '~', '\x7f']
char_group_pool = ['\r\n', ]
pair_pool = [('(', ')'), ('\"', '\"'), ('[', ']'), ('{', '}'), ('<', '>'), ('\'', '\''), ]
# If not specified, the set of children nodes will be used as the pool.
symbol_pool = ['<space>', '<CRLF>']

