from numpy import linspace
import Node_SingleList
import random
import matplotlib.pyplot as plt

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
        print(counters)

    return time


counter1 = [["A", 0], ["A", 0], ["A", 0], ["B", 0], ["B", 0], ["B", 0], ["C", 0], ["C", 0], ["C", 0]]
counter2 = [["A", 0], ["A", 0], ["B", 0], ["B", 0], ["C", 0], ["C", 0], ["E", 0], ["E", 0], ["E", 0]]
counter3 = [["A", 0], ["B", 0], ["B", 0], ["C", 0], ["C", 0], ["C", 0], ["E", 0]]

print("Czasy dla okienek 3 roznych typow:")
print("Czas dla okienek(3A,3B,3C): ", urzad(counter1))
print("Czas dla okienek(2A,2B,2C,3E): ", urzad(counter2))
print("Czas dla okienek(1A,2B,3C,1E): ", urzad(counter3))
print("\n")

time1 = []
time2 = []
time3 = []

for time in range(0, 100):
    time1.append(urzad(counter1))
    time2.append(urzad(counter2))
    time3.append(urzad(counter3))

print("Średnie czasy dla okienek 3 roznych typow:")
print(f"Czas dla okienek(3A,3B,3C): {sum(time1)/100}")
print(f"Czas dla okienek(2A,2B,2C,3E): {sum(time2)/100}")
print(f"Czas dla okienek(1A,2B,3C,1E): {sum(time3)/100}")


names = ['(3A,3B,3C)', '(2A,2B,2C,3E)', '(1A,2B,3C,1E)']
values = [sum(time1)/100, sum(time2)/100, sum(time3)/100]
plt.suptitle('Średnie czasy dla danych wersji urzędu')
plt.xlabel('Wersja urzędu')
plt.ylabel('Czas')
plt.bar(names, values)
plt.show()


t = linspace(0, 100, 100)
plt.suptitle('Czasy 100 prób dla kolejki 30-osobowej')
plt.plot(t, time1, 'r')
plt.plot(t, time2, 'b')
plt.plot(t, time3, 'g')
plt.xlabel('Numer próby dla danej kolejki')
plt.ylabel('Czas')
plt.legend(["3A,3B,3C", "2A,2B,2C,2E", "1A,2B,3C,3E"], loc="upper right")
plt.show()


