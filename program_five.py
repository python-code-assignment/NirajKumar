import re

password = "NirajKumar@"
flag = 0

while True:
    if (len(password) < 8):
        flag = -1
        print("Password must be minimum 8 characters")
        break
    elif not re.search("[a-z]", password):
        flag = -1
        print("Password must containe atleast one small letter")
        break
    elif not re.search("[A-Z]", password):
        print("Password must contain atleast one capital letter ")
        flag = -1
        break
    elif not re.search("[$#@]", password):
        flag = -1
        print("Password must contain $ or # or @")
        break
    else:
        flag = 0
        print("Valid Password")
        break
if flag == -1:
    print("Not a valid password!")