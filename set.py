#IMPLEMENTATION OF 10 OPERATIONS ON SETS
print("1:UNION OF A SET:")
print("2:INTERSECTION OF A SET:")
print("3:DIFFERENCE OF A SET:")
print("4:SYMMETRIC DIFFERENCE OF A SET:")
print("5:LENGTH OF A SET:")
print("6:CLEAR OF A SET:")
print("7:POP OF A SET:")
print("8:SUBSET OF A SET:")
print("9:SIZE OF A SET:")
print("10:ADD VALUE OF A SET:")
while True:
    choice=int(input("ENTER YOUR CHOICE:"))
    if choice==1:
        s1=set(input("enter the set 1?"))
        s2=set(input("enter the set 2?"))
        print(s1.union(s2))
    elif choice==2:
        s1=set(input("enter the set 1?"))
        s2=set(input("enter the set 2?"))
        print(s1.intersection(s2))
    elif choice==3:
        s1=set(input("enter the set 1?"))
        s2=set(input("enter the set 2?"))
        print(s1-s2)
    elif choice==4:
        s1 = set(input("enter the set 1?"))
        s2 = set(input("enter the set 2?"))
        print(s1.symmetric_difference(s2))
    elif choice==5:
        s1=set(input("enter the set?"))
        print(len(s1))
    elif choice==6:
        s1=set(input("enter the set?"))
        print(s1.clear())
    elif choice==7:
        s1=set(input("enter the set?"))
        print(s1.pop())
    elif choice==8:
        s1=set(input("enter the set 1?"))
        s2=set(input("enter the set 2?"))
        z=s1.issubset(s2)
        print(z)
    elif choice==9:
        s1=set(input("enter the set?"))
        print(s1.__sizeof__())
    elif choice==10:
        s1=set(input("enter the set?"))
        s1.add(100)
        print(s1)
        break
    else:
        print("INVALID CHOICE!")
