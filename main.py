# Є список чисел впорядкованих по зростаню.
# Напишіть функцію, що буде приймати два аргумента x, lst -
# і за допомогою алгоритма бінарного пошуку буде повертати True якщо x є у списку lst, i false у зворотньому.
def bi(x, lst):
    x2 = len(lst) // 2
    m = x2
    if x != lst[x2] and x != lst[0] and x != lst[-1]:
        while m > 0:
            if x > lst[x2]:
                m = m // 2
                x2 += m
                continue
            elif x < lst[x2]:
                m = m // 2
                x2 -= m
                continue
            elif x == lst[x2]:
                return True
        return False
    else:
        return True


# Написати декоратор, який при кожному виклику функції яку він декорує, буде писати яка функція виконалася
# і з якими аргументами. Тобто: # Є дві функції exampl_func_1, exampl_func_2
# Потрібно написати декоратор для цих функцій що після нього при кожному виклику цих функцій буде писати
# Function <function xxxx> was called with args .... kwargs ...
def w(f):
    def wrapper(*args, **kwargs):
        print(f'Function <{f}> was called with args {args} kwargs {kwargs}')
        r = f(*args, **kwargs)
        return r
    return wrapper


@w
def f1(a, b):
    return print(f'{a} + {b} =', a + b)


@w
def f2(a, b):
    return print(f'{a} - {b} =', a - b)


f1(5, 6)
f2(10, 20)
