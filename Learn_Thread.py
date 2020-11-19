import multiprocessing
import time

start = time.perf_counter()

def do_something(second):
    print(f"Sleep {second} second...")
    time.sleep(1)
    print("Don't sleeping...")

if(__name__ == "__main__"): 
    Processes = []
    for _ in range(10):
        p = multiprocessing.Process(target =do_something, args=[1.5])
        p.start()
        Processes.append(p)

    for process in Processes:
        process.join()

    finish = time.perf_counter()
    print(f"run take about {round(finish-start, 2)} seconds")

'''
if(__name__ == "__main__"): 
    p1 = multiprocessing.Process(target = do_something)
    p2 = multiprocessing.Process(target = do_something)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finish = time.perf_counter()

    print(f"run take about {round(finish-start, 2)} seconds")
'''