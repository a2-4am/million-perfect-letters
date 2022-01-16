#!/bin/sh

awk -F'|' '{print $2}' | \
    tr ',' '\n' | \
    sort | \
    uniq -c | \
    grep -v '  1 '
