contacts = {}

while True :
    print("=====MAIN MENU===== \n")
    print("1. Add contact \n")
    print("2. Lookup by contact name \n")
    print("3. Print all records \n")

    ch = int(input("Enter your choice"))
    if ch == 1:
        name = input("Enter name")
        num = input("Enter phone number")
        contacts[name] = num
    elif ch == 2:
        name = input("Enter name to look for")
        if name in contacts:
            print(f"Name : {name} \n Phone : {contacts[name]}")
        else:
            print("Contact not found")
    elif ch == 3:
        for item, values in contacts.items():
            print (f"Name : {item}, Phone : {values} \n")
    else:
        print ("Enter valid option")

    choice = input("Press Y to continue N to end")
    if choice == 'N' or choice == 'n':
        break 
  
