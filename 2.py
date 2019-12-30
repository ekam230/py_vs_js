from time import time
start = time()
i = 1
while i < 1001:
    print(i)
    i += 1
end = round(time() - start, 3)
print(str(end) + " ms")