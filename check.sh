#!/bin/bash


kubectl --context $1 -n $2 get pod | grep -q signal-test-
if [ $? == 0 ]; then
    exit 1;
fi