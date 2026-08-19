import todo

def show_menu():
    print("\n" + "=" * 30)
    print("TO-DO LIST")
    print("=" * 30)
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as completed")
    print("4. Remove a task")
    print("5. Exit")
    print("=" * 30)
    
def main():
    tasks = []
    
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            todo.add_task(tasks)
        elif choice == '2':
            todo.view_tasks(tasks)
        elif choice == '3':
            task_index = int(input("Enter the task number to mark as completed: ")) - 1
            todo.mark_task_completed(tasks)
        elif choice == '4':
            task_index = int(input("Enter the task number to remove: ")) - 1
            todo.remove_task(tasks, task_index)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()