import sys


def hamming(first, second):
    sum = 0
    if len(first) != len(second):
        print("Słowa są różnej długości")
        return -1
    else:
        for i in range(len(first)):
            if first[i] != second[i]:
                sum += 1

    return sum


def hamming(first, second):
    sum = 0
    if len(first) != len(second):
        return 10000
    else:
        for i in range(len(first)):
            if first[i] != second[i]:
                sum += 1

    return sum


def location(letter):
    keyboard = [["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
                ["a", "s", "d", "f", "g", "h", "j", "k", "l"],
                ["z", "x", "c", "v", "b", "n", "m"]]
    for rows in range(3):
        if rows == 0:
            for columns in range(10):
                if str(letter) == keyboard[rows][columns]:
                    return [int(rows), int(columns)]
        elif rows == 1:
            for columns in range(9):
                if letter == keyboard[rows][columns]:
                    return [int(rows), int(columns)]
        elif rows == 2:
            for columns in range(7):
                if letter == keyboard[rows][columns]:
                    return [int(rows), int(columns)]


def hamming_mod(first, second):
    sum = 0
    if len(first) != len(second):
        print("Słowa są różnej długości")
        return -1
    else:
        for i in range(len(first)):
            coords = location(first[i])
            rows1 = coords[0]
            columns1 = coords[1]

            coords2 = location(second[i])
            rows2 = coords2[0]
            columns2 = coords2[1]

            if abs(rows1 - rows2) == 0 and abs(columns1 - columns2) == 1:
                sum += 1
            elif abs(rows1 - rows2) == 1 and abs(columns1 - columns2) == 0:
                sum += 1
            elif abs(rows1 - rows2) == 1 and abs(columns1 - columns2) == 1:
                sum += 2
            elif abs(rows1 - rows2) > 1 and abs(columns1 - columns2) == 1:
                sum += 2
            elif abs(rows1 - rows2) == 1 and abs(columns1 - columns2) > 1:
                sum += 2
            elif abs(rows1 - rows2) > 1 and abs(columns1 - columns2) > 1:
                sum += 2

    return sum


first_word = str(input("Podaj pierwsze słowo: "))
second_word = str(input("Podaj drugie słowo: "))

# A
length = hamming(first_word, second_word)
if length == 0:
    print("Słowa są indentyczne")
elif length > 0:
    print(f"Słowa mają odległość równą", length)

# B
length_mod = hamming_mod(first_word, second_word)
if length_mod == 0:
    print("Słowa są indentyczne")
elif length_mod > 0:
    print(f"Słowa mają odległość równą", length_mod)

# C
file = open('words.txt', "r")
distance = []
words = []
word = str(input("Podaj słowo: "))
for line in file:
    for w in line.split():
        if word == w:
            print("OK")
            sys.exit()
        else:
            distance.append(hamming(word, w))
            words.append(w)


min1 = min(distance)
index = distance.index(min1)
print(words[index])
distance.remove(min1)
words.remove(words[index])

min2 = min(distance)
index = distance.index(min2)
print(words[index])
distance.remove(min2)
words.remove(words[index])

min3 = min(distance)
index = distance.index(min3)
print(words[index])

file.close()
