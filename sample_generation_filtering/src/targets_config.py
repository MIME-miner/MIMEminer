fuzz_targets = {
    "mimekit-parser":{
        "name": "mimekit-parser",
        "cwd": "parser/csharp/mimekit-parser",
        "execute_str": "dotnet run -i {input_path} -o {output_path}",
    },
    "apache-common-parser":{
        "name": "apache-common-parser",
        "cwd": "parser/java/apache-commons-parser/targets",
        "execute_str": "java -jar apache-commons-parser-1.0-SNAPSHOT.jar -i {input_path} -o {output_path}",
    },
    "mailparser-parser":{
        "name": "mailparser-parser",
        "cwd": "parser/js/mailparser-parser",
        "execute_str": "node index.js -i {input_path} -o {output_path}",
    },
    "php-mime-mail-parser":{
        "name": "php-mime-mail-parser",
        "cwd": "parser/php/php-mime-mail-parser",
        "execute_str": "php index.php -i {input_path} -o {output_path}",
    },
    "email-parser":{
        "name": "email-parser",
        "cwd": "parser/python/email-parser",
        "execute_str": "python main.py -i {input_path} -o {output_path}",
    },
    "flanker-parser":{
        "name": "flanker-parser",
        "cwd": "parser/python/flanker-parser",
        "execute_str": "python main.py -i {input_path} -o {output_path}",
    },
    "mail-parser-parser":{
        "name": "mail-parser",
        "cwd": "parser/python/mail-parser-parser",
        "execute_str": "python main.py -i {input_path} -o {output_path}",
    },
}
