import Node_SingleList
import random


task_types = ["A", "B", "C"]
queue_A = Node_SingleList.SingleList()
queue_B = Node_SingleList.SingleList()
queue_C = Node_SingleList.SingleList()

for i in range(0, 40):
    task_type = random.choice(task_types)
    if task_type == "A":
        task_complexity = random.randint(1, 4)
        queue_A.insert_tail(Node_SingleList.Node(task_complexity))
    elif task_type == "B":
        task_complexity = random.randint(5, 8)
        queue_B.insert_tail(Node_SingleList.Node(task_complexity))
    else:
        task_complexity = random.randint(9, 12)
        queue_C.insert_tail(Node_SingleList.Node(task_complexity))


counters = [["A", 0], ["A", 0], ["A", 0], ["B", 0], ["B", 0], ["B", 0], ["C", 0], ["C", 0], ["C", 0], ["E", 0]]
clients = [["A", 0], ["A", 0], ["A", 0], ["B", 0], ["B", 0], ["B", 0], ["C", 0], ["C", 0], ["C", 0], ["E", 0]]

tasks_check = True
time = -1
while tasks_check == True:
    time += 1
    for task in range(len(counters)):
        if counters[task][1] > 0:
            counters[task][1] -= 1

    for counter in range(len(counters)):
        if counters[counter][1] == 0:
            if counters[counter][0] == "A" and queue_A.length > 0:
                counters[counter][1] = queue_A.remove_head()
                clients[counter][1] += 1
            if counters[counter][0] == "B" and queue_B.length > 0:
                counters[counter][1] = queue_B.remove_head()
                clients[counter][1] += 1
            if counters[counter][0] == "C" and queue_C.length > 0:
                counters[counter][1] = queue_C.remove_head()
                clients[counter][1] += 1
            if counters[counter][0] == "E" and (queue_A.length+queue_B.length+queue_C.length) > 0:
                sum_A = queue_A.sum_q()
                sum_B = queue_B.sum_q()
                sum_C = queue_C.sum_q()
                priority = max(sum_A, sum_B, sum_C)
                if priority == sum_A:
                    counters[counter][1] = queue_A.remove_head()
                    clients[counter][1] += 1
                elif priority == sum_B:
                    counters[counter][1] = queue_B.remove_head()
                    clients[counter][1] += 1
                elif priority == sum_C:
                    counters[counter][1] = queue_C.remove_head()
                    clients[counter][1] += 1

    tasks_check = False
    for tasks in range(len(counters)):
        if(counters[tasks][1] > 0):
            tasks_check = True
            break
    print(counters)

print(f"Liczba obsluzonych klientow w poszczegolnych okienkach: \n {clients} \n W czasie: {time}")