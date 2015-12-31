def parse_line(line):
    return tuple(atom.strip() for atom in line.split('=>'))
