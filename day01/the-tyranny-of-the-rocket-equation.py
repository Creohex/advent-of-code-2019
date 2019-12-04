def calculate_fuel(module_mass):
    return (int(module_mass) / 3) - 2


def part_one():
    return sum(calculate_fuel(module) for module in open("input.txt"))


def part_two():
    fuel = 0

    for mass in [calculate_fuel(module) for module in open("input.txt")]:
        fuel += mass
        additional = calculate_fuel(mass)

        while additional > 0:
            fuel += additional
            additional = calculate_fuel(additional)

    return fuel


print(part_one())
print(part_two())
