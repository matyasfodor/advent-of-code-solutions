from collections import OrderedDict

from init_data import input_data, input_molecule
from util import parse_line


def parse_reverse_replacements(data):
    reverse_replacements = dict(parse_line(line)[::-1] for line in data)

    ordered_reverse_replacements = OrderedDict()
    for key in sorted(reverse_replacements.keys(), key=lambda x: len(x), reverse=True):
        ordered_reverse_replacements[key] = reverse_replacements[key]

    return ordered_reverse_replacements


def generate_replacement_step_lengths(reverse_replacements, molecule, steps=0):
    if molecule == 'e':
        return steps

    for replacement, origin in reverse_replacements.iteritems():
        steps += molecule.count(replacement)
        molecule = molecule.replace(replacement, origin)
    return generate_replacement_step_lengths(reverse_replacements, molecule, steps)


def solution():
    reverse_replacements = parse_reverse_replacements(input_data)
    return generate_replacement_step_lengths(reverse_replacements, input_molecule)
