from .utils import parse_tape


class Aunt(object):
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

    def get_score(self, query):
        matches = 0
        fails = 0
        missing = 0

        for key in query.keys():
            if key not in self.__dict__:
                missing += 1
                continue

            if self.__dict__[key] == query[key]:
                matches += 1
            else:
                fails += 1

        return matches - fails - missing

    @classmethod
    def parse_line(cls, line):
        values_string = line[line.find(':') + 2:]
        return cls(**parse_tape(values_string.split(', ')))


class NewAunt(Aunt):

    GREATER_THAN = ['cats', 'trees']
    FEWER_THAN = ['pomeranians', 'goldfish']

    def __init__(self, **kwargs):
        super(NewAunt, self).__init__(**kwargs)

    def get_score(self, query):
        matches = 0
        fails = 0
        missing = 0

        for key in query.keys():
            if key not in self.__dict__:
                missing += 1
                continue

            if key in self.GREATER_THAN:
                if self.__dict__[key] > query[key]:
                    matches += 1
                    continue
            elif key in self.FEWER_THAN:
                if self.__dict__[key] < query[key]:
                    matches += 1
                    continue
            else:
                if self.__dict__[key] == query[key]:
                    matches += 1
                    continue
            fails += 1

        return matches - fails - missing
