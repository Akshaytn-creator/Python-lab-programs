#IMPLEMENTATION OF 10 OPERATIONS ON STRINGS
print("1:LENGTH OF A STRING:")
print("2:MAXIMUM OF A STRING:")
print("3:MINIMUM OF A STRING:")
print("4:UPPER OF A STRING:")
print("5:LOWER OF A STRING:")
print("6:CAPITALIZE OF A STRING:")
print("7:DIGIT OF A STRING:")
print("8:ALPHABET OF A STRING:")
print("9:CONCATENATION OF A STRING:")
print("10:ALPHABET/NUMERIC OF A STRING:")
while True:
    choice=int(input("ENTER YOUR CHOICE:"))
    if choice==1:
        s1=(input("enter your string?"))
        print(len(s1))
    elif choice==2:
        s1=(input("enter your string?"))
        print(max(s1))
    elif choice==3:
        s1=(input("enter your string?"))
        print(min(s1))
    elif choice==4:
        s1=(input("enter the string?"))
        print(s1.upper())
    elif choice==5:
        s1 = (input("enter the string?"))
        print(s1.lower())
    elif choice==6:
        s1=(input("enter the string?"))
        print(s1.capitalize())
    elif choice==7:
        s1=(input("enter the string?"))
        print(s1.isdigit())
    elif choice==8:
        s1=(input("enter the string?"))
        print(s1.isalpha())
    elif choice==9:
        s1=(input("enter the string 1?"))
        s2=(input("enter the string 2?"))
        print(s1+s2)
    elif choice==10:
        s1=(input("enter the string?"))
        print(s1.isalnum())
        break
    else:
        print("INVALID CHOICE!")
