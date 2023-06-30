def limit_calls(max_calls):
    def decorator(func):
        def inner(*args, **kwargs):
            if inner.calls < max_calls:
                inner.calls += 1
                return func(*args, **kwargs)
            else:
                print("limit")
        inner.calls = 0
        return inner
    return decorator

@limit_calls(3)
def some_function():
    print("Виклик функції")

some_function()
some_function()
some_function()
some_function()
