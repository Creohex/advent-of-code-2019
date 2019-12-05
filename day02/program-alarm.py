def part_one():
    ops = [int(value) for value in open("input.txt").readline().split(",")]
    cursor = 0
    ops[1] = 12
    ops[2] = 2

    while ops[cursor] != 99:
        if ops[cursor] == 1:
            ops[ops[cursor + 3]] = ops[ops[cursor + 1]] + ops[ops[cursor + 2]]
        elif ops[cursor] == 2:
            ops[ops[cursor + 3]] = ops[ops[cursor + 1]] * ops[ops[cursor + 2]]
        cursor += 4

    return ops[0]


def part_two():
    opcodes = [int(value) for value in open("input.txt").readline().split(",")]
    target = 19690720

    for noun in range(100):
        for verb in range(100):
            cursor = 0
            ops = list(opcodes)
            ops[1] = noun
            ops[2] = verb

            while ops[cursor] != 99:
                if ops[cursor] == 1:
                    ops[ops[cursor + 3]] = ops[ops[cursor + 1]] + ops[ops[cursor + 2]]
                elif ops[cursor] == 2:
                    ops[ops[cursor + 3]] = ops[ops[cursor + 1]] * ops[ops[cursor + 2]]
                cursor += 4

            if ops[0] == target:
                return 100 * noun + verb


print(part_one())
print(part_two())
