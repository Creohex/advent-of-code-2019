from math import atan2, pi


def monitoring_station(belt):
    asteroids = [(x, y) for y in range(len(belt))
                 for x in range(len(belt[0])) if belt[y][x] == "#"]
    station = {"x": 0, "y": 0, "reaches": 0}

    for x, y in asteroids:
        reaches = 0
        exhausted_angles = []

        for target_x, target_y in asteroids:
            angle = atan2(target_y - y, target_x - x)
            if angle not in exhausted_angles:
                reaches += 1
                exhausted_angles.append(angle)

        if reaches > station["reaches"]:
            station = {"x": x, "y": y, "reaches": reaches}

    return asteroids, station


def part_one(belt):
    return monitoring_station(belt)[1]["reaches"]


def part_two(belt):
    asteroids, station = monitoring_station(belt)
    asteroids.pop(asteroids.index((station["x"], station["y"])))
    asteroids = {asteroid: atan2(asteroid[1] - station["y"], asteroid[0] - station["x"])
                 for asteroid in asteroids}
    laser_angle = -pi / 2 - 0.0000000000000002
    destroyed_asteroids = 0

    def next_target(below_angle):
        possible = sorted([(coords, angle)
                           for coords, angle in asteroids.items()
                           if angle > below_angle], key=lambda a: a[1])
        targets = []

        if possible:
            angle = possible[0][1]
            for p in possible:
                if p[1] == angle:
                    targets.append(p)
                else:
                    break
        else:
            return None

        if len(targets) == 1:
            return targets[0]
        else:
            ranges = [abs(x - station["x"]) + abs(y - station["y"])
                      for x, y in [coords for coords, _ in targets]]
            return targets[ranges.index(min(ranges))]

    while True:
        target, angle = next_target(laser_angle) or next_target(-pi)

        if destroyed_asteroids == 199:
            return target[0] * 100 + target[1]
        else:
            del asteroids[target]
            destroyed_asteroids += 1
            laser_angle = angle

    return destroyed_asteroids


print(part_one(open("input.txt").readlines()))
print(part_two(open("input.txt").readlines()))
