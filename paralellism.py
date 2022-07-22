# Tired of implementing threads, queues, locks, etc to just run some task in paralell?
# Me too, luckly it's very easy with python
import concurrent.futures
import os
import time

def do_task(task):
    if task % 10 == 0:
        print(f"Uh! This is interesting! {task}")
    time.sleep(0.1)

def main():
    tasks = []
    for i in range(0, 1000):
        tasks.append(i)

    # We can use by default the same number of workers as CPU/cores we have
    with concurrent.futures.ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        executor.map(do_task, tasks)
        # For static/repeated args
        #executor.map(do_task, task, repeat(token))
        

if __name__ == "__main__":
    main()