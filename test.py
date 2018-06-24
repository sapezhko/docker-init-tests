import concurrent.futures
import time

def foo(msg):
    print(msg)
    time.sleep(1)

def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        features = []
        for _id in range(10):
            features.append(executor.submit(foo, _id))
        concurrent.futures.wait(features)


if __name__=='__main__':
    main()