num1=int(input("enter num1 :"))
num2=int(input("enter num2 :"))
print("+ : 1","\n- : 2","\n* : 3","\n/ : 4")
click=int(input("click :"))
match click :
    case 1 :
        print(num1+num2)
    case 2 :
        print(num1-num2)
    case 3 :
        print(num1*num2)
    case 4 :
        print(num1/num2)
    case _ :
        print("invalid")