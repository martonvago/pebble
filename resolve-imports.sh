#!/bin/bash

# Script to resolve / parameterise the path to the project 
# root in imports in .tal files

while getopts x opt; do
   case $opt in
     x ) undo=1                       ;;
    \? ) echo "${0##*/} [ -x ]" >&2; exit 1 ;;
  esac
done

placeholder='<project-root>'

if [[ "${undo}" -eq 1 ]]; 
  then change="s|$PWD|$placeholder|g"; 
  else change="s|$placeholder|$PWD|g"; 
fi

find ./*/ -name *.tal -exec sed -i $change {} \;
