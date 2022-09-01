n1 = int(input("Enter first no = "))  # Question no :- 10
n2 = int(input("Enter second no = "))
n3 = int(input("Enter third no = "))

if n1>n2>n3:
    print(n1)
elif n1>n3>n2:
    print(n1)
elif n2>n1>n3:
    print(n2)
elif n2>n3>n1:
    print(n2)
elif n3>n1>n2:
    print(n3)
elif n3>n2>n1:
    print(n3)
else:
    print(n1)




