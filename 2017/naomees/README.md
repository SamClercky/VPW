# Naomees

Simpele vraag met aan patern matching moet gedaan worden.

2 mogelijke oplossingsmethoden:
* Handmatig gaan checken -> `oplossing.py`
* Converteer de taal naar regex -> `alt_oplossing.py`

Regex lijkt op het eerste zicht sneller omdat het intern versneld kan worden, 
maar heeft het probleem met te algemeen te zijn.

Benchmarks:
```bash
$> hyperfine "python alt_oplossing.py <bench.input" "python oplossing.py <bench.input"
Benchmark 1: python alt_oplossing.py <bench.input
  Time (mean ± σ):      67.6 ms ±   8.4 ms    [User: 58.2 ms, System: 9.1 ms]
  Range (min … max):    55.9 ms …  88.3 ms    42 runs
 
Benchmark 2: python oplossing.py <bench.input
  Time (mean ± σ):      54.4 ms ±   8.9 ms    [User: 46.3 ms, System: 7.9 ms]
  Range (min … max):    41.8 ms …  70.3 ms    56 runs
 
Summary
  'python oplossing.py <bench.input' ran
    1.24 ± 0.26 times faster than 'python alt_oplossing.py <bench.input'
```
