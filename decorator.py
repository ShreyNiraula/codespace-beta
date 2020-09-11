import time

# decorator function 
def timer(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        f(*args, **kwargs)
        end = time.time()
        print(f'time taken ={(end-start)*1000} sec')
    return wrapper

# using the decorator 
@timer
def sqrtx(x):
    x = [i*i for i in x]
    print('after calculating square')

x = [i for i in range(100000)]
sqrtx(x)



    
