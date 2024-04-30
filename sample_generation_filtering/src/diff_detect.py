import json
import os
import re
import filecmp
import config as cfg

# 差异类型：0parser输出目录缺失 1文件数量不同 2文件名不同 3文件内容不同
parser_diff = {}
refer_diff = {}
valid_diff = {}
no_valid_diff = []


def diff_detected(diff_record, eml_name, diff):
    if eml_name in diff_record.keys():
        diff_record[eml_name].append(diff)
    else:
        diff_record[eml_name] = [diff]


def standard_cmp(path):
    res = 0
    for att in os.listdir(path):
        if filecmp.cmp(os.path.join(path, att), cfg.standard_refer_path):
            res += 1
    return res


def parser_refer_cmp(parser, att_path, refer_att_list):
    same_flag = True
    eml_name = os.path.basename(att_path)
    path = os.path.join(att_path, parser)
    file_set = set(os.listdir(path))

    for i in range(len(refer_att_list)):
        refer_att_name = "att_" + str(i + 1)
        if refer_att_name not in file_set:
            diff_detected(refer_diff, eml_name, "{} not exist in output from {}.".format(refer_att_name, parser))
            same_flag = False
            continue

        if filecmp.cmp(cfg.refer_att_path[refer_att_list[i]], os.path.join(path, refer_att_name)) is False:
            diff_detected(refer_diff, eml_name, "{} from {} unmatched with reference.".format(refer_att_name, parser))
            same_flag = False
    return same_flag


def two_parser_cmp(parser1, parser2, att_path):
    same_flag = True
    remove_ext = True
    eml_name = os.path.basename(att_path)
    path1 = os.path.join(att_path, parser1)
    path2 = os.path.join(att_path, parser2)

    if remove_ext:
        file_dict1 = dict((os.path.splitext(f)[0], f) for f in os.listdir(path1))
        file_dict2 = dict((os.path.splitext(f)[0], f) for f in os.listdir(path2))
    else:
        file_dict1 = dict((f, f) for f in os.listdir(path1))
        file_dict2 = dict((f, f) for f in os.listdir(path2))
    file_set1 = set(file_dict1.keys())
    file_set2 = set(file_dict2.keys())

    # 附件数量是否相同
    # if len(file_set1) != len(file_set2):
    #     diff_detected(eml_name, "Attachment number unmatched between parser {} and {}.".format(parser1, parser2))
    #     same_flag = False

    # 有哪几个文件不同时存在于两个目录中
    common_file = file_set1.intersection(file_set2)
    not_in_set2 = file_set1.difference(file_set2)
    not_in_set1 = file_set2.difference(file_set1)
    if len(not_in_set2) != 0:
        diff_detected(parser_diff, eml_name,
                      "{} from {} not exist in output from {}.".format(not_in_set2, parser1, parser2))
        same_flag = False
    if len(not_in_set1) != 0:
        diff_detected(parser_diff, eml_name,
                      "{} from {} not exist in output from {}.".format(not_in_set1, parser2, parser1))
        same_flag = False

    # 对比文件内容 只对文件名相同的文件集合进行比较
    # match, mismatch, error = filecmp.cmpfiles(path1, path2, common=common_file)
    mismatch = []
    for cf in common_file:
        f1 = file_dict1[cf]
        f2 = file_dict2[cf]
        if not filecmp.cmp(os.path.join(path1, f1), os.path.join(path2, f2)):
            mismatch.append(cf)
    if len(mismatch) != 0:
        diff_detected(parser_diff, eml_name,
                      "{} unmatched between parser {} and {}.".format(mismatch, parser1, parser2))
        same_flag = False

    return same_flag


def att_output_cmp(att_path):
    same_flag = True
    eml_name = os.path.basename(att_path)
    # subdirs = os.listdir(att_path)
    # if set(subdirs) != set(cfg.parser_list):
    #     diff_detected(parser_diff, eml_name, "Sub dirs not equal to parser list.")
    #     same_flag = False

    parser_num = len(cfg.parser_list)
    for i in range(parser_num):
        for j in range(i + 1, parser_num):
            if two_parser_cmp(cfg.parser_list[i], cfg.parser_list[j], att_path) is False:
                same_flag = False

    if same_flag:
        print(att_path)
    return same_flag


def att_refer_cmp(att_path, att_list):
    same_flag = True
    for parser in cfg.parser_list:
        if parser_refer_cmp(parser, att_path, att_list) is False:
            same_flag = False
    return same_flag


def exist_valid_diff(att_path, seed):
    valid_diff_flag = False
    standard_num = {}
    for i in range(len(cfg.parser_list)):
        parser = cfg.parser_list[i]
        standard_num[parser] = standard_cmp(os.path.join(att_path, parser))
        if i >= 1 and (standard_num[cfg.parser_list[i]] != standard_num[cfg.parser_list[i - 1]]):
            valid_diff_flag = True
    if valid_diff_flag:
        valid_diff[seed] = standard_num
    else:
        no_valid_diff.append(seed)
    return valid_diff_flag


if __name__ == "__main__":
    eml_list = os.listdir(cfg.extract_dest_path)

    # refer_cmp_flag = "origin" in cfg.extract_dest_path      # 对于mutated，没有标准参考可言 因此只有parser_diff
    refer_cmp_flag = False
    valid_cmp_flag = True
    with open(cfg.att_dict_path, "r") as fp_att:
        att_dict = json.load(fp_att)

    print("\nConsistent samples:")
    # for eml in tqdm(eml_list):
    for eml in eml_list:
        seed = re.sub(r'_.*', "", eml)
        eml_att_path = os.path.join(cfg.extract_dest_path, eml)
        if not os.path.isdir(eml_att_path):
            continue

        att_output_cmp(eml_att_path)
        if refer_cmp_flag:
            att_refer_cmp(eml_att_path, att_dict[seed])
        if valid_cmp_flag:
            exist_valid_diff(eml_att_path, seed)

    with open(cfg.parser_diff_path, "w") as diff_fp:
        for key, value in parser_diff.items():
            diff_fp.write(">>> " + key + "\n")
            for diff in value:
                diff_fp.write(diff + "\n")
            diff_fp.write("\n")
    print("\nDifference between parsers detected from {} email samples.".format(len(parser_diff)))

    if refer_cmp_flag:
        with open(cfg.refer_diff_path, "w") as diff_fp:
            for key, value in refer_diff.items():
                diff_fp.write(">>> " + key + "\n")
                for diff in value:
                    diff_fp.write(diff + "\n")
                diff_fp.write("\n")
        print("Difference from reference detected from {} email samples.".format(len(refer_diff)))

        parser_diff_sample = set(parser_diff.keys())
        refer_diff_sample = set(refer_diff.keys())
        print("Distinctive parser diff: ", len(parser_diff_sample.difference(refer_diff_sample)))
        print("Distinctive refer diff: ", len(refer_diff_sample.difference(parser_diff_sample)))

    if valid_cmp_flag:
        with open(cfg.valid_diff_path, "w") as valid_fp:
            valid_fp.write(">>> valid diff detected in samples below:\n")
            for key, value in valid_diff.items():
                valid_fp.write(key + "  " + str(value) + "\n")
            valid_fp.write("\n>>> valid diff not detected in samples below:\n")
            for seed in no_valid_diff:
                valid_fp.write(seed + "\n")
        print("Valid difference: ", len(valid_diff))
