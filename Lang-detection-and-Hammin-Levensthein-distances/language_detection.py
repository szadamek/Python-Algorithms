polish_letter_frequency = [["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
                           [9.9, 1.47, 2.498, 3.25, 8.06, 0.3, 1.42, 1.08, 8.21, 2.28, 3.51, 3.92, 2.8, 5.72, 8.6, 3.13, 0.14, 4.69, 4.98, 3.98, 2.5, 0.04, 4.65, 0.02, 3.76, 6.53]]
english_letter_frequency = [["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
                            [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.36, 0.15, 1.974, 0.074]]
deutsch_letter_frequency = [["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
                            [7.094, 1.886, 2.732, 5.076, 16.396, 1.656, 3.009, 4.577, 6.55, 0.268, 1.417, 3.437, 2.534, 9.776, 3.037, 0.67, 0.018, 7.003, 7.27, 6.154, 5.161, 0.846, 1.921, 0.034, 0.039, 1.134]]


letter_frequency = [["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

polish_sum = 0
english_sum = 0
deutsch_sum = 0
text = " Wymysl i zaimplementuj sposob porownywania wynikowej tablicy czestosci z tablicami dla poszczegolnych jezykow"
#text = "It has also called into question claims by state Governor Greg Abbott who earlier this week hailed the"
# text = "Eine Legislaturperiode des Bundestages endet grundsatzlich nach vier Jahren oder davor durch Auflosung.
text = text.replace(" ", "")
text = text.lower()
print(text)
for letter in text:
    for i in range(26):
        if letter == letter_frequency[0][i]:
            letter_frequency[1][i] += 1

for i in range(26):
    if letter_frequency[1][i] != 0:
        letter_frequency[1][i] = float(letter_frequency[1][i]/len(text)*100)

'''
for i in range(26):
    print(letter_frequency[0][i], " ", letter_frequency[1][i])
'''

for i in range(26):
    polish_sum += abs(polish_letter_frequency[1][i] - letter_frequency[1][i])
    english_sum += abs(english_letter_frequency[1][i] - letter_frequency[1][i])
    deutsch_sum += abs(deutsch_letter_frequency[1][i] - letter_frequency[1][i])

minimum = min(polish_sum, english_sum, deutsch_sum)

if minimum == polish_sum:
    print("Polski")
elif minimum == english_sum:
    print("Angielski")
else:
    print("Niemiecki")
