#!/bin/bash

a=1
b=2
c=3
echo "test"
if ((a < b)) ; then
    if ((c < 3)); then
        echo "b is better candidate"
    else 
        echo "c is better candidate"
    fi
fi
