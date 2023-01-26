import string

def pangram(str):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        if i not in str.lower():
            return False

    return True

string=input("ENTER THE STRING : ")
if(pangram(string) ==True):
    print("YES")
else:
    print("NO")
