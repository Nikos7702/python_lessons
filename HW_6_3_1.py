def geometric_progression(start, ratio):
    current = start
    while True:
        yield current
        current *= ratio
progression = geometric_progression(2, 3)
for item in range(5):
    print(next(progression))
