while True:
    # taking input from the user
    num1=int(input("num1: - "))
    num2=int(input("num2: - "))
    opreation=input("opreation:_")
    # making calculation
    if opreation=="+":
      print(num1+num2)
    elif opreation== "-":
      print(num1-num2)
    elif opreation=="*":
      print(num1*num2)
    elif opreation=="/":
      print(num1/num2)
    else:
       ("invalid")