import os
import re
import random
import string

import config
from time import gmtime, strftime


def get_date():
    mdate = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    return mdate.encode("utf-8")


def get_main_content(eml_path):
    trivial_headers = [b"From:", b"To:", b"Date:"]
    line_cnt = 0
    main_content = b""
    with open(eml_path, "rb") as eml_fp:
        for line in eml_fp:
            line_cnt += 1
            if line_cnt <= 5 and line.split(b" ")[0] in trivial_headers:
                continue
            main_content += line
    return main_content


def convert_binfile_to_bytes():
    path = r"xxx/xxx/sample.eml"
    with open(path) as fp:
        for line in fp.readlines():
            if line[-1] == '\n':
                line = line[:-1]
            print("b\"" + str(line) + r"\r\n" + "\"")


def print_warning(msg):
    print("\033[93m%s\033[0m" % msg)


def print_hint(msg):
    print("\033[92m%s\033[0m" % msg)


def get_payload(specified_payload):
    rp = config.payload_root_path
    # search for file with specified payload name
    payload_path = None
    for root, dirs, files in os.walk(rp):
        for file in files:
            if file == specified_payload:
                payload_path = os.path.join(root, file)

    if payload_path is None:
        print_warning("payload not found")
        exit(-1)
    with open(payload_path, "rb") as payload_fp:
        payload = payload_fp.read()
    return payload


def insert_payload(msg_content, specified_payload):
    specify_payload_flag = b"<specified_payload_here>"
    flag_cnt = msg_content.count(specify_payload_flag)
    # default_payload = "b64_normal_data"
    # if len(specified_payload) == 0:
    #     specified_payload = [default_payload] * flag_cnt
    if flag_cnt != len(specified_payload):
        print_warning("invalid number of payloads specified")
        exit(-1)
    for i in range(flag_cnt):
        payload = get_payload(specified_payload[i])
        msg_content = msg_content.replace(specify_payload_flag, payload, 1)
        # msg_content = msg_content.replace(specify_payload_flag, b"<" + specified_payload[i].encode() + b">", 1)

    # payload_token_dict = config.payload_token_dict
    # for token, payload_path in payload_token_dict.items():
    #     if token in msg_content:
    #         with open(payload_path, "rb") as payload_fp:
    #             payload = payload_fp.read()
    #         msg_content = msg_content.replace(token, payload)
    return msg_content


def get_cases_span(case_list, start_case, end_case):
    if start_case not in case_list or end_case not in case_list:
        print_warning("case not found in case list")
        exit(-1)
    start_idx = case_list.index(start_case)
    end_idx = case_list.index(end_case)
    if start_idx > end_idx:
        print_warning("invalid case span")
        exit(-1)
    return case_list[start_idx:end_idx + 1]


def get_header(header_token, msg_content):
    # example: header_token = b"From"
    header = re.findall(header_token + b": (.*)\r\n", msg_content)[0]
    return header


def generate_random_text():
    num_of_lines = random.randint(1, 3)
    characters = string.ascii_letters + string.digits + ' ,. ,.  '

    random_text = ''
    for _ in range(num_of_lines):
        line_length = random.randint(10, 30)
        line = ''.join(random.choice(characters) for _ in range(line_length))
        random_text += line + '\r\n'
    # return a string without the last \r\n
    return random_text[:-2]
