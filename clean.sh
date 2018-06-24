#!/bin/bash

set -e

for deployment in $(kubectl --context $1 -n $2 get deployment | grep signal-test- | awk '{print $1}'); do
    kubectl --context $1 -n $2 delete deployment $deployment;
done