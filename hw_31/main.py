def validate_args(*used_types):
    def wrapper_1(func):
        def wrapper_2(*args):
            try:
                for arg, arg_type in zip(args, used_types):
                    if not isinstance(arg, arg_type):
                        raise TypeError(f"Argument '{arg}' have wrong type {type(arg)}, must be {arg_type}.")
            except TypeError as err:
                print(err)
            else:
                return func(*args)
        return wrapper_2
    return wrapper_1

@validate_args(int, str)
def greet(age, name):
    print(f"Hello {name}! You are {age} years old.")


greet(33, 'Jeka')
greet("35", "Vika")
