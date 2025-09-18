def oscillate(start, stop):
    for i in range(start, stop):
        yield i
        if i != 0:
            yield -i

for n in oscillate(-3, 5):
    print(n, end=' ')
print()