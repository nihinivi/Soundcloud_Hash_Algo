public class Main {
	
	
public static  String getV1Signature(String p0){
       byte[] p1= p0.getBytes(); 
       int len = p1.length;
       int i = 1;
       int i1 = 0;
       int i2 = i1;
       while (i1 < len) {
          
          i = (i + p1[i1]) % 0xc8cf;
          i2 = (i2 + i) % 0xc8cf;
          i1 = i1 + 1;
       }
       return  Integer.toHexString((~ ((i2 << 16) | i)));
        
    }
	public  static void main(String[] args) {
		System.out.println(getV1Signature("abcd"));
	}
}
