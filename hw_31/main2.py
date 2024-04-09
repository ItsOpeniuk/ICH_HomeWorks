import logging
logging.basicConfig(filename='log.txt', level=logging.INFO)
def log_decorator(func):

    def wrapper(*args, **kwargs):

        with open('log.txt', 'a') as file:
            result = func(*args, **kwargs)
            log_mess = f'Arguments: {args}, result: {result}\n'
            file.write(log_mess)
        return result
    return wrapper


@log_decorator
def add(a, b):
    return a + b

@log_decorator
def mull(a, b):
    return a * b

add(12, 22)
print(add(12, 24))
mull(45, 12)