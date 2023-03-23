import json

# with open('automaton_language.json', 'r') as f:
#     json_text = f.read()
with open('zad3-language.json', 'r') as f:
    json_text = f.read()

data = json.loads(json_text)

states = data["states"]
alphabet = data["input_symbols"]
accept_states = data["accept_states"]
transitions = data["transitions"]
start_state = data["start_state"]

current_state = start_state
input_string = input("Podaj ciąg wejściowy: ")

for symbol in input_string:
    new_state = []
    for t in transitions:
        if t["current_state"] == current_state and t["symbol"] == symbol:
            new_state.append(t)
    print("Aktualna konfiguracja: ({}, {})".format(current_state, symbol))
    if len(new_state) > 0:
        current_state = new_state[0]["next_state"]
    else:
        print("Nie znaleziono przejścia dla symbolu {} i stanu {}".format(symbol, current_state))
        break

if current_state in accept_states:
    print("Ciąg wejściowy jest akceptowany przez automat.")
else:
    print("Ciąg wejściowy nie jest akceptowany przez automat.")
