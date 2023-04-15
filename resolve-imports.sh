#!/bin/bash

# Script to resolve / parameterise the path to the project 
# root in imports in .tal files

while getopts c opt; do
   case $opt in
     c ) committing=1                       ;;
    \? ) echo "${0##*/} [ -c ]" >&2; exit 1 ;;
  esac
done

placeholder='<project-root>'

if [[ "${committing}" -eq 1 ]]; 
  then change="s|$PWD|$placeholder|g"; 
  else change="s|$placeholder|$PWD|g"; 
fi

find ./*/ -name *.tal -exec sed -i $change {} \;
