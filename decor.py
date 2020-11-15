# use decorator for function parameters type check

from itertools import chain


def type_check(func):
    def checked(*args, **kwargs):
        a = iter(func.__annotations__.values())
        t = chain((type(a) for a in args), (type(k) for k in kwargs.values()))

        for a, t in zip(a, t):
            if a != t:
                raise ValueError(f'Wrong type: {t}. Expected: {a}')

        return func(*args, **kwargs)
    return checked


@ type_check
def power(x: int, p: int) -> int:
    print(x**p)


power(2, 2)
power(2, '2')
