import sys
import string
import hashlib

def checkPassword(message):
    uppers = ""
    lowers = ""
    digits = ""
    specialChars = ""
    sc = set(string.punctuation)
    l = [ str(x) for x in message]
    for j in range(len(l)):
        i = message[j]
        if i.isdigit():
            digits += i
        if i in sc:
            specialChars += i
        if i.isupper():
            uppers += i
        if i.islower():
            lowers += i
    
    if len(message) >= 10 and len(uppers) > 0 and len(lowers) > 0 and len(digits) > 0 and len(specialChars) > 0:
        return True
    else:
        return False
        
def encrypt(username,password):
    s = username[:3] + password[:3]
    m = hashlib.new('sha1')
    m.update(str.encode(s))
    salt = m.hexdigest()[:8]
    g = salt + password

    sha256 = hashlib.new('sha256')
    sha256.update(str.encode(g)) #salt and password

    shaString = sha256.hexdigest()

    shadow = username + "$"+ salt + "$" + shaString

    f = open("shadow.txt","a")
    f.write(shadow + '\n')
    f.close()



    

def main():
    password = ""
    username = ""

    username = input("choose username")
    while True:
        password = input("choose password ")
        if checkPassword(password) == True:
            break
        else:
            print("Your password is invalid")

    print(encrypt(username,password))

if __name__=="__main__":
    main()
    
