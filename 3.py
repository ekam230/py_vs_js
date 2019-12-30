from time import time
start = time()
def func(a, b):
    print(a ** b)
func(123, 123)
end = round(time() - start, 3)
print(str(end) + " ms")