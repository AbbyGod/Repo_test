print("TO DO LIST APP")
tasks = [] #initialize task
def add_task(task): 
    tasks.append(task) #I use this to add the task
    print(f"you added {task} in your to do list") # That is the result of user added task
def view_task(): # view your task , ifnot is when yo haven't add yet 
    if not tasks: 
     print("No task added yet")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):
         print(f"{i}. {task}")
while True: #this loop is to contineously ask user for input
    print("\nOptions: 1. Add Task  2. View Tasks  3. Exit") #if to elif is to control the menu bar 
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task: ")  #  Program now asks for input
        add_task(task)
    elif choice == "2":
        view_task()
    elif choice == "3":
        print("Goodbye!")
        break
    else: #to store user bad inputs
        print("Invalid choice, try again, please....")