import argparse
import os
from flanker import mime

def extract_attachments(email_file, output_dir):
    with open(email_file, 'rb') as f:
        msg = mime.from_string(f.read())

    ##attachments = msg.is_attachment()

    for part in msg.parts:
        print('Content-Type: {} Body: {}'.format(part, part.body))
        if part.is_attachment():
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            print('Content-Type: {} Body: {}'.format(part, part.body))
            filename = part.detected_file_name
            with open(os.path.join(output_dir, filename), 'w') as f:
               f.write(part.body)
               print(f'Saved attachment: {filename}')




    # for attachment in attachments:
    #     filename = os.path.join(output_dir, attachment.detected_file_name)
    #     with open(filename, 'wb') as f:
    #         f.write(attachment.payload)

    # print("Attachments extracted successfully to:", output_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract attachments from an email file.")
    parser.add_argument("-i", "--input", required=True, help="Input email file path.")
    parser.add_argument("-o", "--output", required=True, help="Output directory to save attachments.")
    args = parser.parse_args()

    extract_attachments(args.input, args.output)