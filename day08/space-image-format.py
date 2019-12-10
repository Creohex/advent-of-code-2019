def get_layers(pixels, frame):
    return [pixels[layer * frame:layer * frame + frame]
            for layer in range(len(pixels) // frame)]


def part_one(width, height, pixels):
    layers = sorted(get_layers(pixels, width * height), key=lambda l: l.count("0"))
    return layers[0].count("1") * layers[0].count("2")


def part_two(width, height, pixels):
    layers = get_layers(pixels, width * height)
    image = []
    pixels = ("0", "1")

    for pos in range(width * height):
        for l in layers:
            if l[pos] in pixels:
                image.append("*" if l[pos] == "1" else " ")
                break

    return "\n".join(["".join(image[row:row + width])
                      for row in range(0, len(image), width)])


print(part_one(25, 6, open("input.txt").read()))
print(part_two(25, 6, open("input.txt").read()))
