class TodoList:
    def __init__(self):
        self.tasks = []
        self.count = 0 # to count the number of tasks present in the list

    def add_task(self, task):      # used to add new task
        self.count += 1
        self.tasks.append(task)
        print("Task added successfully")

    def remove_task(self, task):   # used to remove a particular task
        if task <= self.count:
            print(f"{self.tasks.pop(task-1)} is successfully removed.")  
            self.count -= 1
        else:
            print("Task not found in the list.")
            
    def edit_task(self, index, new_task):   # used to edit an existing task
        if index <= self.count:
            self.tasks[index - 1] = new_task
            print("Task edited successfully")
        else:
            print("Task not found in the list.")        

    def display_tasks(self):            # used to display all tasks
        if self.tasks:
            print("Tasks in the to-do list:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("No tasks in the to-do list.")


todo_list = TodoList()
print('TODO LIST')
print("----------")
while True:
    try:
        print("\n1.Add Task \n2.Remove Task \n3.Display Task \n4.Edit Task \n5.Exit")
        choice = int(input("Enter your choice:"))
        if choice == 1:
            new_task = input("Enter your task here:")
            todo_list.add_task(new_task)
        elif choice == 2:
            task_to_remove = int(input("Enter the index task that you want to remove:"))
            todo_list.remove_task(task_to_remove)
        elif choice == 3:
            todo_list.display_tasks()
        elif choice == 4:
            task_to_edit = int(input("Enter the index of the task you want to edit: "))
            new_task_description = input("Enter the new description for the task: ")
            todo_list.edit_task(task_to_edit, new_task_description) 
    
        elif choice == 5:
            exit(0)
            
        print("-----------------------------------------------")    
    except ValueError:
        print("Please enter a valid integer choice.")
