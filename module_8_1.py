def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        return ('{}{}'.format(str(a), str(b)))


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(f"{add_everything_up(123.456, 7):.3f}")
