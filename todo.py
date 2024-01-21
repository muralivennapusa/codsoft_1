todo=[]

def choice():
    print("\n________________________________________________________________\n")
    print("OPERATION ON TODO LIST:")
    print("1.Add")
    print("2.Delete")
    print("3.Update")
    print("4.Show")
    print("5.Exit")
    choice=int(input("Enter your choice: "))
    print("\n\n")
    return choice

def addtask():
    t=input("Enter task to add in list: \n")
    todo.append(t)
    return "Added task\n\n"

def deletetask():
    t=int(input("Enter task ID to delete in list: \n"))
    global todo
    if len(todo)==0:
        print("TODO list is empty DELETE TASK not possible")
        return "\nExiting \n\n"
    elif len(todo)<=t:
        print("invalid task ID")
        return "\nExiting\n\n"
    temp=todo[:t]+todo[t+1:]
    todo=temp
    return "Deleted task\n\n"

def updatetask():
    t=int(input("Enter task ID to update in list: \n"))
    if len(todo)==0:
        print("TODO is empty so UPDATE TASK not possible")
    elif len(todo)<=t:
        print("Invalid task ID")
        t=int(input("Enter new Task ID:"))
    todo[t]=input("Enter new task: \n")
    return "\nUpdated task\n\n"

def printtask():
    if(len(todo)==0):
        return "No tasks in TODO list"
    print("TODO list:")
    print("ID:  TaskName:")
    for i in range(0,len(todo)):
        print(i,todo[i],sep='\t')
    
    n=input("\nNOTE: press ENTER key to continue\n")    
    return "\nENDED\n\n"

while(1):
    t=choice()
    match t:
        case 1:
            print(addtask())
        case 2:
            print(deletetask())
        case 3:
            print(updatetask())
        case 4:
            print(printtask())
        case 5:
            print("________X________\n\nExiting the program.\n\n\n")
            break
        case _:
            print("Invalid choice")
