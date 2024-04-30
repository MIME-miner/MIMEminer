# MIMEminer

A tool to discover email malware detection evasion vulnerabilities based on parsing ambiguities of the email structure

## Sample Generation and Filtering

* See content in sample_generation/filtering directory

## Bypass Test

### Usage

* edit information of sender and receiver in ./bypass_test/config.py
* run the sending script to send test emails to target mail product
    ```bash
    cd ./bypass_test
    python main.py -r target_email_account -c case_id -p payload_id
    # example
    python main.py -r receiver -c generic_structure -p basic_qp_normal_data
    ```
* use `python main.py -h` for more information

### Parameters

* `-s`: token of sender email address in `config.sender`. Example: `-s sender_email_address`.
* `-r`: token of receiver email address in `config.target_mailbox`. Example: `-r target_email_account`. **Required Parameter**
* `-m`: `-m cases` to test cases in `./test_samples/test_cases.py`, `-m payloads` to test payloads in `./test_samples/test_payloads.py`.
* `-c`: case id in `./test_samples/test_cases.py`. Example: `-c generic_structure`.
* `-p`: payload id in `./test_samples/test_payloads.py`. Example: `-p basic_qp_normal_data`.
* `-e`: specify the encoding scheme for the payload. Example: `-e base64` or `-e quoted-printable`.
* `-i`: specify the invalid encoding scheme when it is needed in the test case.
* `-d`: control the length of email message to display when sending. `-d -1` to display all, `-d 20` to display the first 20 lines. Default is `-1`.
* `-j`: specify the subject of the email.
* `-l`: save sending logs when `-l` is specified.

## Test Samples

* `test_cases.py`: test cases of **Category 1: Confusion over Ambiguous Header Fields** and **Category 2: Differences in Parsing Malformed MIME strucures**.
* `test_payloads.py`: test payload IDs of **Category 3: Inconsistencies in Decoding Algorithms**.
* 3 types of payloads are provided here: EICAR test file, WannaCry sample and a PDF virus. 
