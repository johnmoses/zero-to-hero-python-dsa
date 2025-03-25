""" 
Get speeds for different workloads
"""

import time

def getSpeeds1(workload):
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

def getSpeeds2(workload):
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

print(getSpeeds1(1000))
print(getSpeeds2(1000))