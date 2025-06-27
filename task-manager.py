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

# Using Binary Search Algorithm
def search_for_task(queue: list, title: str):
    if is_empty(queue):
        return "This title is for sure isn't in the tasks. Queue is EMPTY."

    # Taking the titles only from the queue
    titles = [[task[0], i] for i, task in enumerate(queue)]

    # Insertion Sort
    for i in range(1, len(titles)):
        j = i

        while j > 0 and titles[j - 1] > titles[j]:
            titles[j - 1], titles[j] = titles[j], titles[j-1]
            j -= 1

    # Binary Search
    low = 0
    high = len(titles) -1

    while low <= high:
        mid = (low + high) // 2

        if titles[mid][0] == title:
            return "Task with title '" + title +"' found at index " + str(titles[mid][1]) + "."
        
        elif titles[mid][0] < title:
            low = mid + 1

        elif titles[mid][0] > title:
            high = mid - 1

    return "Task with title '" + title + "' not found."



tasks = []
priorities= []


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

    while priority < 0 or priority in priorities:
        priority = int(input("Priority mustn't be negative and must be unique: "))

    priorities.append(priority)

    insert_task(tasks, [title, duration, priority])

print("\nAll Tasks in Queue: " + str(tasks))

print("\nCompleted Task: " + str(complete_next_task(tasks)))

print("\nAll Tasks in Queue: " + str(tasks))


print(search_for_task(tasks,"Foo"))