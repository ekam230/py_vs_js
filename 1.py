from time import time
start = time()
for i in range(1, 1001):
    print(i)
end = round(time() - start, 3)
print(str(end) + " ms")