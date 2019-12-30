from time import time
start = time()
for i in range(1, 1001):
    if i % 5 == 0:
        print(i ** 10)
    else:
        print(i ** 123)
end = round(time() - start, 3)
print(str(end) + " ms")