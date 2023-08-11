#!/bin/bash

# Set the Internal Field Separator to a newline character
IFS=$'\n'

# Specify the destination directory
destination="/mnt/d/coding/pro-b_lang_master/JavaScript/Expert"

# Iterate through each file in the current directory
for i in $(ls -v1 | grep -F '[Ex]'); do
    # Move the file to the specified destination directory
    mv "$i" "$destination$i"
done
