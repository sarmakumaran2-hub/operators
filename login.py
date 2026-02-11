user_name=("yarlit")
pass_word=int(1234)
Rol=("admin")
username=input("enter username ")

if username==user_name :
    password=int(input("enter password "))
    if password ==pass_word :
        rol=input("enter your rol ")
        if Rol==rol :
            print("welcome to admin board")
        else :
            print("welcome to user board")
    else:
        print("invalid password")
else :
    print("invalid username")