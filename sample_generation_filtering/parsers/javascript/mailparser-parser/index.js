const fs = require('fs');
const path = require('path');
const simpleParser = require('mailparser').simpleParser;


// 获取命令行参数
const args = process.argv.slice(2);

if (args.length !== 4 || args[0] !== '-i' || args[2] !== '-o') {
    console.log('Usage: node extractAttachments.js -i <input_mail_file> -o <output_directory>');
    process.exit(1);
}

const inputFile = args[1];
const outputDir = args[3];

// 创建输出目录
if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir);
}

// 读取邮件文件
fs.readFile(inputFile, (err, data) => {
    if (err) {
        console.error('Error reading input file:', err);
        process.exit(1);
    }

    // 解析邮件

    simpleParser(data, (err, mail) => {
        if (err) {
            console.error('Error parsing mail:', err);
            process.exit(1);
        }

        // 保存邮件附件
        mail.attachments.forEach((attachment, index) => {
            const outputFilename = path.join(outputDir, attachment.filename);
            fs.writeFileSync(outputFilename, attachment.content);
            console.log('Saved attachment:', outputFilename);
        });
    });
});