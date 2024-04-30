<?php

require_once __DIR__.'/vendor/autoload.php';

use eXorus\PhpMimeMailParser\Parser;


// use -i flag to get the emailFilePath


// 解析命令行参数
$options = getopt("i:o:");

// 检查是否提供了-i和-o参数
if (!isset($options['i']) || !isset($options['o'])) {
    echo "Usage: php script.php -i <input_file> -o <output_file>\n";
    exit(1);
}

$emailFilePath = $options['i'];
$attach_dir = $options['o'];


if (!file_exists($emailFilePath)) {
    echo "Error: Input file does not exist.\n";
    exit(1);
}



$Parser = new Parser();
$Parser->setPath($emailFilePath); 

$to = $Parser->getHeader('to');

var_dump($to);

$from = $Parser->getHeader('from');
$subject = $Parser->getHeader('subject');

$text = $Parser->getMessageBody('text');
$html = $Parser->getMessageBody('html');


// $attach_dir = '/path/to/save/attachments/';

if (!file_exists($attach_dir)) {
    mkdir($attach_dir, 0777, true);
}

$attach_url = 'http://www.company.com/attachments/';
$Parser->saveAttachments($attach_dir, $attach_url);


$html_embedded = $Parser->getMessageBody('html', TRUE);
?>