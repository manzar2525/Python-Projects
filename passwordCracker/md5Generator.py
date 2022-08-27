import hashlib

fr=open("password_list.txt","r")
fw=open("hash_list_md5.txt","w")




while True:
    password=fr.readline().strip()
    if not password:
        break;
    byteValue=hashlib.md5(password.encode('utf-8'))
    hashValue=byteValue.hexdigest()
    fw.write(hashValue)
    fw.write("\r")
print("Successfully generated")



