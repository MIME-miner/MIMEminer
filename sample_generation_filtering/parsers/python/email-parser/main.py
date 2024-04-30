import argparse
import os
import sys
import email
import re

def save_attachments(input_file, output_dir):
    # 创建输出目录
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(input_file, 'rb') as f:
        msg = email.message_from_binary_file(f)

        # 遍历邮件的所有部分
        for part in msg.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue

            # 提取文件名
            filename = part.get_filename()
            if filename:
                # 防止路径遍历攻击
                filename = os.path.basename(filename)

                # 将非法字符替换为下划线
                filename = re.sub(r'[\\/:*?"<>|]', '_', filename)

                # 保存附件
                with open(os.path.join(output_dir, filename), 'wb') as fp:
                    fp.write(part.get_payload(decode=True))
                    print(f'Saved attachment: {filename}')

def main():
    # 命令行参数解析
    parser = argparse.ArgumentParser(description='Extract attachments from an email file')
    parser.add_argument('-i', '--input', help='Input email file path', required=True)
    parser.add_argument('-o', '--output', help='Output directory for attachments', required=True)
    args = parser.parse_args()

    input_file = args.input
    output_dir = args.output

    if not os.path.isfile(input_file):
        print(f'Error: Input file "{input_file}" does not exist.')
        sys.exit(1)

    save_attachments(input_file, output_dir)

if __name__ == "__main__":
    main()