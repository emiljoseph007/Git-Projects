password=input("Please Enter Your Password:")
if len(password)< 8:
    print("Password Must Be Atleast 8 Characters Long")
else:
    print("")
pass2word=input("Please Re Enter Your Password:")
if password==pass2word:
    print("Password Is Corrcet ,! ACCESS GRANTED !")
else:
    print("Password Is Incorrect , ! ACCESS DENIED !")
    