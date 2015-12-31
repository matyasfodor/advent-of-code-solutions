import re

from init_data import input_data, input_molecule
from .util import parse_line


def parse_replacements(data):
    replacements = {}
    for line in data:
        key, value = parse_line(line)
        replacements.setdefault(key, []).append(value)
    return replacements


def get_molecule_variation(replacements, molecule):
    for match_molecule, replacement_molecules in replacements.iteritems():
        for match in re.finditer(match_molecule, molecule):
            for replacement_molecule in replacement_molecules:
                start_point = match.start()
                yield molecule[0:start_point] + molecule[start_point:].replace(match_molecule, replacement_molecule, 1)
    return


def solution():
    replacements = parse_replacements(input_data)
    return len(set([variation for variation in get_molecule_variation(replacements, input_molecule)]))
