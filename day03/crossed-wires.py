def get_coords(instructions):
    coords = [(0, 0)]
    turns = {
        "U": (0, 1),
        "R": (1, 0),
        "D": (0, -1),
        "L": (-1, 0),
    }

    for i in instructions:
        for _ in range(int(i[1:])):
            x, y = turns[i[0]]
            coords.append((coords[-1][0] + x, coords[-1][1] + y))

    return coords[1:]


def part_one():
    coords = [set(get_coords(i.split(","))) for i in open("input.txt").readlines()]
    overlaps = coords[0].intersection(coords[1])
    return min(abs(overlap[0]) + abs(overlap[1]) for overlap in overlaps)


def part_two():
    coords = [get_coords(i.split(",")) for i in open("input.txt").readlines()]
    overlaps = set(coords[0]).intersection(set(coords[1]))
    return 2 + min(coords[0].index(overlap) + coords[1].index(overlap)
                   for overlap in overlaps)


print(part_one())
print(part_two())
