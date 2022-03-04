# Regels afbreken

## Formule rafeligheid
```python
lines = ["Lijn 1 tekst", "Lijn 2 tekst"]
max_len_regel = max(len(line) for line in lines)
rafel = sum((max_len_regel - len(line)**2 for line in lines))
```

## Constructie met minimale rafeligheid
```python
max_len = 80
input_text = "bla bla bla bla bla"
input_len = len(input_text)
result = []
index = 0
while index < input_len:
    start_index = index
    # advance max_len
    index += 80
    if index < input_len:
        # backtrack to prev whitespace
        while input_text[index] != " ":
            index -= 1
        result.append(input_text[start_index:index])
```

Opm: Het is waarschijnlijk mogelijk om de maximum en lengte van alle aparte onderdelen te berekenen in vorig stuk code.
Er wordt niet gevraagd naar de geformateerde tekst, enkel de rafeligheid!