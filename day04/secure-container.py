def conforms(password):
    password = str(password)
    has_same_adjacent = False
    ever_increasing = True
    prev = password[0]

    for char in password[1:]:
        if char == prev:
            has_same_adjacent = True
        if ord(char) < ord(prev):
            ever_increasing = False
        prev = char

    return has_same_adjacent and ever_increasing


def adjacent_are_not_part_of_larger_group(password):
    password = str(password)
    groups = []
    current_group = prev = password[0]
    skip = None

    for char in password[1:]:
        current_group += char
        if skip and char == skip:
            continue
        else:
            if prev == char:
                if len(current_group) > 2:
                    del groups[-1]
                    skip = char
                else:
                    groups.append(current_group)
            else:
                current_group = char
            prev = char

    return len(groups) > 0


def part_one():
    return len(filter(conforms, range(125730, 579382)))


def part_two():
    return len(filter(adjacent_are_not_part_of_larger_group,
        filter(conforms, range(125730, 579382))))


print(part_one())
print(part_two())
