def delta(state, input_symbol):
    # Funkcja przejścia stanu
    transition_table = {
        'q0': {'a': 'q2', 'b': 'q2', 'c': 'q2'},
        'q1': {'a': 'q4', 'b': 'q0', 'c': 'q3'},
        'q2': {'a': 'q1', 'b': 'q1', 'c': 'q6'},
        'q3': {'a': 'q3', 'b': 'q3', 'c': 'q3'},
        'q4': {'a': 'q0', 'b': 'q5', 'c': 'q5'},
        'q5': {'a': 'q4', 'b': 'q4', 'c': 'q4'},
        'q6': {'a': 'q3', 'b': 'q3', 'c': 'q3'}
    }
    return transition_table[state][input_symbol]


# Zbiór stanów
states = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6']
# Zbiór symboli wejściowych
alphabet = ['a', 'b', 'c']
# Zbiór stanów końcowych
accepting_states = ['q0']

# Stan początkowy
current_state = 'q0'

# Pobieramy od użytkownika ciąg wejściowy
input_string = input("Podaj ciąg wejściowy: ")


for symbol in input_string:
    # Wykonujemy funkcję przejścia
    new_state = delta(current_state, symbol)
    # Wyświetlamy aktualną konfigurację automatu
    print("Aktualna konfiguracja: ({}, {})".format(current_state, symbol))
    # Przechodzimy do nowego stanu
    current_state = new_state

# Sprawdzamy, czy osiągnięty stan jest stanem końcowym
if current_state in accepting_states:
    print("Ciąg wejściowy jest akceptowany przez automat.")
else:
    print("Ciąg wejściowy nie jest akceptowany przez automat.")
