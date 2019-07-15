def adder(**args):
    c = list(args.values())[0]
    for b in list(args.values())[1:]:
        c += b
    return c 

print(adder(a=1, f=3, g=6))
