
def geom_prog(a, q, count):
    result = a
    for _ in range(count):
        yield result
        result *= q

limit = 6
generator = geom_prog(-2, -5, limit)
print([item for item in generator])
print("-"*30)
generator = geom_prog(10, 3, limit)
print([item for item in generator])
