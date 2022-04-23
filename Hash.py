def getSignedNumber(number, bitLength):
    mask = (2 ** bitLength) - 1
    if number & (1 << (bitLength - 1)):
        return number | ~mask
    else:
        return number & mask
 
def lshift(val, n): 
    return (int(val) << n) - 0x100000000 

             
def hash(d):
       d=d[:1024]
       p1= [getSignedNumber(ord(x),8) for x in d]
    
       leng = len(p1);
       i = 1;
       i1 = 0;
       i2 = i1;
       while (i1 < leng):
          
          i = (i + p1[i1]) % 0xc8cf;
          i2 = (i2 + i) % 0xc8cf;
          i1 = i1 + 1;
       
       return ("2:"+str(hex((~ (lshift( i2 ,16) | i))))[2:]).rstrip("L")
       
       
print(hash("abcd"))
