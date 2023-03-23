# Definiujemy funkcję przejścia automatu
def delta(state, input_symbol):
    # Tabela przejść automatu
    transition_table = {
        'q0': {'0': 'q1', '1': 'q0'},
        'q1': {'0': 'q3', '1': 'q2'},
        'q2': {'0': 'q2', '1': 'q0'},
        'q3': {'0': 'q2', '1': 'q2'}
    }
    return transition_table[state][input_symbol]


# Definiujemy zbiór stanów automatu, alfabet wejściowy oraz zbiór stanów końcowych
states = ['q0', 'q1', 'q2', 'q3']
alphabet = ['0', '1']
accepting_states = ['q3']

# Definiujemy stan początkowy
current_state = 'q0'

# Pobieramy od użytkownika ciąg wejściowy
input_string = input("Podaj ciąg wejściowy: ")

# Symulujemy działanie automatu dla każdego symbolu wejściowego
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
