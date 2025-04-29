number  =  int(input("enter number"))
if number <0:
    print("number cant be zero")

else:
    factor =1
    for i in range(1,number+1):
        factor = factor*i
    print(factor)