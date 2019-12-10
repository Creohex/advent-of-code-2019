def build_tree(records, reverse=False):
    tree = {}

    for record in records:
        parent, child = record.strip().split(")")
        if reverse:
            tree[child] = tree.get(child, []) + [parent]
        else:
            tree[parent] = tree.get(parent, []) + [child]

    return tree


def part_one():
    orbit_map = build_tree(open("input.txt").readlines())

    orbit_count = 0
    depth = 0
    current_stack = orbit_map["COM"]
    next_stack = []

    while True:
        depth += 1

        for _ in range(len(current_stack)):
            body = current_stack.pop()
            next_stack.extend(orbit_map.get(body, []))
            orbit_count += depth

        if len(next_stack) > 0:
            current_stack = next_stack
            next_stack = []
        else:
            break

    return orbit_count


def part_two():
    orbit_map = build_tree(open("input.txt").readlines(), reverse=True)

    def get_parents(orbit_map, node):
        parents = []
        stack = orbit_map[node]

        while len(stack) > 0:
            parent = stack.pop()
            parents.append(parent)
            stack.extend(orbit_map.get(parent, []))

        return parents

    san_parents = get_parents(orbit_map, "SAN")
    you_parents = get_parents(orbit_map, "YOU")

    for parent in san_parents:
        if parent in you_parents:
            return san_parents.index(parent) + you_parents.index(parent)


print(part_one())
print(part_two())
