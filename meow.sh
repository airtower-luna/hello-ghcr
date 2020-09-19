#!/bin/sh

# check if there's an integer parameter
if echo "${1}" | egrep -q '^[0-9]+$'; then
    m="${1}"
else
    m=1
fi

i=0
while [ $i -lt $m ]; do
    echo -n "Meow! "
    i=$((i + 1))
done
echo "=^.^="
