
def geom_prog(a, q, count):
    result = a
    for _ in range(count):
        yield result
        result *= q

generator = geom_prog(-2, -5, 6)
print([item for item in generator])
print("-"*30)
generator = geom_prog(10, 3, 6)
print([item for item in generator])
