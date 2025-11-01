print("simple To_Do list")
print("option: add | remove | show | exit ")

tasks=[]
while True:
    action=input("what do you want to do:").lower()

    if  action == "add":
        task=input(f"add your new list:")
        tasks.append(task)
        print(f"new list is added")
    elif  action == "remove":
        task=input(f"add your remove list:")
        if task in tasks:
            tasks.remove(task)
            print(f"your list is removed")
        else:
            print(f"invaled list")
    elif action == "show":
        if len(tasks) == 0:
            print(f"list not yet")
        else:
            print(f"your To_Do list")
            for i in range(len(tasks)):
                print(f"{i+1} {tasks[i]}")
    elif action == "exit":
        print(f"Exiting To_Do list goodbye")
        break
    else:
        print(f"invaled option try again")


