def generate_divisions(number, pieces):
    if pieces == 1:
        yield [number]
        return

    for i in range(1, number):
        for rest in generate_divisions(number - i, pieces - 1):
            yield [i] + rest
    return
