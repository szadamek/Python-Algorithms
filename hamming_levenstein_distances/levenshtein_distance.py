def levenshtein(first, second):

    tab = [[i + j for j in range(len(second) + 1)] for i in range(len(first) + 1)]

    for i in range(len(first) + 1):
        tab[i][0] = i
    for j in range(len(second)):
        tab[0][j] = j

    for i in range(1, len(first) + 1):
        for j in range(1, len(second) + 1):
            if first[i - 1] == second[j - 1]:
                cost = 0
            else:
                cost = 1
            tab[i][j] = min(tab[i-1][j] + 1, tab[i][j-1] + 1, tab[i-1][j-1] + cost)

    return tab

a = "foka"
b = "kotka"
tab = levenshtein(a, b)
print(tab[len(a)][len(b)])
