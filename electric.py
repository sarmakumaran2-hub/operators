unit=int(input("enter your units "))
if 0<unit<=90 :
    print("amount is ",unit*7)
elif 90<unit<=150 :
    extra=int(unit-90)
    print("amount is ",90*7+extra*10)
elif 150<unit<=300 :
    extra=int(unit-150)
    print("amount is ",90*7+60*10+extra*15)
elif unit>300 :
    extra=int(unit-300)
    price=(90*7+60*10+150*15)
    print("amount is ",price+price*3/100)
else:
    print("invalid")