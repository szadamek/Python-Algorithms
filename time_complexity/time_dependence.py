import PA_zad1_lista4
from PA_zad1_lista4 import znajdz_najwiekszy_element, znajdz_drugi_najwiekszy_element, srednia
from PA_zad2_lista4 import multiplying_matrix
from PA_zad3_lista4 import has_subset_with_sum_zero
import random
import time
import numpy as np
import matplotlib.pyplot as plt


def zad1_max(n):
    lista = [random.randint(0, 5) for j in range(n)]
    start_time_zad1 = time.perf_counter()
    # zad1_max
    znajdz_najwiekszy_element(lista)
    # zad1_2nd_max
    znajdz_drugi_najwiekszy_element(lista)
    # zad1_mean
    PA_zad1_lista4.srednia(lista)
    stop_time_zad1 = time.perf_counter()
    elapsed_time = stop_time_zad1 - start_time_zad1

    return elapsed_time


# zad2
def zad2(size):
    # size = int(input('Podaj rozmiar macierzy: '))
    # macierz A
    A = np.random.randint(0, 5, (size, size))
    # macierz B
    B = np.random.randint(0, 5, (size, size))
    start_time_zad2 = time.perf_counter()
    multiplying_matrix(A, B)
    stop_time_zad2 = time.perf_counter()
    elapsed_time = stop_time_zad2 - start_time_zad2
    # print(f'Czas zadania 2: {elapsed_time:.6f} sekund')

    return elapsed_time


# zad3
def zad3(n):
    lista = [random.randint(-5, 5) for i in range(n)]
    start_time_zad3 = time.perf_counter()
    has_subset_with_sum_zero(lista)
    stop_time_zad3 = time.perf_counter()
    elapsed_time = stop_time_zad3 - start_time_zad3
    # print(f'Czas zadania 3: {elapsed_time:.6f} sekund')

    return elapsed_time


n = int(input('Podaj liczbę elementów listy: '))
times = []
for i in range(100, n, 200000):
    times.append(zad1_max(i))

# plot
plt.plot(times)
plt.xlabel('n')
plt.ylabel('czas')
plt.show()

# zad2
size = int(input('Podaj rozmiar macierzy: '))
zad2_times = []
for i in range(1, size, 4):
    zad2_times.append(zad2(i))

# plot
plt.plot(zad2_times)
plt.xlabel('size')
plt.ylabel('czas')
plt.show()

# zad3
n = int(input('Podaj liczbę elementów listy: '))
zad3_times = []
for i in range(1, n, 2):
    zad3_times.append(zad3(i))

# plot
plt.plot(zad3_times)
plt.xlabel('n')
plt.ylabel('czas')
plt.show()
