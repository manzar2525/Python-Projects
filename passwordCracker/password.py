import hashlib

print("enter your choice\n")
print("1.   if you want to enter md5 hash")
print("2.   if you want to enter SHA2 hash ")


choice=int(input())

if(choice==1):
    print("enter the plain text password")
    user_md5_hash=input().strip()
    fr_md5=open("hash_list_md5.txt","r")
    while True:
        h=fr_md5.readline().strip()
        print("hash stored: "+h)
        print("hash generated: "+user_md5_hash)
        if not h:
            break;
        if( user_md5_hash==h):
            print("password found")
            quit()
fr_hash=open("hash_list_sha2.txt","r")
while True:
    h = fr_hash.readline().strip()

    if not h:
        found=False
        break;
    if (sha2_hash== h):
        print("password found")
        break
print("Your password was safe")

if(found==False):
    fw_hash=open("hash_list_sha2.txt","a")
    fw_md5=open("hash_list_md5.txt","a")
    fw_hash.write(byte_cnvrt_sha2.hexdigest())
    fw_md5.write(byte_cnvrt_md5.hexdigest())
    fw_hash.write("\n")
    fw_md5.write("\n")
    print("Password updated successfully")


fw_md5.close()
fw_hash.close()
fr_hash.close()
fr_md5.close()