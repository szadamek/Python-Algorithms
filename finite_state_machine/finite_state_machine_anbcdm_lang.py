def automaton(input_string):
    current_state = 0
    i = 0
    while i < len(input_string):
        if current_state == 0:
            if input_string[i] == 'a' and input_string[i + 1] == 'a':
                i += 1
            elif input_string[i] == 'a' and input_string[i + 1] != 'a':
                current_state = 1
                i += 1
            elif input_string[i] != 'a':
                current_state = 1
            else:
                return False
        elif current_state == 1:
            if input_string[i] == 'b':
                current_state = 2
                i += 1
            else:
                return False
        elif current_state == 2:
            if input_string[i] == 'c':
                current_state = 3
                i += 1
            else:
                return False
        elif current_state == 3:
            if input_string[i] == 'd':
                i += 1
            else:
                return False
    return True


input_str = str(input("Podaj ciąg wejściowy: "))
state = automaton(input_str)
if state:
    print("Ciąg wejściowy jest akceptowany przez automat.")
else:
    print("Ciąg wejściowy nie jest akceptowany przez automat.")
