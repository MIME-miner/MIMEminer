import os
import re
import sys
import time
import json
import dkim
import argparse
import config
import utils
from mail_sender import MailSender

sys.path.append("..")
import test_samples.test_cases as cases
import test_samples.test_payload as payload_cases


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--client_mode', default=False, action='store_true')

    parser.add_argument('-s', '--sender', default="vps3")
    parser.add_argument('-r', '--receiver', required=True, nargs='*')

    parser.add_argument('-m', '--msg_source', choices=["cases", "eml", "payload"], default="cases")
    parser.add_argument('-c', '--cases', default=["normal_msg"], nargs='*')
    parser.add_argument('-p', '--payload', default=[], nargs='*')
    parser.add_argument('-j', '--subject', default="")
    parser.add_argument('-e', '--encoding', default="quoted-printable")
    parser.add_argument('-i', '--invalid_encoding', default="")

    parser.add_argument('-d', '--display_data', type=int, default=-1)
    parser.add_argument('-l', '--log', default=False, action='store_true', help="Enable logging")

    parser.add_argument('-n', '--filename_ext', default="")

    args = parser.parse_args()
    return args


def build_message(case_id, from_content, to_content, payload, subject="", encoding={}):
    msg = cases.test_cases[case_id]["data"]

    # substitute certain fields
    # --------- subject ---------
    subject_flag = b"<SUBJECT>"
    msg = msg.replace(subject_flag, (subject + config.subject_ext).encode())
    # --------- filename ---------
    filename_flag = b"<FILENAME>"
    filename_flag_cnt = msg.count(filename_flag)
    for i in range(1, filename_flag_cnt + 1):
        msg = msg.replace(filename_flag, (subject + "-att" + str(i) + config.filename_ext).encode())
    # --------- text part ---------
    text_flag = b"<TEXT_PART>"
    text_flag_cnt = msg.count(text_flag)
    for i in range(1, text_flag_cnt + 1):
        random_text = utils.generate_random_text()  # return a string without ending '\r\n'
        msg = msg.replace(text_flag, random_text.encode())
    # --------- encoding ---------
    for ecd_label, ecd in encoding.items():
        msg = msg.replace(ecd_label.encode(), ecd.encode())
    # --------- payload ---------
    msg_with_payload = utils.insert_payload(msg, payload)

    # add headers according to config.required_headers
    # currently: From, To, Date, DKIM-Signature
    from_header = b"" if b"From: " in msg_with_payload else b"From: " + from_content + b"\r\n"
    to_header = b"" if b"To: " in msg_with_payload else b"To: " + to_content + b"\r\n"
    date_header = b"" if b"Date: " in msg_with_payload else b"Date: " + utils.get_date() + b"\r\n"
    if config.dkim_flag:
        pri_key = open("./dkim_dir/test00_private.pem", "rb").read()
        dkim_header = dkim.sign(msg_with_payload, b"test_00", b"example.com", pri_key)
    else:
        dkim_header = b""
    msg_content = dkim_header + from_header + to_header + date_header + msg_with_payload

    return msg_content


def execute_sending(client_mode, sender_token, target_token, msg_content):
    if client_mode:
        login_info = config.account_login_info[sender_token]
        mail_server = config.sender[sender_token]["sending_server"]
    else:
        login_info = None
        mail_server = config.target_mailbox[target_token]["mx"]

    mail_server_port = config.mail_server_port
    smtp_header_hl = config.sender[sender_token]["helo"]
    smtp_header_mf = config.sender[sender_token]["mf"]
    smtp_header_rt = config.target_mailbox[target_token]["receiver"]
    # starttls = args.starttls if args.starttls else config['server_mode']['starttls']
    # smtp_seqs = exploits_builder.generate_smtp_seqs()

    mail_sender = MailSender()
    mail_sender.set_param(client_mode, (mail_server, mail_server_port), helo=smtp_header_hl, mail_from=smtp_header_mf,
                          rcpt_to=smtp_header_rt, email_data=msg_content, login_info=login_info)
    mail_sender.send_email()
    if mail_sender.unfinished_flag:
        mail_sender.unfinished_flag = False  # reset unfinished flag
        if mail_sender.err_msg == "":       # timeout with unknown reason
            config.time_out_cnt += 1
            # execute sending once and only once
            utils.print_warning("sending unfinished, will retry after 2 minutes...\n")
            time.sleep(90)
            mail_sender.send_email()      # unfinished_flag might be set to True again
    if config.log_flag:
        subject = re.findall(b"Subject: (.*)\r\n", msg_content)[0]  # get subject from main_content
        with open(config.log_path, "a") as fp:
            fp.write(time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime()))
            fp.write("[" + smtp_header_mf.decode("utf-8") + " -> " + smtp_header_rt.decode("utf-8") + " " + subject.decode("utf-8") + "] ")
            if mail_sender.unfinished_flag:
                fp.write("TIMEOUT\n")
            elif mail_sender.err_msg == "":
                fp.write("success\n")
            else:
                fp.write(mail_sender.err_msg + "\n")
    time.sleep(0.5)


