def main():
    file = open("PuzzleDay2Input.txt", "r")
    commands = file.readlines()
    file.close()
    h_pos = 0
    depth = 0
    F = "forward"
    U = "up"
    D = "down"
    for command in commands:
        direction, magnitude = command.split(" ")
        if direction == F:
            h_pos += int(magnitude)
        if direction == D:
            depth += int(magnitude)
        if direction == U:
            depth -= int(magnitude)

    print(
        "The final h_pos:{}, depth:{} multiplied:{}".format(h_pos, depth, h_pos * depth)
    )


if __name__ == "__main__":
    main()
