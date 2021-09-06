import multiprocessing
from multiprocessing import cpu_count

def worker():
    #worker function
    print ('Worker')
    x = 0
    while x < 100:
        print(x)
        x += 1
    return

if __name__ == '__main__':
    
    print(cpu_count())
    jobs = []
    for i in range(1):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()

