#!/bin/sh

readonly FILENAME="all-trips.csv"

echo "Start station,Start time,End station,End time" > "${FILENAME}"

rm -f "${FILENAME}"

for CSVFILE in data/*.csv; do
    sed -n '1!p' "${CSVFILE}" >> "${FILENAME}"
done