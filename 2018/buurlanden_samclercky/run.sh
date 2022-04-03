#!/usr/bin/env bash

if [ -e "__pycache__" ]; then
    rm -r __pycache__ # make sure we get accurate time measure
fi

timing_program=$( ( time (python ./oplossing.py3 <wedstrijd.invoer >wedstrijd.temp_uitvoer) ) 2>&1)

echo "========================== INPUT/EXPECTED/ACTUAL ======================="
pr -m -t -W 150 wedstrijd.invoer wedstrijd.uitvoer wedstrijd.temp_uitvoer
echo "=========================== START OUTPUT ==============================="
diff -y wedstrijd.uitvoer wedstrijd.temp_uitvoer
diff_status=$?
echo "============================ STATISTICS ================================"
if [ $diff_status -eq 0 ]; then
    echo "Correct"
else
    echo "Not yet correct"
fi

echo "$timing_program"
#rm wedstrijd.temp_uitvoer

echo "=============================== END ===================================="
