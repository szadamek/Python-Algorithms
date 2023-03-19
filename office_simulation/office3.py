import Node_SingleList
import random


def urzad(counters=[]):
    task_types = ["A", "B", "C"]
    queue = Node_SingleList.SingleList()

    for i in range(0, 30):
        task = random.choice(task_types)
        if task == "A":
            queue.insert_tail(Node_SingleList.Node(random.randint(1, 4)))
        elif task == "B":
            queue.insert_tail(Node_SingleList.Node(random.randint(5, 8)))
        else:
            queue.insert_tail(Node_SingleList.Node(random.randint(9, 12)))

    time = -1
    tasks_check = True
    while tasks_check:
        time += 1
        for task in range(len(counters)):
            if counters[task][1] > 0:
                counters[task][1] -= 1

        for counter in range(len(counters)):
            if counters[counter][1] == 0 and queue.length > 0:
                if counters[counter][0] == "A":
                    task = queue.search(1, 4)
                    if task != False:
                        counters[counter][1] = task
                        queue.deleteNode(task)
                elif counters[counter][0] == "B":
                    task = queue.search(5, 8)
                    if task != False:
                        counters[counter][1] = task
                        queue.deleteNode(task)
                elif counters[counter][0] == "C":
                    task = queue.search(9, 12)
                    if task != False:
                        counters[counter][1] = task
                        queue.deleteNode(task)
                elif counters[counter][0] == "E":
                    task = queue.search(1, 12)
                    if task != False:
                        counters[counter][1] = task
                        queue.deleteNode(task)

        tasks_check = False
        for tasks in range(len(counters)):
            if counters[tasks][1] > 0:
                tasks_check = True
                break

    return time

def urzad_A(counters=[]):
    task_types = ["A", "B", "C"]
    queue = Node_SingleList.SingleList()

    for i in range(0, 30):
        task = random.choice(task_types)
        if task == "A":
            queue.insert_tail(Node_SingleList.Node(random.randint(1, 4)))
        elif task == "B":
            queue.insert_tail(Node_SingleList.Node(random.randint(5, 8)))
        else:
            queue.insert_tail(Node_SingleList.Node(random.randint(9, 12)))

    queue.sortList_A()

    time = -1
    tasks_check = True
    while tasks_check:
        time += 1
        for task in range(len(counters)):
            if counters[task][1] > 0:
                counters[task][1] -= 1

        for counter in range(len(counters)):
            if counters[counter][1] == 0 and queue.length > 0:
                if counters[counter][0] == "A":
                    task = queue.search(1, 4)
                    if task != False:
                        counters[counter][1] = task
                        queue.deleteNode(task)
                elif counters[counter][0] == "B":
                    task = queue.search(5, 8)
                    if task != False:
                        counters[counter][1] = task
                        queue.deleteNode(task)
                elif counters[counter][0] == "C":
                    task = queue.search(9, 12)
                    if task != False:
                        counters[counter][1] = task
                        queue.deleteNode(task)
                elif counters[counter][0] == "E":
                    task = queue.search(1, 12)
                    if task != False:
                        counters[counter][1] = task
                        queue.deleteNode(task)

        tasks_check = False
        for tasks in range(len(counters)):
            if counters[tasks][1] > 0:
                tasks_check = True
                break

    return time


def urzad_D(counters=[]):
    task_types = ["A", "B", "C"]
    queue = Node_SingleList.SingleList()

    for i in range(0, 30):
        task = random.choice(task_types)
        if task == "A":
            queue.insert_tail(Node_SingleList.Node(random.randint(1, 4)))
        elif task == "B":
            queue.insert_tail(Node_SingleList.Node(random.randint(5, 8)))
        else:
            queue.insert_tail(Node_SingleList.Node(random.randint(9, 12)))

    queue.sortList_D()

    time = -1
    tasks_check = True
    while tasks_check:
        time += 1
        for task in range(len(counters)):
            if counters[task][1] > 0:
                counters[task][1] -= 1

        for counter in range(len(counters)):
            if counters[counter][1] == 0 and queue.length > 0:
                if counters[counter][0] == "A":
                    task = queue.search(1, 4)
                    if task != False:
                        counters[counter][1] = task
                        queue.deleteNode(task)
                elif counters[counter][0] == "B":
                    task = queue.search(5, 8)
                    if task != False:
                        counters[counter][1] = task
                        queue.deleteNode(task)
                elif counters[counter][0] == "C":
                    task = queue.search(9, 12)
                    if task != False:
                        counters[counter][1] = task
                        queue.deleteNode(task)
                elif counters[counter][0] == "E":
                    task = queue.search(1, 12)
                    if task != False:
                        counters[counter][1] = task
                        queue.deleteNode(task)

        tasks_check = False
        for tasks in range(len(counters)):
            if counters[tasks][1] > 0:
                tasks_check = True
                break

    return time


counter = [["A", 0], ["A", 0], ["A", 0], ["B", 0], ["B", 0], ["B", 0], ["C", 0], ["C", 0], ["C", 0], ["E", 0]]
counterA = [["A", 0], ["A", 0], ["A", 0], ["B", 0], ["B", 0], ["B", 0], ["C", 0], ["C", 0], ["C", 0], ["E", 0]]
counterD = [["A", 0], ["A", 0], ["A", 0], ["B", 0], ["B", 0], ["B", 0], ["C", 0], ["C", 0], ["C", 0], ["E", 0]]
timeA = []
timeD = []
time = []

for i in range(0, 100):
    timeA.append(urzad_A(counterA))
    timeD.append(urzad_D(counterD))
    time.append(urzad(counter))

print(f"Czas dla okienek uporządkowanych rosnąco: {sum(timeA)/100}")
print(f"Czas dla okienek uporządkowanych malejąco: {sum(timeD)/100}")
print(f"Czas dla okienek nieuporządkowanych: {sum(time)/100}")

