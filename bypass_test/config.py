import os

cur_path = os.path.dirname(os.path.abspath(__file__))

MAX_time_out = 4
time_out_cnt = 1    # allowed maximum number of timeouts

mail_server_port = 25

# edit sender and receiver info as needed
sender = {
    "sender_email_address": {
        "helo": b"sender.a.com",
        "mf": b"<sender@a.com>",
    },
}

target_mailbox = {
    "target_email_account": {
        "mx": "mx1.b.com",
        "receiver": b"<receiver@b.com>",
    },
    "gmail": {
        "mx": "gmail-smtp-in.l.google.com",
        "receiver": b"<receiver_example@gmail.com>",
    },
}

target_list = [
    "gmail",
    "icloud_mail",
    "outlook",
    "mail_com",
    "qq_mail",
]

args_mode = True
disp_lim = 0        # 0: don't display data  -1: display all data  >0: display first *disp_lim* lines of data
interval = 12       # interval between sending continuous messages
log_flag = False    # enable logging or not
log_dir = os.path.join(cur_path, "log")
if not os.path.exists(log_dir):
    os.mkdir(log_dir)
log_name = r""      # the name can be automatically generated if not specified
log_path = os.path.join(log_dir, log_name)

payload_root_path = os.path.join(cur_path, "../test_samples")

filename_ext = ""
subject_ext = ""

dkim_flag = False
dkim_sign_headers = ["From"]

account_login_info = {}

# payload_token_dict = {
#     b"<normal_data>": os.path.join(cur_path, "./sample/normal/normal_data"),
#     b"<b64_normal_data>": os.path.join(cur_path, "./sample/normal/b64_normal_data"),
#     b"<basic_qp_normal_data>": os.path.join(cur_path, "./sample/normal/basic_qp_normal_data"),
#     b"<greeting>": os.path.join(cur_path, "./sample/normal/greeting"),
# }
