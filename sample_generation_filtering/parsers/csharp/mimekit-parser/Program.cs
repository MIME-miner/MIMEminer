using System;
using System.IO;
using System.Linq;
using MimeKit;

class Program
{
    static void Main(string[] args)
    {
        string inputFilePath = null;
        string outputDirectory = null;

        // 解析命令行参数
        for (int i = 0; i < args.Length; i++)
        {
            if (args[i] == "-i" && i + 1 < args.Length)
            {
                inputFilePath = args[i + 1];
            }
            else if (args[i] == "-o" && i + 1 < args.Length)
            {
                outputDirectory = args[i + 1];
            }
        }

        if (string.IsNullOrEmpty(inputFilePath) || string.IsNullOrEmpty(outputDirectory))
        {
            Console.WriteLine("Usage: -i <inputfile> -o <outputdirectory>");
            return;
        }

        // 检查输出目录是否存在，如果不存在，则创建
        if (!Directory.Exists(outputDirectory))
        {
            Directory.CreateDirectory(outputDirectory);
        }

        try
        {
            // 加载邮件
            var message = MimeMessage.Load(inputFilePath);

            // 提取附件
            foreach (var attachment in message.Attachments)
            {
                var fileName = attachment.ContentDisposition?.FileName ?? "attachment";
                var outputPath = Path.Combine(outputDirectory, fileName);

                // 将附件保存到输出目录
                using (var stream = File.Create(outputPath))
                {
                    if (attachment is MimePart)
                    {
                        var part = (MimePart)attachment;
                        Console.WriteLine($"Saving attachment: {part.FileName}");
                        part.Content.DecodeTo(stream);
                    }
                }

                Console.WriteLine($"Attachment saved: {outputPath}");
            }

            Console.WriteLine("Attachments extracted successfully.");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}