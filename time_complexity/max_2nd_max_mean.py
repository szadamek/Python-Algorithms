import random


def znajdz_drugi_najwiekszy_element(lista_2nd_max):
    if lista_2nd_max[0] > lista_2nd_max[1]:
        najwiekszy = lista_2nd_max[0]
        drugi_najwiekszy = lista_2nd_max[1]
    else:
        najwiekszy = lista_2nd_max[1]
        drugi_najwiekszy = lista_2nd_max[0]

    for i in range(2, len(lista_2nd_max)):
        if lista_2nd_max[i] >= najwiekszy:
            drugi_najwiekszy = najwiekszy
            najwiekszy = lista_2nd_max[i]

    return drugi_najwiekszy


def znajdz_najwiekszy_element(lista_max):
    max_from_list = lista_max[0]
    for i in range(1, len(lista_max)):
        if lista_max[i] > max_from_list:
            max_from_list = lista_max[i]
    return max_from_list


def srednia(lista_mean):
    suma = 0
    for i in range(len(lista_mean)):
        suma += lista_mean[i]
    return suma / len(lista_mean)


if __name__ == '__main__':
    # losowa lista liczb
    lista = [random.randint(0, 5) for i in range(10)]
    print(lista)

    # największy element na liście
    max = znajdz_najwiekszy_element(lista)
    print(f'max = {max}')
    # drugi największy element na liście
    drugi_max = znajdz_drugi_najwiekszy_element(lista)
    print(f'drugi max = {drugi_max}')
    # średnia elementów na liście
    srednia = srednia(lista)
    print(f'srednia = {srednia}')

    # Złożoność czasowa dla każdego z algorytmów jest liniowa O(n),
    # ponieważ każdy z nich wykonuje się dokładnie tyle razy, ile wynosi długość listy.
