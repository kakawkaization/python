def adder(*args):
    c = args[0]
    for b in args[1:]:
        c += b
    return c

print(adder(1, 2))
