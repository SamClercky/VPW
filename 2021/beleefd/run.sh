#!/usr/bin/env bash

rm -r __pycache__ # make sure we get accurate time measure

timing_program=$( ( time python ./oplossing.py3 <wedstrijd.invoer 1>wedstrijd.temp_uitvoer ) 2>&1)

echo "========================== INPUT/EXPECTED/ACTUAL ======================="
pr -m -t -W 150 wedstrijd.invoer wedstrijd.uitvoer wedstrijd.temp_uitvoer
echo "=========================== START OUTPUT ==============================="
diff -y wedstrijd.uitvoer wedstrijd.temp_uitvoer
diff_status=$?
echo "============================ STATISTICS ================================"
if [ $diff_status ]; then
    echo "Not yet correct"
else
    echo "Correct"
fi

echo $timing_program
rm wedstrijd.temp_uitvoer

echo "=============================== END ===================================="
