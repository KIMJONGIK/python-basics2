def frange(val, base=0.0, step=0.1):
    x = []
    if val < base:
        while val < base:
            x.append(val)
            val += step
    else:
        while base < val:
            x.append(base)
            base += step
    return(x)
print(frange(2))
print(frange(1.0, 2.0))
print(frange(1.0, 3.0, 0.5))