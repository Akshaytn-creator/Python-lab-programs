#IMPLEMENTATION OF 10 OPERATIONS ON LIST
print("1:LENGTH OF A LIST:")
print("2:GET FIRST ELEMENT OF A LIST:")
print("3:GET LAST ELEMENT OF A LIST:")
print("4:SLICING OF A LIST:")
print("5:SORTING OF A LIST:")
print("6:REPETITION OF A LIST:")
print("7:CONCATENATION OF A LIST:")
print("8:MAXIMUM OF A LIST:")
print("9:MINIMUM OF A LIST:")
print("10:COUNT ELEMENT OF A LIST:")
while True:
    choice=int(input("ENTER YOUR CHOICE:"))
    if choice==1:
        l1=list(input("enter the list?"))
        print(len(l1))
    elif choice==2:
        l1=list(input("enter the list?"))
        print(l1[0])
    elif choice==3:
        l1=list(input("enter the list?"))
        print(l1[-1])
    elif choice==4:
        l1=list(input("enter the list?"))
        print(l1[2:4])
    elif choice==5:
        l1=list(input("enter the list?"))
        print(sorted(l1))
    elif choice==6:
        l1=list(input("enter the list?"))
        print(l1*2)
    elif choice==7:
        l1=list(input("enter the list 1?"))
        l2=list(input("enter the list 2?"))
        print(l1+l2)
    elif choice==8:
        l1=list(input("enter the list?"))
        print(max(l1))
    elif choice==9:
        l1=list(input("enter the list?"))
        print(min(l1))
    elif choice==10:
        l1=list(input("enter the set?"))
        z= input("enter element to count?")
        print(l1.count(z))
        break
    else:
        print("INVALID CHOICE!")
