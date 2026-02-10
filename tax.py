salary=int(input("enter your salary "))
print("basic salary :",salary)
if salary>=100000 :
    print("net salary is ",salary-salary*5/100)
elif salary>=80000 :
    print("net salary is ",salary-salary*3/100)
else:
    print("no tax   \nnet salary is ",salary)
 
