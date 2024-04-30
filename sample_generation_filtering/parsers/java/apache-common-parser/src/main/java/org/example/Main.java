package org.example;

import org.apache.commons.mail.Email;
import org.apache.commons.mail.EmailAttachment;
import org.apache.commons.mail.EmailException;
import org.apache.commons.mail.MultiPartEmail;
import org.apache.commons.mail.util.MimeMessageParser;
import org.apache.commons.mail.util.MimeMessageUtils;

import javax.mail.MessagingException;
import javax.mail.internet.MimeMessage;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        String inputFile = null;
        String outputFolder = null;

        // 解析命令行参数
        for (int i = 0; i < args.length; i++) {
            if (args[i].equals("-i") && i + 1 < args.length) {
                inputFile = args[i + 1];
            } else if (args[i].equals("-o") && i + 1 < args.length) {
                outputFolder = args[i + 1];
            }
        }

        if (inputFile == null || outputFolder == null) {
            System.out.println("Usage: java EmailAttachmentExtractor -i <inputFile> -o <outputFolder>");
            return;
        }

        File inputEmail = new File(inputFile);
        if (!inputEmail.exists()) {
            System.out.println("Input email file does not exist.");
            return;
        }

        try {
            MimeMessage mimeMessage = MimeMessageUtils.createMimeMessage(null, inputEmail);
            MimeMessageParser parser = new MimeMessageParser(mimeMessage);
            parser.parse();

            File outputDir = new File(outputFolder);
            if (!outputDir.exists()) {
                outputDir.mkdir();
            }

            parser.getAttachmentList().forEach(attachment -> {
                try {
                    String outputFilePath = outputDir.getPath() + File.separator + attachment.getName();
                    FileOutputStream outputStream = new FileOutputStream(outputFilePath);
                    InputStream target = attachment.getInputStream();
                    byte[] buf = new byte[8192];
                    int length;
                    while ((length = target.read(buf)) != -1) {
                        outputStream.write(buf, 0, length);
                    }

                    outputStream.close();
                    System.out.println("Attachment saved: " + outputFilePath);
                } catch (IOException e) {
                    e.printStackTrace();
                }
            });

            System.out.println("Attachments extracted successfully.");
        } catch (IOException | MessagingException e) {
            e.printStackTrace();
        }
    }
}