#IMPLEMENTATION OF 10 OPERATIONS ON TUPLE
print("1:LENGTH OF A TUPLE:")
print("2:MAXIMUM OF A TUPLE:")
print("3:MINIMUM OF A TUPLE")
print("4:REPETITION OF A TUPLE:")
print("5:GET FIRST ELEMENT OF A TUPLE:")
print("6:SORTING OF A TUPLE:")
print("7:GET LAST ELEMENT OF A TUPLE:")
print("8:SLICING OF A TUPLE:")
print("9:CONCATENATION OF A TUPLE:")
print("10:ITERABLE OF A TUPLE:")
while True:
    choice=int(input("ENTER YOUR CHOICE:"))
    if choice==1:
        t1=tuple(input("enter the tuple?"))
        print(len(t1))
    elif choice==2:
        t1=tuple(input("enter the tuple?"))
        print(max(t1))
    elif choice==3:
        t1=tuple(input("enter the tuple?"))
        print(min(t1))
    elif choice==4:
        t1=tuple(input("enter the tuple?"))
        print(t1*2)
    elif choice==5:
        t1=tuple(input("enter the tuple?"))
        print(t1[1])
    elif choice==6:
        t1=tuple(input("enter the tuple?"))
        print(sorted(t1))
    elif choice==7:
        t1=tuple(input("enter the tuple?"))
        print(t1[-1])
    elif choice==8:
        t1=tuple(input("enter the tuple?"))
        print(t1[2:4])
    elif choice==9:
        t1=tuple(input("enter the tuple 1?"))
        t2=tuple(input("enter the tuple 2?"))
        print(t1+t2)
    elif choice==10:
        t1=tuple(input("enter the tuple?"))
        print(all(t1))
        break
    else:
        print("INVALID CHOICE!")
