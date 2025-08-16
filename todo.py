tasks = []

while True:
    task = input("Enter a task (or type 'done' to stop): ")
    if task.lower() == "done":
        break
    tasks.append(task)

print("\nYour To-Do List:")
for i, task in enumerate(tasks, 1):
    print(f"{i}. {task}")
