#!/bin/bash

set -e

kubectl --context $1 -n $2 delete deployment --force=true signal-test-$3
