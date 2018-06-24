#!/usr/bin/env python3

import sys
import subprocess
import random
import time
import concurrent.futures


MAX_POD_COUNT = 100
MAX_IN_PARALLEL_STOP = 5
AFTER_START_SLEEP = 180
AFTER_STOP_SLEEP = 180


def stop_pod(k8s_context, k8s_namespace, index):
    try:
        subprocess.run(args=["./stop.sh", k8s_context, k8s_namespace, str(index)],
                       check=True,
                       stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as err:
        print("Fail to stop pod {}".format(err))


def main(docker_registry, docker_project, k8s_context, k8s_namespace):
    random.seed()
    while True:
        cnt = random.randint(1, MAX_POD_COUNT)
        print('Spawn {} PODs'.format(cnt))
        for _id in range(cnt):
            subprocess.run(args=["./run.sh", docker_registry, docker_project, k8s_context, k8s_namespace, str(_id)],
                           check=True,
                           stderr=subprocess.STDOUT,
                           stdout=subprocess.PIPE)
        print('Sleep for {} seconds'.format(AFTER_START_SLEEP))
        time.sleep(AFTER_START_SLEEP)
        print('Stop all')
        in_parallel_stop = random.randint(1, min(MAX_IN_PARALLEL_STOP, cnt))
        print('Stop {} in parallel'.format(in_parallel_stop))
        with concurrent.futures.ThreadPoolExecutor(max_workers=in_parallel_stop) as executor:
            features = []
            for _id in range(cnt):
                features.append(executor.submit(stop_pod, k8s_context, k8s_namespace, _id))
            concurrent.futures.wait(features)
        print('Sleep for {} seconds'.format(AFTER_STOP_SLEEP))
        time.sleep(AFTER_STOP_SLEEP)
        print('Check for working pods')
        try:
            subprocess.run(args=["./check.sh", k8s_context, k8s_namespace],
                           check=True,
                           stderr=subprocess.STDOUT,
                           stdout=subprocess.PIPE)
        except subprocess.CalledProcessError as err:
            print('Check failed: {}'.format(err))
            exit(1)


if __name__=='__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])