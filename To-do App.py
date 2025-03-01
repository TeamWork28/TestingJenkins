tasks = []

def show_menu():
    print('1. Add task')
    print('2. View task')
    print('3. Remove task')
    print('4. Exit task')
    
while True:
    show_menu()
    choice = input('Enter your choice:')
    
    if choice == "1":
        task = input('Enter the task: ')
        tasks.append(task)
        print(f'task {task} added!')
        
    elif choice == "2":
        if tasks:
            for i, task in enumerate(tasks):
                print(f"{i}. {task}")
        else:
            print('No task to be shown')
            
    elif choice == "3":
        if tasks:
            for i, task in enumerate(tasks):
                print(f"{i}. {task}")
            try:
                task_num = int(input("Enter the task to be removed: ")) -1
                removed_task = tasks.pop(task_num)
                print(f"task '{removed_task}' removed!")
            except (IndexError, ValueError):
                print('Invalid, Please Enter the valid task number')
        else:
            print('No task to be removed')
            
    elif choice == "4":
        print("Exit the task")
        break
    else: 
        print('Invalid choice, Please enter the valid choice')
                
        