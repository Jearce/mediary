#!/bin/bash
set -e
set -u
set -o pipefail

#get fixture directory
if [ $# -eq 0 ];
then
    echo "usage: load_data.sh <path to fixture>"
    echo "Submit one or more files."
    exit
fi

for file in "$@";
do
    fixture_name=$(basename $file)
    echo $fixture_name
    python manage.py loaddata $fixture_name
done


