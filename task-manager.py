# Task Queue Functions
def insert_task(queue: list, task: list):
    queue.append(task)  

def extract_task(queue: list):
    if not is_empty(queue):
        return queue.pop(0)  
    return "Can't extract task. Queue is EMPTY."

def peek(queue: list):
    if not is_empty(queue):
        return queue[0] 
    return "Can't peek task. Queue is EMPTY."

def is_empty(queue: list):
    return len(queue) == 0  

def complete_next_task(queue: list):
    if is_empty(queue):
        return "Can't complete task. Queue is EMPTY."

    highest_priority_index = 0
    highest_priority = queue[highest_priority_index][2]
    for task in range(1, len(queue)):
        if highest_priority > queue[task][2]:
            highest_priority = queue[task][2]
            highest_priority_index = task

    return queue.pop(highest_priority_index)

tasks = []

# Get number of tasks from user
num_tasks = int(input("Number of Tasks: "))
while num_tasks < 0:
    num_tasks = int(input("Number of Tasks mustn't be negative: "))

# Input each task data
for i in range(num_tasks):
    print("\nTask: " + str(i + 1))
    
    title = input("Enter title: ")
    
    duration = int(input("Enter duration (in minutes): "))
    while duration < 0:
        duration = int(input("Duration mustn't be negative: "))
    
    priority = int(input("Enter priority (lower is higher): "))
    while priority < 0:
        priority = int(input("Priority mustn't be negative: "))

    insert_task(tasks, [title, duration, priority])

# Show all tasks in queue
print("\nAll Tasks in Queue: " + str(tasks))

print("\nCompleted Task: " + str(complete_next_task(tasks)))

print("\nAll Tasks in Queue: " + str(tasks))


