#!/bin/sh

echo "Start station,Start time,End station,End time" > trips-2016-all.csv

rm -f all-trips.csv

for csvfile in data/*.csv; do
    sed -n '1!p' "$csvfile" >> all-trips.csv
done