#!/usr/bin/env bash

if [ -e "__pycache__" ]; then
    rm -r __pycache__ # make sure we get accurate time measure
fi

python ./oplossing.py3 <wedstrijd.invoer >wedstrijd.uitvoer_temp

echo "========================== INPUT/EXPECTED/ACTUAL ======================="
pr -m -t -W 150 wedstrijd.invoer wedstrijd.uitvoer "$wedstrijd_uitvoer"
echo "=========================== START OUTPUT ==============================="
delta -sn wedstrijd.uitvoer wedstrijd.uitvoer_temp
diff_status=$?
echo "============================ STATISTICS ================================"
if [ $diff_status -eq 0 ]; then
    echo "Correct"
else
    echo "Not yet correct"
fi

hyperfine "python ./oplossing.py3 <wedstrijd.invoer"

echo "=============================== END ===================================="
