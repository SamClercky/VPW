# Beleefd

Programmeer technisch niet al te moeilijk. Moeilijk door wiskundige theorie.

Interessante linken:
* [https://nrich.maths.org/2074](https://nrich.maths.org/2074)
* [https://en.wikipedia.org/wiki/Polite_number](https://en.wikipedia.org/wiki/Polite_number)

Beleefd tot 20:
```
5 = 2 + ... + 3
6 = 1 + ... + 3
7 = 3 + ... + 4
9 = 2 + ... + 4
9 = 4 + ... + 5
10 = 1 + ... + 4
11 = 5 + ... + 6
12 = 3 + ... + 5
13 = 6 + ... + 7
14 = 2 + ... + 5
15 = 1 + ... + 5
15 = 4 + ... + 6
15 = 7 + ... + 8
17 = 8 + ... + 9
18 = 3 + ... + 6
18 = 5 + ... + 7
19 = 9 + ... + 10
20 = 2 + ... + 6
```

## Vinden van hoeveelheid beleefde nummers

Het aantal oneven delers groter dat 1 = aantal te vinden sequenties

### Aantal sequenties
1. Decompositie in priem getallen
2. Neem de machten van de priemfactoren groter dan 1 en +1 voor elk
3. Vermenigvuldig alle en dan -1

Vb. 90:
```
90 = 2 * 3^2 * 5^1
2,1 => (2+1) * (1+1) -1 = 5
```

### Constructie sequentie

```python
# x is totaal van som
# y is oneven deler
x = sum(i for i in range(x/y - (y-1)/2, x/y + (y+1)/2+1))
```
Het volstaat dus om enkel een priemfactorisatie te doen en de uiterste
te berekenen:
```python
eerste = x/y - (y-1)/2
laatste = x/y + (y+1)/2
```

```python
# https://stackoverflow.com/questions/567222/simple-prime-number-generator-in-python
def is_prime(num):
    if num < 2:         return False
    elif num < 4:       return True
    elif not num % 2:   return False
    elif num < 9:       return True
    elif not num % 3:   return False
    else:
        for n in range(5, int(math.sqrt(num) + 1), 6):
            if not num % n:
                return False
            elif not num % (n + 2):
                return False

    return True
```