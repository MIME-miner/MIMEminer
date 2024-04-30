import argparse
from mailparser import parse_from_file
import os

def extract_attachments(input_file, output_dir):
    # 解析邮件文件
    mail = parse_from_file(input_file)

    # 检查是否存在附件
    attachments = mail.attachments
    # 创建输出目录（如果不存在）
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    # 保存附件到输出目录
    for attachment in attachments:
        with open(os.path.join(output_dir, attachment['filename']), 'w') as f:
            f.write(attachment['payload'])

def main():
    # 设置命令行参数
    parser = argparse.ArgumentParser(description='Extract attachments from email file')
    parser.add_argument('-i', '--input', type=str, required=True, help='Path to the input email file')
    parser.add_argument('-o', '--output', type=str, required=True, help='Path to the output directory for attachments')
    args = parser.parse_args()

    # 提取附件
    extract_attachments(args.input, args.output)
    print("Attachments extracted successfully!")

if __name__ == "__main__":
    main()