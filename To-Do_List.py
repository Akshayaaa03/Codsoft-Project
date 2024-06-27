print("To-Do List Application")
print("MENU\n1 Create a new task \n 2 Update task \n 3 Track to-do list \n 4 Exit")

task_list = []

while True:
    print("\nEnter a number:")
    number = int(input())

    if number == 1:
        print("Create a new Task")
        file_name = input("Enter file name: ")
        task = input("Enter task: ")
        task_list.append((file_name))
        print("Task added successfully!")
        
    elif number == 2:
        print("Update Task")
        file_name = input("Enter file name: ")
        if file_name in task_list:
            updated_task = input("Enter updated task: ")
            print("Task updated successfully!")
        else:
            print("File not found")
        
    elif number == 3:
        print("Track to-do list")
        if not task_list:
            print("No tasks found.")
        else:
            for file_name in task_list:
                print(f"File Name: {file_name}")
                
    elif number == 4:
        print("Exit")
        break
        
    else:
        print("Please enter a valid number")
