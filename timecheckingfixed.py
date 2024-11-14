import time

problemSize = 1000000
print("%12s%16s" % ("ProblemSize", "Seconds"))
for count in range(5):
    start = time.time()
    
    for x in range(problemSize):
        pass 
    
    elapsed = time.time() - start
    print("%12d%16.3f" % (problemSize, elapsed))
    problemSize *= 2
