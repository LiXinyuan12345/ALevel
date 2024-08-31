import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileReader;
import java.io.IOException;
import java.nio.charset.StandardCharsets;

public class S2_File {

    // 打印文本文件内容
    public static void print_txt_file_content(String filePath)
    {
        try {
            BufferedReader reader = new BufferedReader(new FileReader(filePath, StandardCharsets.UTF_16));
            String line;

            System.out.printf("\n\n%s\n",filePath);
            // 按行读取文件
            while ((line = reader.readLine()) != null) 
            {
                // 打印每一行
                System.out.println(line);
            }

            reader.close();

        } catch (IOException e) {
            e.printStackTrace();
        }        
    }

    // 打印二进制文件内容
    public static void print_bin_file_content(String filePath)
    {
        File    file = new File(filePath);
        try{
                // 将文件装入输入流
                FileInputStream stream = new FileInputStream(file);
        
                // 获取文件长度
                long fileLength = file.length();
                            
                // 创建适当大小的byte数组
                byte[] fileData = new byte[(int) fileLength];
                
                // 读取文件数据到byte数组
                stream.read(fileData);

                // 关闭输入流
                stream.close();

                // 打印读入的内容
                System.out.printf("\n\n%s\n",filePath);
                for (byte d:fileData)
                {
                    System.out.printf("%02X ", d);
                }
                
        }catch(IOException e){
            e.printStackTrace();
        }
    }


    public static void main(String[] args) {

        S2_File.print_bin_file_content("C:/Src/lxy/github/ALevel/AS/CS/1.Information_Representation/Charset//ascii.txt");
        //S2_File.print_txt_file_content("C:/Src/lxy/github/ALevel/AS/CS/1.Information_Representation/Charset//Unicode Charset.txt");

        S2_File.print_bin_file_content("C:/Src/lxy/github/ALevel/AS/CS/1.Information_Representation/Charset//Unicode Charset.txt");
        S2_File.print_bin_file_content("C:/Src/lxy/github/ALevel/AS/CS/1.Information_Representation/Image//Bitmap20X1.bmp");
    }
}
