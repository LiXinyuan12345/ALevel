import java.util.*;

class DataTypeDemo{

  // 整数数据类型，根据表示数的大小，分别用1,2,4,8bytes容纳

  byte    bMin = Byte.MIN_VALUE,    bMax = Byte.MAX_VALUE;   // 1个字节(8Bits)大小的正负整数 [-128 , +127]
  short   sMin = Short.MIN_VALUE,   sMax = Short.MAX_VALUE;  // 2个字节(16Bits)大小的正负整数 [-32768,32767]
  int     iMin = Integer.MIN_VALUE, iMax = Integer.MAX_VALUE;  // 4个字节(32Bits)大小的正负整数 [-2^31, 2^31 - 1]
  long    lMin = Long.MIN_VALUE,    lMax = Long.MAX_VALUE;  // 8个字节(64Bits)大小的正负整数 [-2^63, 2^63 - 1]

  // 小数数据类型，用4,8bytes容纳，double表达的小数位更多
  float   fMin = Float.MIN_VALUE,  fMax = Float.MAX_VALUE;   // 4个字节(32Bits)大小的小数
  double  dMin = Double.MIN_VALUE, dMax = Double.MAX_VALUE;  // 8个字节(64Bits)大小的小数

  boolean boolMin = false, boolMax = true;

  // 2个字节(16Bits)大小的单个字符，用Unicode Charset。
  char    cMin = Character.MIN_VALUE,     cMax = Character.MAX_VALUE;   
}


public class S1_DataType {
  
  public static void main(String[] args) {

       DataTypeDemo   d = new DataTypeDemo();

       /* byte  
        +--------+                 7f            |     ff           hex  
        |        |               +---+---+---+---+---+---+---+---+  
        | Byte 1 |   =  8bits =  | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |  max
        |        |               +---+---+---+---+---+---+---+---+ 
        +--------+                              127                 dec 
       */
       System.out.println("byte:\t"+ Byte.SIZE/8 + "bytes,\t Range=[" + d.bMin+ " , "+ d.bMax +"]"  );  
 
       /* short  
        +--------+--------+                        7f        |     ff                     ff       |      ff          hex  
        |        |        |                  +---+---+---+---+---+---+---+---+     +---+---+---+---+---+---+---+---+  
        | Byte 1 | Byte 2 |   =  16bits  =   | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |     | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |  max
        |        |        |                  +---+---+---+---+---+---+---+---+     +---+---+---+---+---+---+---+---+  
        +--------+--------+                                 127                  *                256                 dec        
       */
       System.out.println("short:\t"+ Short.SIZE/8 + "bytes,\t Range=[" + d.sMin+ " , "+ d.sMin +"]"  );  
 
       /* int                                                    7f        |     ff                     ff       |      ff          hex      
        +--------+--------+--------+--------+              +---+---+---+---+---+---+---+---+     +---+---+---+---+---+---+---+---+   
        |        |        |        |        |              | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |     | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 
        | Byte 1 | Byte 2 | Byte 3 | Byte 4 |  =  32bits = +---+---+---+---+---+---+---+---+     +---+---+---+---+---+---+---+---+  max
        |        |        |        |        |              | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |     | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |   
        +--------+--------+--------+--------+              +---+---+---+---+---+---+---+---+     +---+---+---+---+---+---+---+---+ 
                                                                 ff        |     ff                     ff       |      ff          hex  
                                                                                                            127 * 256 *256 * 256    dec
       */
       System.out.println("int:\t"+ Integer.SIZE/8 + "bytes,\t Range=[" + d.iMin+ " , "+ d.iMax +"]"  );  
 
       /* long  
        +--------+--------+--------+--------+--------+--------+--------+--------+
        |        |        |        |        |        |        |        |        |
        | Byte 1 | Byte 2 | Byte 3 | Byte 4 | Byte 5 | Byte 6 | Byte 7 | Byte 8 |  =  =  64bits
        |        |        |        |        |        |        |        |        |
        +--------+--------+--------+--------+--------+--------+--------+--------+
       */
       System.out.println("long:\t"+ Double.SIZE/8 + "bytes,\t Range=[" + d.lMin+ " , "+ d.lMin +"]"  );  
       System.out.println();  



 
 }
}