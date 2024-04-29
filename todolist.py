
def manage_tasks():
    task_list = []
    

    while True:
        user_choice = input("\nPlease choose:\n1 = Add task\n2 = List task\n3 = Remove task\nX = Exit\n")

        if user_choice not in ["1", "2", "3", "X", "x"]:
            print("\nInvalid option, please enter 1, 2, 3 or X")
            continue
            
        
        if user_choice == '1':
            add_task(task_list)
        elif user_choice == '2':
            list_tasks(task_list)
        elif user_choice == '3':
            remove_task(task_list)
        elif user_choice in ['X','x']:
            print("Exiting Task List")
            break


def add_task (task_list):
    task = input("\nEnter a task:\n")
    task_list.append(task)
    print(task_list)
    print("\nTask has been added!")

def list_tasks(task_list):
    print("\nTo-Do List:")
    if task_list:
        for index, task in enumerate(task_list, start=1):
            print(f"\n{index}. {task}")
    else:
        print("\nThere are no tasks")

def remove_task (task_list):
    list_tasks(task_list)

    if task_list:
        remove = int(input("\nWhat task do you want to remove?\n"))
        if 1 <= remove <= len(task_list):
            removed_task = task_list.pop(remove - 1)
            print(f"Removed task: {removed_task}")
        else:
            print("Enter a valid task number")
            

if __name__ == "__main__":    
        manage_tasks()

