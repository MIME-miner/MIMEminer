import email
import imaplib
from email.header import decode_header
# import pandas as pd
import datetime


class Email_parse:
    def __init__(self,remote_server_url,email_url,password):
        self.remote_server_url = remote_server_url
        self.email_url = email_url
        self.password = password

    def get_att(msg):
        filename = Email_parse.get_email_name(msg)
        for part in msg.walk():
            file_name = part.get_param("name")
            if file_name:
                data = part.get_payload(decode=True)
                if data != None:
                    att_file = open('./src/' + filename, 'wb')
                    att_file.write(data)
                    att_file.close()
                else:
                    pass

    def get_email_title(msg):
        subject = email.header.decode_header(msg.get('subject'))
        if type(subject[-1][0]) == bytes:
            title = subject[-1][0].decode(str(subject[-1][1]))
        elif type(subject[-1][0]) == str:
            title = subject[-1][0]
        print("title:", title)
        return title


    def get_email_name(msg):
        for part in msg.walk():
            file_name = part.get_param("name")
            if file_name:
                h = email.header.Header(file_name)
                dh = email.header.decode_header(h)
                filename = dh[0][0]
                if dh[0][1]:
                    value, charset = decode_header(str(filename, dh[0][1]))[0]
                    if charset:
                        filename = value.decode(charset)
                        print("附件名称：", filename)
                        return filename


    def main_parse_Email(self):
        server = imaplib.IMAP4_SSL(self.remote_server_url, 993)
        server.login(self.email_url, self.password)
        server.select('INBOX')
        status,data = server.search(None,"ALL")
        if status != 'OK':
            raise Exception('read email error')
        emailids = data[0].split()
        mail_counts = len(emailids)
        print("count:",mail_counts)
        for i in range(mail_counts - 1, mail_counts - 2, -1):
            status, edata = server.fetch(emailids[i], '(RFC822)')
            msg = email.message_from_bytes(edata[0][1])
            subject = email.header.decode_header(msg.get('subject'))
            if type(subject[-1][0]) == bytes:
                title = subject[-1][0].decode(str(subject[-1][1]))
            elif type(subject[-1][0]) == str:
                title = subject[-1][0]
            print("title:", title)
            Email_parse.get_att(msg)
            Email_parse.get_text_from_HTML(msg)


    def get_text_from_HTML(msg):
        filename = Email_parse.get_email_name(msg)
        current_title = Email_parse.get_email_title(msg)
        print("filename:",filename,type(filename))
        for part in msg.walk():
            if not part.is_multipart():
                result = part.get_payload(decode=True)
                result = result.decode('gbk')
                f = open(f'./src/{current_title}.txt','w')
                f.write(result)
                f.close()
                return result


if __name__ == "__main__":
    remote_server_url = 'imap.qq.com'
    email_url = "*********@qq.com"
    password = "**********"
    demo = Email_parse(remote_server_url,email_url,password)
    demo.main_parse_Email()
