


def encryption(msg):
    ct = []
    for char in msg:
        ct.append((123 * char + 18) % 256)
    return bytes(ct)
    
a=encryption([1,2,3,4,5,5,4,6])
print(a)
print(a.hex())

def decryption(msg):
    dc=[]
    flaglist=[]
    for i in range(len(msg) - 1, -1, -1):
        c=msg[i]
        #print(c,i)
          
        if i%2 ==0 and i!= len(msg) - 1 :
            a=int(msg[i], 16)
            b=int(msg[i+1],16)
            res =a*16+b 
            res=((res+238)*179) % 256
            dc.append(chr(res))
            a=0
            b=0         
  
    for i in range(len(dc) - 1, -1, -1):
        flaglist.append(dc[i])
        
    flag = ''.join(flaglist)
    print(flag)


        

print(decryption("6e0a9372ec49a3f6930ed8723f9df6f6720ed8d89dc4937222ec7214d89d1e0e352ce0aa6ec82bf622227bb70e7fb7352249b7d893c493d8539dec8fb7935d490e7f9d22ec89b7a322ec8fd80e7f8921"))