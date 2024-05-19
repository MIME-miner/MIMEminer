test_cases = {
    "normal_msg": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"Hi, this is a test message! Best wishes.\r\n"
        ,
        "description": b"The simplest test case, just to test sending function."
    },
    "manual_case": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"afcsebwilwevf wefqoplqkdncoie\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"5rC45ZKM5Lmd5bm077yM5bKB5Zyo55m45LiR77yM5pqu5pil5LmL5Yid77yM5Lya5LqO5Lya56i9\r\n"
            b"5bGx6Zi05LmL5YWw5Lqt77yM5L+u56aK5LqL5Lmf44CC576k6LSk5q+V6Iez77yM5bCR6ZW/5ZK4\r\n"
            b"6ZuG44CC5q2k5Zyw5pyJ5bSH5bGx5bO75bKt77yM6IyC5p6X5L+u56u577yM5Y+I5pyJ5riF5rWB\r\n"
            b"5r+A5rmN77yM5pig5bim5bem5Y+z77yM5byV5Lul5Li65rWB6Kee5puy5rC077yM5YiX5Z2Q5YW2\r\n"
            b"5qyh44CC6Jm95peg5Lid56u5566h5bym5LmL55ub77yM5LiA6Kee5LiA5ZKP77yM5Lqm6Laz5Lul\r\n"
            b"55WF5Y+Z5bm95oOF44CCCuaYr+aXpeS5n++8jOWkqeacl+awlOa4he+8jOaDoOmjjuWSjOeVheOA\r\n"
            b"guS7sOinguWuh+WumeS5i+Wkp++8jOS/r+Wvn+WTgeexu+S5i+ebm++8jOaJgOS7pea4uOebrumq\r\n"
            b"i+aAgO+8jOi2s+S7peaegeinhuWQrOS5i+Wose+8jOS/oeWPr+S5kOS5n+OAgg==\r\n"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    # if encoded sample is blocked in this case, it should not be used in following cases
    "generic_no_encoding": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    # need to specify Subject and Content-Transfer-Encoding
    "generic_structure": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },


    # lack of header ==============
    "no_disp": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Use app/octet type header."
    },

    # multiple conflicting headers ===============
    # Content-Transfer-Encoding
    "multiple_encoding_valid_prev": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"Content-Transfer-Encoding: <invalid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "multiple_encoding_valid_latter": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <invalid_CTE_here>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "multiple_encoding_ftt": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <invalid_CTE_here>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "multiple_encoding_ttf": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"Content-Transfer-Encoding: <invalid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "multiple_encoding_invalid_valid": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: xxxxxxx\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "multiple_encoding_valid_invalid": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"Content-Transfer-Encoding: xxxxxxx\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "multiple_encoding_value_valid_prev": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>, <invalid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "multiple_encoding_value_valid_latter": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <invalid_CTE_here>, <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "multiple_encoding_value_quote_valid_prev": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: \"<valid_CTE_here>\", <invalid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "multiple_encoding_value_quote_valid_latter": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: \"<invalid_CTE_here>\", <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    # Content-Type
    "multiple_type_header_valid_prev": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Type: multipart/mixed; boundary=bar\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "multiple_type_header_valid_latter": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: multipart/mixed; boundary=bar\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "multiple_type_value_valid_prev": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream, multipart/mixed; boundary=bar\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "multiple_type_value_valid_latter": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: multipart/mixed, application/octet-stream; boundary=bar\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "multiple_type_header_valid_prev_mp": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"Content-Type: application/octet-stream\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "multiple_type_header_valid_latter_mp": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: application/octet-stream\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "multiple_type_value_valid_prev_mp": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed, application/octet-stream; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "multiple_type_value_valid_latter_mp": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: application/octet-stream, multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },

    # header & header values ================
    # Content-Transfer-Encoding
    "space_before_CTE": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b" Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"Add extra space before CTE header."
    },
    "space_before_first_CTE": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b" Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"Add extra space before CTE header."
    },
    "0_before_CTE": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"\0Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"Add extra \\0 before CTE header."
    },
    "0_before_first_CTE": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"\0Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"Add extra \\0 before CTE header."
    },
    "space_before_CTE_colon": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding : <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"Add extra space in CTE header before colon."
    },
    "0_before_CTE_colon": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding\0: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"Add \\0 in CTE header before colon."
    },
    "CTE_value_abnormal_case_b64": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: bASe64\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"Abnormal case in CTE value."
    },
    "CTE_value_abnormal_case_qp": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: qUOteD-PrinTAblE\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"Abnormal case in CTE value."
    },
    "CTE_value_with_0_start": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: \0<valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"Add extra \\0 within CTE value."
    },
    "CTE_value_with_0_mid_b64": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: bas\0e64\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"Add extra \\0 within CTE value."
    },
    "CTE_value_with_0_mid_qp": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: quot\0ed-printable\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"Add extra \\0 within CTE value."
    },
    "CTE_value_with_0_end": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\0\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"Add extra \\0 after CTE value."
    },
    # CTE - folding
    "CTE_truncated_folding_b64": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Transfer-Encoding: bas\r\n"
            b" e64\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "CTE_truncated_folding_qp": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Transfer-Encoding: quot\r\n"
            b" ed-printable\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "CTE_colon_folding": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Transfer-Encoding:\r\n"
            b" <valid_CTE_here>\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "CTE_folding_colon": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Transfer-Encoding\r\n"
            b" :<valid_CTE_here>\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "CTE_comment_folding_b64": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Transfer-Encoding: bas(com\r\n"
            b" ment)e64\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "CTE_comment_folding_qp": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Transfer-Encoding: quot(com\r\n"
            b" ment)ed-printable\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    # Content-Type
    "space_before_type": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b" Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"Add extra space before type header."
    },
    "space_before_first_type": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b" Content-Type: multipart/mixed; boundary=bar\r\n"
            b"\r\n"
            b"--bar\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--bar\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--bar--\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Add extra space before type header."
    },
    "0_before_type": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"\0Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"Add extra \\0 before type header."
    },
    "0_before_first_type": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"\0Content-Type: multipart/mixed; boundary=bar\r\n"
            b"\r\n"
            b"--bar\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--bar\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--bar--\r\n"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "space_before_type_colon": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type : multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"Add extra space in type header before colon."
    },
    "0_before_type_colon": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type\0: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"Add \\0 in type header before colon."
    },
    "type_value_abnormal_case": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: mUltIpARt/mIxeD; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"Abnormal case in type value."
    },
    "type_value_with_0_start": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: \0multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"Add extra \\0 within type value."
    },
    "type_value_with_0_mid": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipar\0t/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"Add extra \\0 within type value."
    },
    "type_value_with_0_end": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed\0; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"Add extra \\0 after type value."
    },

    "type_no_header": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b": application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "mp_type_header_overlap": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type:Content-Type:multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "mp_type_value_overlap": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixedmultipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "CTE_header_overlap": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding:Content-Transfer-Encoding:<valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "CTE_value_overlap": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here><valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "CTE_value_invalid_base645": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: base645\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "CTE_value_invalid_dash": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>-\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },

    # separation between headers ===============
    "abnormal_line_break_between_headers_r": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"Abnormal line break between headers."
    },
    "abnormal_line_break_between_headers_n": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"Abnormal line break between headers."
    },
    "abnormal_line_break_between_headers_nr": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\n\r"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"Abnormal line break between headers."
    },
    "abnormal_line_break_between_headers_rrn": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"Abnormal line break between headers."
    },
    "abnormal_line_break_between_headers_rnn": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"Abnormal line break between headers."
    },
    "abnormal_line_break_between_headers_rnr": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n\r"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"Abnormal line break between headers."
    },
    "abnormal_line_break_between_headers_nrn": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\n\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"Abnormal line break between headers."
    },
    "abnormal_line_break_between_headers_rc": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\x13"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"Abnormal line break between headers."
    },
    "abnormal_line_break_between_headers_cn": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\x13\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"Abnormal line break between headers."
    },
    "abnormal_line_break_between_headers_rcn": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r{}\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"Abnormal line break between headers."
    },
    "abnormal_line_break_between_headers_rcnc": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r(\n)"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"Abnormal line break between headers."
    },
    "abnormal_line_break_between_headers_r_space": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r "
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"Content-ID: 3\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"Abnormal line break between headers."
    },
    "abnormal_line_break_between_headers_space_n": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME> \n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"Content-ID: 3\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"Abnormal line break between headers."
    },
    "abnormal_line_break_between_headers_rnc": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"#Content-ID: 3\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    # separation between headers - folding
    "pre_CTE_r_n_folding": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b" Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"Content-ID: 3\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "pre_CTE_r_folding": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r"
            b" Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"Content-ID: 3\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "pre_CTE_n_folding": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\n"
            b" Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"Content-ID: 3\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "post_CTE_r_n_folding": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b" Content-ID: 3\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "post_CTE_r_folding": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r"
            b" Content-ID: 3\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "post_CTE_n_folding": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\n"
            b" Content-ID: 3\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },

    # boundary related =============
    # multiple boundary
    "mul_bound_header_valid_prev": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"Content-Type: multipart/mixed; boundary=faa\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "mul_bound_header_valid_latter": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=faa\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "mul_bound_para_valid_prev": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo, boundary=faa\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "mul_bound_para_valid_latter": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=faa, boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "mul_bound_header_valid_prev_mix_app": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"Content-Type: multipart/mixed; boundary=faa\r\n"
            b"\r\n"
            b"--faa\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
            b"--faa--\r\n"
        ,
        "description": b""
    },
    "mul_bound_header_valid_latter_mix_app": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=faa\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--faa\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
            b"--faa--\r\n"
        ,
        "description": b""
    },
    "mul_bound_para_valid_prev_mix_app": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo, boundary=faa\r\n"
            b"\r\n"
            b"--faa\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
            b"--faa--\r\n"
        ,
        "description": b""
    },
    "mul_bound_para_valid_latter_mix_app": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=faa, boundary=foo\r\n"
            b"\r\n"
            b"--faa\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
            b"--faa--\r\n"
        ,
        "description": b""
    },
    # comma in boundary
    "comma_bound_app_both": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo,faa\r\n"
            b"\r\n"
            b"--foo,faa\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo,faa\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo,faa--\r\n"
        ,
        "description": b""
    },
    "comma_bound_app_prev": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo,faa\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "comma_bound_app_latter": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo,faa\r\n"
            b"\r\n"
            b"--faa\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--faa\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--faa--\r\n"
        ,
        "description": b""
    },
    # blank char / 0 before boundary
    "bound_begin_blank_char_sta": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary= foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"blank char at the beginning of separating boundary"
    },
    "bound_begin_blank_char_sta_app": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary= foo\r\n"
            b"\r\n"
            b"-- foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"-- foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"-- foo--\r\n"
        ,
        "description": b"blank char at the beginning of separating boundary"
    },
    "bound_begin_blank_char_quo_sta": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=\" foo\"\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"blank char at the beginning of separating boundary"
    },
    "bound_begin_blank_char_quo_sta_app": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=\" foo\"\r\n"
            b"\r\n"
            b"-- foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"-- foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"-- foo--\r\n"
        ,
        "description": b"blank char at the beginning of separating boundary"
    },
    "bound_begin_0_sta": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=\0foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "bound_begin_0_sta_app": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=\0foo\r\n"
            b"\r\n"
            b"--\0foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--\0foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--\0foo--\r\n"
        ,
        "description": b""
    },
    "bound_begin_0_quo_sta": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=\"\0foo\"\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "bound_begin_0_quo_sta_app": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=\"\0foo\"\r\n"
            b"\r\n"
            b"--\0foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--\0foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--\0foo--\r\n"
        ,
        "description": b""
    },
    # blank char in boundary
    "blank_char_within_bound_sta": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"null char within boundary statement"
    },
    "blank_char_within_bound_sta_app": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo foo\r\n"
            b"\r\n"
            b"--foo foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo foo\r\n"
            b"\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo foo--\r\n"
        ,
        "description": b"null char within boundary statement"
    },
    "blank_char_within_bound_q_sta_app": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=\"foo foo\"\r\n"
            b"\r\n"
            b"--foo foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo foo\r\n"
            b"\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo foo--\r\n"
        ,
        "description": b"null char within boundary statement"
    },
    "blank_char_within_bound_q_sta_q_app": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=\"foo foo\"\r\n"
            b"\r\n"
            b"--\"foo foo\"\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--\"foo foo\"\r\n"
            b"\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--\"foo foo\"--\r\n"
        ,
        "description": b"null char within boundary statement"
    },
    # semicolon / quotation / null boundary
    "semicolon_within_bound_sta": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo;foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"semicolon within boundary statement"
    },
    "semicolon_within_bound_sta_app": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo;foo\r\n"
            b"\r\n"
            b"--foo;foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo;foo\r\n"
            b"\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo;foo--\r\n"
        ,
        "description": b"semicolon within boundary statement"
    },
    "semicolon_within_bound_q_sta_app": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=\"foo;foo\"\r\n"
            b"\r\n"
            b"--foo;foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo;foo\r\n"
            b"\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo;foo--\r\n"
        ,
        "description": b"semicolon within boundary statement"
    },
    "semicolon_within_bound_q_sta_q_app": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=\"foo;foo\"\r\n"
            b"\r\n"
            b"--\"foo;foo\"\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--\"foo;foo\"\r\n"
            b"\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--\"foo;foo\"--\r\n"
        ,
        "description": b"semicolon within boundary statement"
    },
    "bound_quot_null_str_app_null": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=\"\"foo\r\n"
            b"\r\n"
            b"--\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--\r\n"
            b"\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"----\r\n"
        ,
        "description": b"quotation within boundary statement"
    },
    "bound_quot_null_str_app_str": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=\"\"foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"quotation within boundary statement"
    },
    "bound_quot_null_str_app_both": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=\"\"foo\r\n"
            b"\r\n"
            b"--\"\"foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--\"\"foo\r\n"
            b"\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--\"\"foo--\r\n"
        ,
        "description": b"quotation within boundary statement"
    },
    "bound_quot_half_app_prev": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=\"bar\"foo\r\n"
            b"\r\n"
            b"--bar\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--bar\r\n"
            b"\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--bar--\r\n"
        ,
        "description": b"quotation within boundary statement"
    },
    "bound_quot_half_app_latter": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=\"bar\"foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"quotation within boundary statement"
    },
    "bound_quot_half_app_both": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=\"bar\"foo\r\n"
            b"\r\n"
            b"--\"bar\"foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--\"bar\"foo\r\n"
            b"\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--\"bar\"foo--\r\n"
        ,
        "description": b"quotation within boundary statement"
    },
    "null_bound": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=\r\n"
            b"\r\n"
            b"--\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"----\r\n"
        ,
        "description": b"null value for boundary para"
    },
    "null_bound_q": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=\"\r\n"
            b"\r\n"
            b"--\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"----\r\n"
        ,
        "description": b"null value for boundary para"
    },
    "null_bound_qq": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=\"\"\r\n"
            b"\r\n"
            b"--\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"----\r\n"
        ,
        "description": b"null value for boundary para"
    },
    "null_bound_semicolon": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=;\r\n"
            b"\r\n"
            b"--\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--\r\n"
            b"\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"----\r\n"
        ,
        "description": b"null value for boundary para"
    },
    "null_bound_semicolon_app": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=;\r\n"
            b"\r\n"
            b"--;\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--;\r\n"
            b"\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--;--\r\n"
        ,
        "description": b"null value for boundary para"
    },
    "boundary_truncated_folding_app_half": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b" foo\r\n"
            b"Content-ID: 3\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "boundary_truncated_folding_app_full": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b" foo\r\n"
            b"Content-ID: 3\r\n"
            b"\r\n"
            b"--foofoo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foofoo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foofoo--\r\n"
        ,
        "description": b""
    },
    "boundary_eq_folding": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=\r\n"
            b" foofoo\r\n"
            b"Content-ID: 3\r\n"
            b"\r\n"
            b"--foofoo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foofoo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foofoo--\r\n"
        ,
        "description": b""
    },
    "boundary_eq_space_folding": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary= \r\n"
            b" foofoo\r\n"
            b"Content-ID: 3\r\n"
            b"\r\n"
            b"--foofoo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foofoo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foofoo--\r\n"
        ,
        "description": b""
    },
    "boundary_folding_eq": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary\r\n"
            b" =foofoo\r\n"
            b"Content-ID: 3\r\n"
            b"\r\n"
            b"--foofoo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foofoo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foofoo--\r\n"
        ,
        "description": b""
    },
    "boundary_space_folding_eq": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary \r\n"
            b" =foofoo\r\n"
            b"Content-ID: 3\r\n"
            b"\r\n"
            b"--foofoo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foofoo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foofoo--\r\n"
        ,
        "description": b""
    },
    # blank char in boundary line
    "bound_begin_blank_char_app_begin": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b" --foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"blank char at the beginning of separating boundary"
    },
    "bound_begin_blank_char_app_sep": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b" --foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"blank char at the beginning of separating boundary"
    },
    "bound_begin_blank_char_app_end": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b" --foo--\r\n"
        ,
        "description": b"blank char at the beginning of separating boundary"
    },
    "bound_end_blank_char_sta": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo \r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"blank char at the beginning of end boundary (statement & application)"
    },
    "terminating_bound_no_dash": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo\r\n"
        ,
        "description": b""
    },
    "bound_end_blank_char_app": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo \r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"blank char at the end of separating boundary"
    },
    # improper boundary statement
    "boundary_space_eq": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary =foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "boundary_0_eq": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary\0=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "bound_para_no_semicolon": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "wrong_bound_para": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; bound=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; boundary=faa\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "bound_para_for_singlepart": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; boundary=faa\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "wrong_boundary": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--faa\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--faa\r\n"
            b"Content-Type: application/octet-stream; boundary=faa\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--faa--\r\n"
        ,
        "description": b""
    },

    "bound_encoding_composite_bypass": {
        "possible_data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=(foo)1\r\n"
            b"\r\n"
            b"--(foo)1\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--(foo)1\r\n"
            b"\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: utf-7\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--(foo)1--\r\n"
        ,
        "description": b"amavis failed to parse out the parts, delivering the entire email message to clamav. "
                       b"clamav encounterd unknown encoding, and employed a default base64 decoding."
    },

    # Entity structure related ====================
    # boundary and entity
    "entity_r_bound": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r"
            b"--foo\r\n"
            b"\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "entity_rc_bound": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r,"
            b"--foo\r\n"
            b"\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "bound_r_entity": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r"
            b"Content-Type: multipart/mixed; boundary=faa\r\n"
            b"\r\n"
            b"--faa\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--faa\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--faa--\r\n"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "bound_rc_entity": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\x13"
            b"Content-Type: multipart/mixed; boundary=faa\r\n"
            b"\r\n"
            b"--faa\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--faa\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--faa--\r\n"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "blank_line_after_bound": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"blank line between separating boundary and trailing entity"
    },
    # epilogue / preamble
    "entity_outside_of_bound_preamble": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"Content-Type: application/octet-stream; name=preamble_att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b'Z=B2=12=E7w=3DP/=C3H*X$=F44?=85=930=FA=CA=F9=60=1Aqky+P=826=8F\r\n'
            b"--foo--\r\n"
        ,
        "description": b"entity placed as preamble"
    },
    "entity_outside_of_bound_epilogue": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b'Z=B2=12=E7w=3DP/=C3H*X$=F44?=85=930=FA=CA=F9=60=1Aqky+P=826=8F\r\n'
            b"--foo--\r\n"
            b"Content-Type: application/octet-stream; name=epilogue_att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
        ,
        "description": b"entity placed as epilogue"
    },
    # nesting multipart
    "inner_using_outer_bound": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: multipart/mixed; boundary=faa\r\n"
            b"\r\n"
            b"--faa\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--faa--\r\n"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "inner_outer_same_bound": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo--\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "inner_no_bound_para": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: multipart/mixed\r\n"
            b"\r\n"
            b"--faa\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--faa\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--faa--\r\n"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "inner_no_bound_para_using_outer": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: multipart/mixed\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "deleted_inner_multipart_body": {
        "data":
            b"Subject: <SUBJECT>\r\n"
            b"MIME-Version: 1.0\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"Content-ID: 1\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: multipart/mixed; boundary=bar\r\n"
            b"Content-ID: 2\r\n"
            b"\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"Content-ID: 5\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
    },
    # header & body
    # simply modifying \r \n
    "header_body_delimit_rnr": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "header_body_delimit_rnn": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "header_body_delimit_rrn": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "header_body_delimit_nrn": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "header_body_delimit_rr": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r"
            b"\r"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "header_body_delimit_nn": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\n"
            b"\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "header_body_delimit_nr": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\n"
            b"\r"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "header_body_delimit_rn": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r"
            b"\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "header_body_delimit_rnrrn": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "header_body_delimit_rnnrn": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\n\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "header_body_delimit_rnrnr": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n\r"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "header_body_delimit_rnrnn": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "header_body_delimit_rnrnrn": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    # insert characters
    "header_body_delimit_crnrn": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>(\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "header_body_delimit_crncrn": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>(\r\n)"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "header_body_delimit_cnrn": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>(\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "header_body_delimit_rcrn": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r/"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "header_body_delimit_rcnrn": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r<>\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "header_body_delimit_rncn": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"c\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "header_body_delimit_rncrn": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"<\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "header_body_delimit_rnrcn": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\"\"\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    # where is the start of body?
    "header_body_delimit_no_rn": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "header_body_delimit_rn_CTE_rn_body": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "header_body_delimit_rn_CTE_body": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "header_body_delimit_rn_l_CTE_rn_body": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"\r\n"
            b"A meaningless sentence.\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "header_body_delimit_rn_l_CTE_l_rn_body": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"\r\n"
            b"A meaningless sentence.\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"A meaningless sentence.\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "header_body_delimit_rn_l_CTE_l_body": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"\r\n"
            b"A meaningless sentence.\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"A meaningless sentence.\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "header_body_delimit_rn_spaceCTE_rn_body": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"\r\n"
            b" Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "header_body_delimit_l_CTE_body": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"A meaningless sentence.\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "header_redundant_bl_r_n": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "header_redundant_bl_r": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"\r"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "header_redundant_bl_n": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },

    # comment ===================
    # comment in CTE
    "comment_CTE_wrap_value": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: (<valid_CTE_here>)\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"comment in CTE"
    },
    "comment_CTE_wrap_invalid_b64": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: bas(comment sentence)e64\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"comment in CTE"
    },
    "comment_CTE_wrap_invalid_qp": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: quot(comment sentence)ed-printable\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"comment in CTE"
    },
    "comment_CTE_wrap_colon": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding(: )<valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"comment in CTE"
    },
    "comment_CTE_half_wrap_header": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfe(r-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"comment in CTE"
    },
    "comment_CTE_half_wrap_end_rn": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>(<invalid_CTE_here>\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"comment in CTE"
    },
    "comment_CTE_half_wrap_end_r": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>(<invalid_CTE_here>\r"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"comment in CTE"
    },
    "comment_CTE_half_wrap_end_n": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>(<invalid_CTE_here>\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"comment in CTE"
    },
    "comment_CTE_wrap_end_r": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>(<invalid_CTE_here>\r)"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"comment in CTE"
    },
    "comment_CTE_wrap_end_n": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>(<invalid_CTE_here>\n)"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"comment in CTE"
    },
    "comment_CTE_wrap_end_rn": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>(<invalid_CTE_here>\r)\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"comment in CTE"
    },
    # comment in boundary
    "comment_boundary_app_all": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo(foo)foo\r\n"
            b"\r\n"
            b"--foo(foo)foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo(foo)foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo(foo)foo--\r\n"
        ,
        "description": b"comment in boundary statement"
    },
    "comment_boundary_app_uncom": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo(foo)foo\r\n"
            b"\r\n"
            b"--foofoo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foofoo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foofoo--\r\n"
        ,
        "description": b"comment in boundary statement"
    },
    "comment_boundary_wrap_all_app_all": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=(foofoofoo)\r\n"
            b"\r\n"
            b"--(foofoofoo)\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--(foofoofoo)\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--(foofoofoo)--\r\n"
        ,
        "description": b"comment in boundary statement"
    },
    "comment_boundary_wrap_all_app_uncom": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=(foofoofoo)\r\n"
            b"\r\n"
            b"--\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"----\r\n"
        ,
        "description": b"comment in boundary statement"
    },
    "comment_boundary_half_wrap_start_app_all": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=(foo\r\n"
            b"\r\n"
            b"--(foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--(foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--(foo--\r\n"
        ,
        "description": b"comment in boundary statement"
    },
    "comment_boundary_half_wrap_start_app_uncom": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=(foo\r\n"
            b"\r\n"
            b"--\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"----\r\n"
        ,
        "description": b"comment in boundary statement"
    },
    "comment_boundary_half_wrap_end_app_all": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo(foo\r\n"
            b"\r\n"
            b"--foo(foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo(foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo(foo--\r\n"
        ,
        "description": b"comment in boundary statement"
    },
    "comment_boundary_half_wrap_end_app_uncom": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo(foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"comment in boundary statement"
    },

    # encoded word ================
    "ecdw_bound_app_decoded": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary==?US-ASCII?Q?foo?=\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"boundary statement in form of encoded-word"
    },
    "ecdw_bound_app_original": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary==?US-ASCII?Q?foo?=\r\n"
            b"\r\n"
            b"--=?US-ASCII?Q?foo?=\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--=?US-ASCII?Q?foo?=\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--=?US-ASCII?Q?foo?=--\r\n"
        ,
        "description": b"boundary statement in form of encoded-word"
    },
    "ecdw_CTE_all": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: =?US-ASCII?Q?<valid_CTE_here>?=\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"CTE in form of encoded-word"
    },
    "ecdw_CTE_all_encode_char_b64": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: =?US-ASCII?Q?base=364?=\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"CTE in form of encoded-word"
    },
    "ecdw_CTE_all_encode_char_qp": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: =?US-ASCII?Q?quote=64=2Dprintable?=\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"CTE in form of encoded-word"
    },
    "ecdw_CTE_part_b64": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: ba=?US-ASCII?Q?se64?=\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"CTE in form of encoded-word"
    },
    "ecdw_CTE_part_qp": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: quot=?US-ASCII?Q?ed-printable?=\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b"CTE in form of encoded-word"
    },

    # RFC 2231



    "half_paren_CTE": {
        "possible_data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: <SUBJECT>\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"<TEXT_PART>\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=<FILENAME>\r\n"
            b"Content-Transfer-Encoding: (<valid_CTE_here>\r\n"
            b"Content-Transfer-Encoding: <valid_CTE_here>"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
    },
}
