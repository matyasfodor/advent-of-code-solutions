def parse_tape(tape):
    return dict([(data[0], int(data[1])) for data in [record.split(': ') for record in tape]])
