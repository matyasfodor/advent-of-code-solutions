from .aunt import NewAunt
from .utils import parse_tape
from .input_data import input_data, ticker_tape


def solution():
    query = parse_tape(ticker_tape)
    aunts = [NewAunt.parse_line(line) for line in input_data]
    best_match = None
    best_score = -float('inf')

    for idx, aunt in enumerate(aunts):
        score = aunt.get_score(query)

        if score > best_score:
            best_score = score
            best_match = idx

    return best_match + 1