# samogłoska
polish_letter_frequency_vowel = [["a", "e", "i", "o", "u", "y"],
                                [9.9, 8.06, 8.21, 8.6, 2.5, 3.76]]
# spółgłoska
polish_letter_frequency_consonant = [["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"],
                           [1.47, 2.498, 3.25, 0.3, 1.42, 1.08, 2.28, 3.51, 3.92, 2.8, 5.72, 3.13, 0.14, 4.69, 4.98, 3.98, 0.04, 4.65, 0.02, 6.53]]

english_letter_frequency_vowel = [["a", "e", "i", "o", "u", "y"],
                            [8.167, 12.702, 6.966, 7.507, 2.758, 1.974]]

english_letter_frequency_consonant = [["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"],
                            [1.492, 2.782, 4.253, 2.228, 2.015, 6.094, 0.153, 0.772, 4.025, 2.406, 6.749, 1.929, 0.095, 5.987, 6.327, 9.056, 0.978, 2.36, 0.15, 0.074]]

deutsch_letter_frequency_vowel = [["a", "e", "i", "o", "u", "y"],
                            [7.094, 16.396, 6.55, 3.037, 5.161, 0.039]]

deutsch_letter_frequency_consonant = [["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"],
                            [1.886, 2.732, 5.076, 1.656, 3.009, 4.577, 0.268, 1.417, 3.437, 2.534, 9.776, 0.67, 0.018, 7.003, 7.27, 6.154, 0.846, 1.921, 0.034, 1.134]]


letter_frequency_vowel = [["a", "e", "i", "o", "u", "y"],
                          [0, 0, 0, 0, 0, 0]]

letter_frequency_consonant = [["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


polish_sum_vowel = 0
english_sum_vowel = 0
deutsch_sum_vowel = 0
polish_sum_consonant = 0
english_sum_consonant = 0
deutsch_sum_consonant = 0
text = " Wymysl i zaimplementuj sposob porownywania wynikowej tablicy czestosci z tablicami dla poszczegolnych jezykow"
#text = "It has also called into question claims by state Governor Greg Abbott who earlier this week hailed the"
# text = "Eine Legislaturperiode des Bundestages endet grundsatzlich nach vier Jahren oder davor durch Auflosung."
text = text.lower()
text = text.replace(" ", "")

for letter in text:
    for i in range(6):
        if letter_frequency_vowel[0][i] == letter:
            letter_frequency_vowel[1][i] += 1
        elif i == 5:
            for j in range(20):
                if letter_frequency_consonant[0][j] == letter:
                    letter_frequency_consonant[1][j] += 1

for i in range(6):
    if letter_frequency_vowel[1][i] != 0:
        letter_frequency_vowel[1][i] = float(letter_frequency_vowel[1][i]/len(text)*100)

for i in range(20):
    if letter_frequency_consonant[1][i] != 0:
        letter_frequency_consonant[1][i] = float(letter_frequency_consonant[1][i]/len(text)*100)

'''
for i in range(6):
    print(letter_frequency_vowel[0][i], " ", letter_frequency_vowel[1][i])

for i in range(20):
    print(letter_frequency_consonant[0][i], " ", letter_frequency_consonant[1][i])
'''

for i in range(6):
    polish_sum_vowel += abs(polish_letter_frequency_vowel[1][i] - letter_frequency_vowel[1][i])
    english_sum_vowel += abs(english_letter_frequency_vowel[1][i] - letter_frequency_vowel[1][i])
    deutsch_sum_vowel += abs(deutsch_letter_frequency_vowel[1][i] - letter_frequency_vowel[1][i])

minimum = min(polish_sum_vowel, english_sum_vowel, deutsch_sum_vowel)

if minimum == polish_sum_vowel:
    print("Samogłoski: Polski")
elif minimum == english_sum_vowel:
    print("Samogłoski: Angielski")
else:
    print("Samogłoski: Niemiecki")

for i in range(20):
    polish_sum_consonant += abs(polish_letter_frequency_consonant[1][i] - letter_frequency_consonant[1][i])
    english_sum_consonant += abs(english_letter_frequency_consonant[1][i] - letter_frequency_consonant[1][i])
    deutsch_sum_consonant += abs(deutsch_letter_frequency_consonant[1][i] - letter_frequency_consonant[1][i])

minimum = min(polish_sum_consonant, english_sum_consonant, deutsch_sum_consonant)

if minimum == polish_sum_consonant:
    print("Spółgłoski: Polski")
elif minimum == english_sum_consonant:
    print("Spółgłoski: Angielski")
else:
    print("Spółgłoski: Niemiecki")
