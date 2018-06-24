include common.mk

.PHONY: build push run clean
SHELL=/bin/bash

build:
	gcc -Wall -o main main.c
	docker build -t $(DOCKER_REGISTRY)/$(DOCKER_PROJECT)/signal-test:latest .

push: build
	docker push $(DOCKER_REGISTRY)/$(DOCKER_PROJECT)/signal-test:latest

run:
	./runner.py $(DOCKER_REGISTRY) $(DOCKER_PROJECT) $(K8S_CONTEXT) $(K8S_NAMESPACE)

clean:
	./clean.sh $(K8S_CONTEXT) $(K8S_NAMESPACE)
