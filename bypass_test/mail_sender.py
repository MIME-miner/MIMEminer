from socket import *
import time
import ssl
import re
import config
import utils
import signal

try:
    from StringIO import StringIO  ## for Python 2
except ImportError:
    from io import StringIO  ## for Python 3


class MailSender(object):
    def __init__(self):
        self.client_mode = False
        self.mail_server = b""
        self.rcpt_to = b""
        self.email_data = b""
        self.helo = b""
        self.mail_from = b""
        self.starttls = False

        self.client_socket = None
        self.tls_socket = None

        self.err_msg = ""
        self.unfinished_flag = False
        self.login_info = None

    def set_param(self, clent_mode, mail_server, rcpt_to, email_data, helo, mail_from, login_info=None, starttls=False):
        self.client_mode = clent_mode
        self.mail_server = mail_server
        self.rcpt_to = rcpt_to
        self.email_data = email_data
        self.helo = helo
        self.mail_from = mail_from
        self.login_info = login_info
        self.starttls = starttls

    def establish_socket(self):
        client_socket = socket(AF_INET, SOCK_STREAM)
        print("Connecting " + str(self.mail_server))
        client_socket.connect(self.mail_server)
        self.print_recv_msg(client_socket)

        if self.starttls == True:
            client_socket.send(b"ehlo " + self.helo + b"\r\n")
            self.print_send_msg("ehlo " + self.helo.decode("utf-8") + "\r\n")
            self.print_recv_msg(client_socket)

            client_socket.send(b"starttls\r\n")
            self.print_send_msg("starttls\r\n")
            self.print_recv_msg(client_socket)

            tls_socket = ssl.wrap_socket(client_socket, ssl_version=ssl.PROTOCOL_TLS)
            self.tls_socket = tls_socket

        self.client_socket = client_socket

    def send_login_cmds(self, client_socket):
        account_name = self.login_info["account"]
        account_pswd = self.login_info["pswd"]

        client_socket.send(b"AUTH LOGIN\r\n")
        time.sleep(0.1)
        self.print_send_msg("AUTH LOGIN\r\n")
        self.print_recv_msg(client_socket)

        client_socket.send(account_name + b"\r\n")
        time.sleep(0.1)
        self.print_send_msg(account_name.decode("utf-8") + "\r\n")
        self.print_recv_msg(client_socket)

        client_socket.send(account_pswd + b"\r\n")
        time.sleep(0.1)
        self.print_send_msg(account_pswd.decode("utf-8") + "\r\n")
        self.print_recv_msg(client_socket)


    def send_smtp_cmds(self, client_socket):
        client_socket.send(b"ehlo " + self.helo + b"\r\n")
        time.sleep(0.1)
        self.print_send_msg("ehlo " + self.helo.decode("utf-8") + "\r\n")
        recv_msg = self.print_recv_msg(client_socket)

        if self.client_mode:
            self.send_login_cmds(client_socket)

        # if self.mode == "client":
        #     if "LOGIN".lower() in recv_msg.lower() and self.auth_proto == "LOGIN":
        #         auth_username = b"AUTH LOGIN " + base64.b64encode(self.username) + b"\r\n"
        #         client_socket.send(auth_username)
        #         self.print_send_msg(auth_username.decode("utf-8"))
        #         self.print_recv_msg(client_socket)
        #
        #         auth_pwd = base64.b64encode(self.password) + b"\r\n"
        #         client_socket.send(auth_pwd)
        #         self.print_send_msg(auth_pwd.decode("utf-8"))
        #         self.print_recv_msg(client_socket)
        #     else:
        #         auth_msg = b'AUTH PLAIN ' + base64.b64encode(
        #             b'\x00' + self.username + b'\x00' + self.password) + b'\r\n'
        #         client_socket.send(auth_msg)
        #         self.print_send_msg(auth_msg.decode("utf-8"))
        #         self.print_recv_msg(client_socket)

        client_socket.send(b'MAIL FROM: ' + self.mail_from + b'\r\n')
        time.sleep(0.1)
        self.print_send_msg('MAIL FROM: ' + self.mail_from.decode("utf-8") + '\r\n')
        self.print_recv_msg(client_socket)

        client_socket.send(b"RCPT TO: " + self.rcpt_to + b"\r\n")
        time.sleep(0.1)
        self.print_send_msg("RCPT TO: " + self.rcpt_to.decode("utf-8") + "\r\n")
        self.print_recv_msg(client_socket)

        client_socket.send(b"data\r\n")
        time.sleep(0.1)
        self.print_send_msg("data\r\n")
        self.print_recv_msg(client_socket)      # possibly error here, self.err_msg will be updated

        client_socket.send(self.email_data + b"\r\n.\r\n")
        time.sleep(0.1)
        if config.disp_lim != 0:
            send_data_str = self.email_data.decode("utf-8")
            send_data_lines = send_data_str.split("\r\n")
            try:
                if config.disp_lim > 0:
                    self.print_send_msg("\r\n".join(send_data_lines[:config.disp_lim]))
                    utils.print_hint("\r\n  more lines are omitted ...\r\n")
                    print("\r\n".join(send_data_lines[-5:]))
                else:
                    self.print_send_msg(send_data_str + "\r\n.\r\n")
                # self.print_send_msg(self.email_data.decode("utf-8") + "\r\n.\r\n")
            except UnicodeDecodeError as e:
                utils.print_warning("\tUnicodeDecodeError found while printing message.")
                utils.print_warning("\t" + str(e))
            # self.print_send_msg(self.email_data + b"\r\n.\r\n")
        self.print_recv_msg(client_socket)

    def send_quit_cmd(self, client_socket):
        client_socket.send(b"quit\r\n")
        self.print_send_msg("quit\r\n")
        self.print_recv_msg(client_socket)

    def close_socket(self):
        if self.tls_socket != None:
            self.tls_socket.close()
        if self.client_socket != None:
            self.client_socket.close()

    def read_line(self, sock):
        buff = StringIO()
        while True:
            data = (sock.recv(1)).decode("utf-8")
            buff.write(data)
            if '\n' in data:
                break
        return buff.getvalue().splitlines()[0]

    def print_send_msg(self, msg):
        print("<<< " + msg)

    def print_recv_msg(self, client_socket):
        print("\033[91m" + ">>> ", end='')
        time.sleep(1)

        msg = ""
        while True:
            line = self.read_line(client_socket)
            msg += line
            print(line)
            if "-" not in line:
                break
            else:
                if len(line) > 5 and "-" not in line[:5]:
                    break
            time.sleep(0.1)
        print("\033[0m")

        pattern = re.compile(r"^[45]\d{2}\b")
        if re.search(pattern, msg):
            self.err_msg += msg
        return msg

    def send_email(self):
        timeout = 90       # if a single sending task takes more than 2 minutes, it will be considered as unfinished
        signal.signal(signal.SIGALRM, self.signal_handler)
        signal.alarm(timeout)

        try:
            self.establish_socket()
            if self.starttls == True:
                self.send_smtp_cmds(self.tls_socket)
                self.send_quit_cmd(self.tls_socket)
            else:
                self.send_smtp_cmds(self.client_socket)
                self.send_quit_cmd(self.client_socket)
            self.close_socket()
        except TimeoutError as e:
            self.unfinished_flag = True
            utils.print_warning("Execution timed out")
            if config.time_out_cnt >= config.MAX_time_out:
                utils.print_warning("Too many timeouts, exiting...")
                exit(-1)
        except Exception as e:
            import traceback
            traceback.print_exc()
        finally:
            self.close_socket()

        return self.err_msg, self.unfinished_flag

    def signal_handler(self, signum, frame):
        raise TimeoutError("Execution timed out")

    def __del__(self):
        self.close_socket()
