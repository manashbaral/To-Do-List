
#menu
def display_menu():
    while True:
        print("\n============================================================\n")
        print("\t|-------------------------------|")
        print("\t|\tTo-Do List Menu:\t|")
        print("\t|-------------------------------|")
        print("\t|\t1. Add Task\t\t|")
        print("\t|\t2. View Tasks\t\t|")
        print("\t|\t3. Remove Task\t\t|")
        print("\t|\t4. Update Task Status\t|")
        print("\t|\t5. Exit\t\t\t|")
        print("\t|-------------------------------|")

        choice = int(input("\n\tChoose an option (1-5):")) #get user choice

        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            remove_task()
        elif choice == 4:
            update_task_status()
        elif choice == 5:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

#add new task
def add_task():
    new_task=input("\n\tEnter a new task: ")

    #check if task already exists in the file
    with open("todo_list.txt","r+") as file: #r+ mode to read and write
        lines=file.readlines()

        for index,line in enumerate(lines):
            task_name=line.strip().split("-") #remove newline character and split by "-"
            task_name[0]=task_name[0].strip() #remove extra spaces

            if task_name[0]==new_task: #task already exists
                print("Task already exists in the to-do list.")
                return
        
        file.write(new_task.capitalize() + "-Incomplete\n") #add new task with incomplete status
    print("Task added successfully!")


#view all task
def view_tasks():
    with open("todo_list.txt","r") as file:
        lines=file.readlines()
        if not lines:
            print("No tasks in the to-do list.")
            return
        print("\t-------------------------------")
        print("\t\tTo-Do List:\t\t")
        print("\t-------------------------------")
        for index, line in enumerate(lines):
            print(f"\t{index+1}. {line.strip()}\t\t") #remove newline character and print the line
        print("\t-------------------------------\n\n")


#remove task
def remove_task():
    task_name=str(input("\n\tEnter the task name to be removed:")).strip() #get the task name to be removed
    
   #remove from the File 
    with open ("todo_list.txt","r") as file:
        lines=file.readlines()

        if not lines: #check if file is empty
            print("\tNo tasks in the to-do list.")
            return

    found=False #flag to check if task is found
    for index, line in enumerate(lines): #iterate through each line and enumerate to get index
        task=line.strip().split("-") #remove newline character and split by "-"
        task[0]=task[0].strip() #remove extra spaces

        if task[0].lower()==task_name.lower(): #check for the task to remove
            found=True
            lines.pop(index) #delete the line from the list
            break
    if not found: #task not found
            print("\tTask not found in the to-do list.")
            return

    with open ("todo_list.txt","w") as file: #write the updated list back to the file
        file.writelines(lines)
    print("\tTask removed successfully!")
    

#update task status
def update_task_status():
    
    task_to_update=str(input("\n\tEnter the task to update:")).strip() #get the task name to be updated
    
    
    with open ("todo_list.txt","r+") as file:
        lines=file.readlines()

        if not lines:
            print("\tNo tasks in the to-do list.")
            return
    
    found=False #flag to check if task is found
    for index, line in enumerate(lines):
        #remove newline character and split by "-"
        task=line.strip().split("-")
        task[0]=task[0].strip() #remove extra spaces
        task[1]=task[1].strip() #remove extra spaces

        #check for the task to update
        if task[0].lower()==task_to_update.lower(): #task found
            found=True
            print("\n\t\t**Press 1 to mark as complete**\n\t\t**Press 0 to mark as incomplete**\n") #display options
            new_status=int(input("\n\tEnter the new status of the task:")) #get the new status

            if new_status==1: #mark as complete
                lines[index]=f"{task[0]} - Complete\n" #update the line with complete status
                print("\tTask marked as complete.")

            elif new_status==0: #mark as incomplete
                lines[index]=f"{task[0]} - Incomplete\n" #update the line with incomplete status
                print("\tTask marked as incomplete.")
            else:
                print("\tInvalid status choice.") #invalid choice
                return
        if not found: #task not found
            print("\tTask not found in the to-do list.")
            return
        
    #rewrite the file with updated status
    with open ("todo_list.txt","w") as file:
        file.writelines(lines)          
   

display_menu()
