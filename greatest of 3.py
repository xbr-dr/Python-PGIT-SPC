a = int(input("enter 1st no."))
b = int(input("enter 2nd no."))
c = int(input("enter 3rd no."))
if a > b and a > c:
    print("1st no entered is greatest which is", a)
elif b > c:
    print("2nd no entered is greatest which is", b)
else:
    print("3rd no entered is greatest which is", c)
