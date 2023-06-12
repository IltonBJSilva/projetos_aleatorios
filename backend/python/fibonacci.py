import time

def fib_python(n):
    if n == 0 or n == 1:
        return n
    return fib_python(n-1) + fib_python(n-2)


start_time = time.time()
print(fib_python(35))
end_time = time.time()
print(end_time - start_time)