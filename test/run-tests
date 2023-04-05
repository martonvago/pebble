#!/bin/bash

RED='\033[1;91m'
GREEN='\033[1;92m'
NC='\033[0m' # No Color
GREEN_HEART='\U0001f49a'
BROKEN_HEART='\U0001f494'

failed=0

for test_file in $(find ./*/ -name *.test.py)
do
    echo $test_file

    python3 $test_file

    failed=$(($failed+$?))      # add most recent status code to failed count

    echo ''
    
done

if [ $failed -gt 0 ]; then
    echo -e "${BROKEN_HEART} ${RED}TESTS FAILED${NC} ${BROKEN_HEART}"
else
    echo -e "${GREEN_HEART} ${GREEN}ALL TESTS PASSED${NC} ${GREEN_HEART}"
fi
