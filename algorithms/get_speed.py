""" 
Get speed
"""

import time

def get_speeds_1(workload):
    """ 
    Get speeds for different workloads
    """
    print("%12s%16s" % ("Workload", "Seconds"))
    for count in range(5):
        start = time.time()
        work = 1
        for x in range(workload):
            work += 1
            work -= 1
        elapsed = time.time() - start

        print("%12d%16.3f" % (workload, elapsed))
        workload *= 2

def get_speeds_2(workload):
    """ 
    Get speeds for different workloads
    """
    print("%12s%16s" % ("Workload", "Seconds"))
    for count in range(5):
        start = time.time()
        work = 1
        for j in range(workload):
            for k in range(workload):
                work += 1
                work -= 1
        elapsed = time.time() - start

        print("%12d%16.3f" % (workload, elapsed))
        workload *= 2

workload = 1000
print(get_speeds_1(workload))
print(get_speeds_2(workload))