#!/usr/bin/env bash

curr_cwd=$(pwd)
md_dir="md"

cd ..
for year in $(ls); do
    if [[ -d $year ]] && [[ $year == 20* ]]; then
        pushd "$year"
        for opdracht in $(ls); do
            if [ -d $opdracht ]; then
                pushd "$opdracht"
                ls
                pandoc -t latex -o "$curr_cwd/$md_dir/$opdracht.tex" ./README.md
                popd
            fi
        done
        popd
    fi
done

