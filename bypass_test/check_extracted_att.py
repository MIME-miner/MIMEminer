import os
import re

# modify this part to for different test --------------------------------
import test_samples.test_cases as cases
# import bhv_test_cases.specific_payload as payloads
case_result = {case_id: "" for case_id in list(cases.test_cases.keys())}
# case_result = {case_id: "" for case_id in payloads.specific_payload["b64_related"]["wncr"]}

att_dir = "../downloaded_att/"
ref_original_path = "../test_samples/eicar/eicar_com"
ref_undecoded_path = "../test_samples/eicar/basic_qp_eicar"
# -----------------------------------------------------------------------

bypass_subdir = os.path.join(att_dir, "bypass")
undecoded_subdir = os.path.join(att_dir, "undecoded")
start_header_subdir = os.path.join(att_dir, "start_header")
mp_body_subdir = os.path.join(att_dir, "mp_body")
empty_subdir = os.path.join(att_dir, "empty")
cnt_dict = {"bypass": 0, "weak_bypass_partial": 0, "undecoded": 0, "undecoded_partial": 0,
            "undecoded_with_diff_crlf": 0, "start_Type": 0, "start_Encoding": 0, "start_Disposition": 0,
            "empty": 0, "mp_body": 0, "unknown": 0}

# if subdir not exists, create it
if not os.path.exists(bypass_subdir):
    os.mkdir(bypass_subdir)
if not os.path.exists(undecoded_subdir):
    os.mkdir(undecoded_subdir)
if not os.path.exists(start_header_subdir):
    os.mkdir(start_header_subdir)
if not os.path.exists(mp_body_subdir):
    os.mkdir(mp_body_subdir)
if not os.path.exists(empty_subdir):
    os.mkdir(empty_subdir)

with open(ref_original_path, "rb") as fp:
    ref_original = fp.read()
with open(ref_undecoded_path, "rb") as fp:
    ref_undecoded = fp.read()

unmatched_case_result = {}
case_result_cnt = 0

# patterns = [re.compile("-att\d+"), re.compile("_b64"), re.compile("_qp")]
patterns = [(re.compile(r"-att\d+"), ""), (re.compile(r"\.bin"), ""), (re.compile(r"\.txt"), ""),
            (re.compile(r"\.exe"), ""),
            (re.compile(r"cte_"), "CTE_")]

file_list = os.listdir(att_dir)
file_list = [f for f in file_list if os.path.isfile(os.path.join(att_dir, f)) and not f.startswith(".")]
print("Total:", len(file_list), " ---------")

for f in file_list:
    case_name = f
    for p, rpl in patterns:
        case_name = re.sub(p, rpl, case_name)
    # read file

    with open(os.path.join(att_dir, f), "rb") as fp:
        content = fp.read()

    # compare with reference
    if content == ref_original:
        f_result = "bypass"
        os.rename(os.path.join(att_dir, f), os.path.join(bypass_subdir, f))
        cnt_dict["bypass"] += 1
    # if ref_original is part of content
    elif content.find(ref_original) == 0:
        f_result = "weak_bypass_partial"
        os.rename(os.path.join(att_dir, f), os.path.join(bypass_subdir, f))
        cnt_dict["weak_bypass_partial"] += 1
    elif content == ref_undecoded:
        f_result = "undecoded"
        os.rename(os.path.join(att_dir, f), os.path.join(undecoded_subdir, f))
        cnt_dict["undecoded"] += 1
    elif content.find(ref_undecoded) == 0:
        f_result = "undecoded_partial"
        os.rename(os.path.join(att_dir, f), os.path.join(undecoded_subdir, f))
        cnt_dict["undecoded_partial"] += 1
    # if difference between content and ref only lies in CRLF
    elif content.replace(b"\n", b"") == ref_undecoded.replace(b"\r\n", b""):
        f_result = "undecoded_with_diff_crlf"
        os.rename(os.path.join(att_dir, f), os.path.join(undecoded_subdir, f))
        cnt_dict["undecoded_with_diff_crlf"] += 1
    elif content.startswith(b"Content-Type:"):
        f_result = "start_Type"
        os.rename(os.path.join(att_dir, f), os.path.join(start_header_subdir, f))
        cnt_dict["start_Type"] += 1
    elif content.startswith(b"Content-Transfer-Encoding:"):
        f_result = "start_Encoding"
        os.rename(os.path.join(att_dir, f), os.path.join(start_header_subdir, f))
        cnt_dict["start_Encoding"] += 1
    elif content.startswith(b"Content-Disposition:"):
        f_result = "start_Disposition"
        os.rename(os.path.join(att_dir, f), os.path.join(start_header_subdir, f))
        cnt_dict["start_Disposition"] += 1
    elif content.startswith(b"--"):
        f_result = "mp_body"
        os.rename(os.path.join(att_dir, f), os.path.join(mp_body_subdir, f))
        cnt_dict["mp_body"] += 1
    elif content == b"":
        f_result = "empty"
        os.rename(os.path.join(att_dir, f), os.path.join(empty_subdir, f))
        cnt_dict["empty"] += 1
    else:
        f_result = "unknown"
        cnt_dict["unknown"] += 1

    if case_name in case_result.keys():
        case_result[case_name] = f_result
    else:
        unmatched_case_result[f] = f_result

print("\n>>> case result:")
for case_id, result in case_result.items():
    print(case_id, end="")
    if result != "":
        case_result_cnt += 1
        print(": ===== ", result, end=" =====")
    print()
print("--- case result cnt:", case_result_cnt)
print("\n>>> unmatched case result:")
for f, result in unmatched_case_result.items():
    print(f, ": =====", result, "=====")
print("--- unmatched case result cnt:", len(unmatched_case_result))

print("\nTotal:", len(file_list), " ---------")
print(cnt_dict)
