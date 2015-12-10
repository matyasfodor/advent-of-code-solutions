import numpy as np

NEGATION = 0
AND = 1
OR = 3
LSHIFT = 4
RSHIFT = 5
NOTHING = 6

map_operators = {
    'NOT': NEGATION,
    'AND': AND,
    'OR': OR,
    'LSHIFT': LSHIFT,
    'RSHIFT': RSHIFT,
    'NOTHING': NOTHING,
}


class Connection:
    def __init__(self, operator=None, left_hand_operand=None, right_hand_operand=None):
        self.operator = operator
        self.left_hand_operand = left_hand_operand
        self.right_hand_operand = right_hand_operand

    def get_operands(self):
        return [operand for operand in [self.left_hand_operand, self.right_hand_operand] if isinstance(operand, basestring)]

    def get_left_hand_operand_value(self, solved_operands):
        if isinstance(self.left_hand_operand, basestring):
            return solved_operands[self.left_hand_operand]
        return self.left_hand_operand

    def get_right_hand_opernad_value(self, solved_operands):
        if isinstance(self.right_hand_operand, basestring):
            return solved_operands[self.right_hand_operand]
        return self.right_hand_operand

    def evaluate(self, solved_operands):
        if self.operator == NEGATION:
            return ~self.get_right_hand_opernad_value(solved_operands)
        if self.operator == AND:
            return self.get_left_hand_operand_value(solved_operands) & self.get_right_hand_opernad_value(solved_operands)
        if self.operator == OR:
            return self.get_left_hand_operand_value(solved_operands) | self.get_right_hand_opernad_value(solved_operands)
        if self.operator == LSHIFT:
            return self.get_left_hand_operand_value(solved_operands) << self.right_hand_operand
        if self.operator == RSHIFT:
            return self.get_left_hand_operand_value(solved_operands) >> self.right_hand_operand
        if self.operator == NOTHING:
            return self.get_left_hand_operand_value(solved_operands)

    @staticmethod
    def parse_from_parts(*args):
        if len(args) == 1:
            if args[0].isdigit():
                return np.uint16(args[0])
            return Connection(operator=NOTHING, left_hand_operand=args[0])
        if len(args) == 2:
            if args[0] == 'NOT':
                return Connection(operator=NEGATION, right_hand_operand=args[1] if not args[1].isdigit() else np.uint16(args[1]))
            raise ValueError('Invalid line: ' + str(args))
        if len(args) == 3:
            operator = map_operators[args[1]]
            return Connection(operator=operator,
                              left_hand_operand=args[0] if not args[0].isdigit() else np.uint16(args[0]),
                              right_hand_operand=args[2] if not args[2].isdigit() else np.uint16(args[2]))
        raise ValueError('Line length does not match: ' + str(args))


def parse_instruction(line):
    left_hand, target = line.split(' -> ')

    left_hand_parts = left_hand.split(' ')

    return target, Connection.parse_from_parts(*left_hand_parts)


class Circuit:
    def __init__(self, connections_by_output):
        self.connections_by_output = connections_by_output

    def get_wire_data(self, wire):
        while not isinstance(self.connections_by_output[wire], np.uint16):
            for key, value in self.connections_by_output.iteritems():
                if isinstance(value, Connection):
                    operands = value.get_operands()
                    if all([isinstance(self.connections_by_output[operand], np.uint16) for operand in operands]):
                        solved_operands = {}
                        for operand in operands:
                            solved_operands[operand] = self.connections_by_output[operand]
                        self.connections_by_output[key] = value.evaluate(solved_operands)
        return self.connections_by_output[wire]

    def set_value(self, key, value):
        self.connections_by_output[key] = value

    @staticmethod
    def parse_input(input_data):
        connections_by_output = {}
        for line in input_data:
            target, value = parse_instruction(line)
            connections_by_output[target] = value
        return Circuit(connections_by_output)


