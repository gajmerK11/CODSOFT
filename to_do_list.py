tasks = []

print("\n")
print("Welcome to the to-do-list app :)")

def welcome_message():
    print("Select your choice")    
    print("1. Add task")
    print("2. List task")
    print("3. Delete task")
    print("4. Update task")
    print("5. Exit")
    print("\n")
    
def addTask():
    print("-------------------------------------")
    task = input("Enter task: ")
    tasks.append(task)
    print(f"Task '{task}' has been added to the list")
    print("\n")

def listTask():
    if not tasks:
        print("You have not added any task.")
    else:
        print("\n")
        print("Your tasks:")
        for index, value in enumerate(tasks):
            print(f"Task #{index}. {value}")
        print("\n")
        

def deleteTask():
    print("\n")
    print("Choose the task you want to delete:")
    listTask()
    task_to_delete = int(input("Enter # to delete: "))
    if task_to_delete >= 0 and task_to_delete < len(tasks):
        removed_task = tasks.pop(task_to_delete)
        print(f"Task '{removed_task}' deleted.")
        print("\n")
    else:
        print("Invalid number")
        print("\n")
    


def updateTask():
    listTask()
    task_to_update = int(input("Choose the task # you want to update: "))
    if task_to_update >= 0 and task_to_update < len(tasks):
        update_input = input("Enter the update: ")
        tasks[task_to_update] = update_input
        listTask()
    
    

while True:
    welcome_message()
    user_choice = int(input("Please enter your choice: "))
    if user_choice == 1:
        addTask()
    elif user_choice == 2:
        listTask() 
    elif user_choice == 3:
        deleteTask() 
    elif user_choice == 4:
        updateTask() 
    elif user_choice == 5:
        print("Goodbye 👋👋")
        break
    else:
        print("Invalid choice")









