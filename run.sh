#!/bin/bash

set -e

export DOCKER_REGISTRY=$1
export DOCKER_PROJECT=$2
export K8S_CONTEXT=$3
export K8S_NAMESPACE=$4
export K8S_DEPLOYMENT_INDEX=$5

envsubst < deployment.yaml.template > deployment.yaml
kubectl --context ${K8S_CONTEXT} -n ${K8S_NAMESPACE} create -f deployment.yaml