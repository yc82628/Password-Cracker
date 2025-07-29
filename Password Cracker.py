import hashlib

def crackHash(InputPass):
    try:
        passFile = open("wordlist.txt", "r")
    except:
        print("Could not find file.")
    
    for password in passFile:
        encPass = password.encode("utf-8")
        digest = hashlib.md5(encPass.strip()).hexdigest()
        if digest == InputPass:
            print("Password Found: " + password)

if __name__ == '__main__':
    crackHash("laldc91c987325c69271ddf0c944bc42")