def main():
    args = parse_args()

    if config.args_mode:
        client_mode = args.client_mode
        sender_token = args.sender
        target_list = args.receiver
        msg_source = args.msg_source
        case_id_list = args.cases
        specified_payload = args.payload
        specified_subject = args.subject
        encoding = args.encoding
        invalid_encoding = args.invalid_encoding
        config.disp_lim = args.display_data
        config.log_flag = args.log
        config.filename_ext = args.filename_ext
    else:
        client_mode = False
        sender_token = "vps3"
        target_list = ["mail_com", ]
        msg_source = "cases"       # to test specific payloads, set this to "payload"
        # case_id_list = list(cases.test_cases.keys())[2:]
        case_id_list = ["ecdw_bound_app_original", ]
        specified_payload = ["basic_qp_normal_data"]
        # specified_payload = payload_cases.specific_payload["b64_related"]["eicar"]  # test a batch of specific payload
        specified_subject = ""      # "" if don't want to specify subject
        encoding = "quoted-printable"
        invalid_encoding = "base64"
        config.disp_lim = -1        # recommend: 20 for long payload. See config.py for more details
        config.log_flag = False
        config.filename_ext = ""

    if invalid_encoding == "" and encoding == "quoted-printable":
        invalid_encoding = "base64"
    if invalid_encoding == "" and encoding == "base64":
        invalid_encoding = "quoted-printable"
    specified_encoding = {"<valid_CTE_here>": encoding, "<invalid_CTE_here>": invalid_encoding}

    # e.g. subject_ext = 202301051654
    config.subject_ext = time.strftime("-%Y%m%d%H%M%S", time.localtime())
    if config.log_flag and config.log_name == "":
        config.log_path = os.path.join(config.log_dir, "coremail-sender_log_qp_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".log")
    start_time = time.time()

    print("Start sending emails...")

    # first traverse all cases; then, for each case, test each target
    if msg_source == "cases":
        for case in case_id_list:
            if "data" not in cases.test_cases[case].keys():
                continue
            print("\033[94mtesting case: %s ...\n\033[0m" % case)
            # msg_main_content = cases.test_cases[case]["data"]
            # msg_main_content = utils.construct_msg_content(case, msg_main_content, specified_payload,
            #                                                subject=specified_subject, encoding=specified_encoding)
            # msg_main_content_with_payload = utils.insert_payload(msg_main_content, specified_payload)
            msg_subject = specified_subject if specified_subject != "" else case
            for target in target_list:
                msg_content = build_message(case, config.sender[sender_token]["mf"],
                                            config.target_mailbox[target]["receiver"], specified_payload,
                                            subject=msg_subject, encoding=specified_encoding)
                print("\033[94mtesting target mailbox: %s ...\n\033[0m" % target)
                execute_sending(client_mode, sender_token, target, msg_content)
            time.sleep(config.interval)
    elif msg_source == "payload":
        for pld in specified_payload:
            print("\033[94mtesting payload: %s ...\n\033[0m" % pld)
            msg_subject = specified_subject if specified_subject != "" else pld
            for target in target_list:
                msg_content = build_message("generic_structure", config.sender[sender_token]["mf"],
                                            config.target_mailbox[target]["receiver"], [pld],
                                            subject=msg_subject, encoding=specified_encoding)
                print("\033[94mtesting target mailbox: %s ...\n\033[0m" % target)
                execute_sending(client_mode, sender_token, target, msg_content)
            time.sleep(config.interval)
    elif msg_source == "eml":
        eml_path = ""
        for target in target_list:
            msg_content = build_message("att_name", config.sender[sender_token]["mf"],
                                        config.target_mailbox[target]["receiver"], specified_payload,
                                        subject=specified_subject, encoding=specified_encoding)
            print("\033[94mtesting target mailbox: %s ...\n\033[0m" % target)
            execute_sending(client_mode, sender_token, target, msg_content)

    end_time = time.time()
    print("Finished.", end_time - start_time, "s")
    if config.log_flag:
        with open(config.log_path, "a") as fp:
            fp.write("\nTime cost: " + str(end_time - start_time) + " s\n")


if __name__ == '__main__':
    main()
