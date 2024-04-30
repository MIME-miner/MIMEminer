import os
import email
import mailparser
import config as cfg
from flanker import mime
from flanker.mime.message.part import MimePart
from tqdm import tqdm


def read_eml(eml_path):
    with open(eml_path, "rb") as eml_fp:
        eml_bytes = eml_fp.read()
    with open(eml_path, "r") as eml_fp:
        eml_str = eml_fp.read()
    return eml_bytes, eml_str


def flanker_get_att_from_body(body_part: MimePart, att_path):
    if body_part.is_attachment():
        name = body_part.detected_file_name
        if name == "" or name is None:
            name = "UNKNOWN_FILENAME"
        out_path = os.path.join(att_path, name)
        attachment = body_part.body  # 这里得到的body可能是string类型，也可能是bytes类型 这到底是由什么决定的？

        # if isinstance(attachment, str):
        #     with open(out_path, "w") as att_fp:
        #         att_fp.write(attachment)
        # else:
        #     with open(out_path, "wb") as att_fp:
        #         att_fp.write(attachment)
        with open(out_path, 'wb') as att_fp:
            if isinstance(attachment, str):
                att_fp.write(attachment.encode('utf-8'))
            else:
                att_fp.write(attachment)


def email_get_att_from_body(body_part, att_path):
    if body_part.get_content_disposition() == "attachment":
        # _name = body_part.get_param("name")
        # _filename = body_part.get_param("filename")       # None -- why?
        name = body_part.get_filename()
        if name == "" or name is None:
            name = "UNKNOWN_FILENAME"
        out_path = os.path.join(att_path, name)
        attachment = body_part.get_payload(decode=True)

        if isinstance(attachment, str):
            with open(out_path, "w") as att_fp:
                att_fp.write(attachment)
        else:
            with open(out_path, "wb") as att_fp:
                att_fp.write(attachment)


def flanker_get_att(eml: MimePart, att_path):
    # print(eml.body)
    if eml.content_type.is_singlepart():
        flanker_get_att_from_body(eml, att_path)
    else:
        for part in eml.parts:
            if part.content_type.is_singlepart():
                flanker_get_att_from_body(part, att_path)
            else:
                flanker_get_att(part, att_path)
                continue


def email_get_att(eml, att_path):
    if not eml.is_multipart():
        email_get_att_from_body(eml, att_path)
    else:
        for part in eml.walk():
            if not part.is_multipart():
                email_get_att_from_body(part, att_path)
            else:
                # email_get_att(part, att_path)
                continue


def flanker_process_eml(eml_bytes, att_path):
    flanker_eml = mime.from_string(eml_bytes)
    flanker_get_att(flanker_eml, att_path)


def email_process_eml(eml_bytes, att_path):
    email_eml = email.message_from_bytes(eml_bytes)
    email_get_att(email_eml, att_path)


def mailParser_process_eml(eml_bytes, att_path):
    mail = mailparser.parse_from_bytes(eml_bytes)
    # att = mail.attachments
    mail.write_attachments(att_path)


if __name__ == "__main__":
    parser_list = cfg.parser_list
    parser_output_path = {}
    err_log = {parser: [] for parser in parser_list}

    # for eml_file in tqdm(os.listdir(in_path)):
    for eml_file in os.listdir(cfg.extract_source_path):
        eml_name = os.path.splitext(eml_file)[0]
        eml_bytes, eml_str = read_eml(os.path.join(cfg.extract_source_path, eml_file))
        print("Extracting: {}".format(eml_name))

        for parser in parser_list:
            att_path = os.path.join(cfg.extract_dest_path, eml_name, parser)
            parser_output_path[parser] = att_path
            try:
                os.makedirs(att_path)
            except FileExistsError:
                # print("*** {} already exists ***".format(att_path))
                pass
            except Exception as e:
                print(e)

        for parser in parser_list:
            # eval(parser + "_process_eml")(eml_bytes, parser_output_path[parser])
            try:
                eval(parser + "_process_eml")(eml_bytes, parser_output_path[parser])
            except Exception as e:
                err_log[parser].append("[{}] {}\n".format(eml_name, e))

        # try:
        #     flanker_process_eml(eml_bytes, parser_output_path["flanker"])
        # except Exception as e:
        #     err_log["flanker"].append("[{}] {}\n".format(eml_name, e))
        #     # print("Flanker [{}] {}".format(eml_name, e))
        #
        # try:
        #     email_process_eml(eml_bytes, parser_output_path["email"])
        # except Exception as e:
        #     err_log["email"].append("[{}] {}\n".format(eml_name, e))
        #     # print("Email [{}] {}".format(eml_name, e))
        # # email_process_eml(eml_bytes, parser_output_path["email"])
        #
        # try:
        #     mailParser_process_eml(eml_bytes, parser_output_path["mail-parser"])
        # except Exception as e:
        #     err_log["mail-parser"].append("[{}] {}\n".format(eml_name, e))
        #     # print("Mail-Parser [{}] {}".format(eml_name, e))

    with open(cfg.extract_err_path, "w") as err_fp:
        for parser in parser_list:
            err_fp.write(">>> {}\n".format(parser))
            err_fp.writelines(err_log[parser])
            err_fp.write("\n\n")
