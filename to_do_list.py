to_do = []

while True :
    print("=====MAIN MENU===== \n")
    print("1. Add task \n")
    print("2. View all tasks \n")
    print("3. Remove a task by number \n")
    print("4. Quit \n")

    ch = int(input("Enter your choice"))
    if ch == 1:
        task = input("Enter task to be done")
        to_do.append(task)
    elif ch == 2:
        for i, items in enumerate(to_do):
            print(f"{i+1}: {items}")
    elif ch == 3:
        remove_task = int(input("Enter task number to remove \n"))
        if 1 <= remove_task <= len(to_do):
            del to_do[remove_task-1]
            print("Task removed")
            # to_do.pop(remove_task-1)
        else:
            print("Invalid task number")
    elif ch == 4:
        break
    else:
        print ("Enter valid option")

    choice = input("Press Y to continue N to end")
    if choice == 'N' or choice == 'n':
        break 
  
