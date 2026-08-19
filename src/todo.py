def add_task(tasks: list, title: str) -> bool:
    title_cleaned = title.strip()
    if not title_cleaned:
        return False  # Invalid task title
    
    task = {"title": title_cleaned, "completed": False}
    tasks.append(task)
    return True  # Task added successfully

def view_tasks(tasks: list) -> None:
    if not tasks:
        print("\nNo tasks available.")
    
    print("\n" + "=" * 30)
    print("TO-DO LIST")
    print("=" * 30)
    
    for i, task in enumerate(tasks, start=1):
            status = "✓" if task["completed"] else "✗"
            print(f"{i}. [{status}] {task['title']}")

def mark_task_completed(tasks: list, index: int) -> bool:
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        return True
    return False 
        
def remove_task(tasks: list, index: int) -> None:
    if 0 <= index < len(tasks):
        return tasks.pop(index)
    return None  # Invalid index