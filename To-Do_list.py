# Codsoft-Project
#To do list
#create, update, and track their to-do lists
print("To do list")
print(" 1 Create a new task \n 2 update task \n 3 Track to-do list \n 4 Exit")

task_list = []

print("Enter a number")
number = int(input())

if number == 1:
    print("Create a new Task")
    file_name = input()
    task = input()
    task_list.append((file_name, task))
    print(f"File Name: {file_name}\nTask: {task}")
    print("Task added successfully!")
   
    print("Enter a number to continue")
    new_number = int(input())
   
elif number == 2:
    print("Update Task")
    file_name = input()
    if file_name in task_list:
        print(f"File Name: {file_name}, Task: {task}")
        update_task = input()
        print(f"File Name: {file_name}\nupdated Task: {updated_task}")
        print("Task updated successfully!")
    else:
        print("file not found")
   
    print("Enter a number to continue")
    new_number = int(input())

elif number == 3:
        print("Track to-do list")
        if not task_list:
            print("No tasks found.")
        else:
            for file_name, task in task_list:
                print(f"File Name: {file_name}, Task: {task}")
        print("Enter a number to continue")
        new_number = int(input())
   
elif number == 4:
    print("Exit")

else:
    print("Please Enter a Valid number")
