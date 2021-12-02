def main():
    file = open("PuzzleDay1Input.txt", "r")
    count = -1
    prev = 0

    for curr in file:
        if int(curr) > prev:
            count += 1
        prev = int(curr)

    file.close()
    print("The num increasing is: {}".format(count))


if __name__ == "__main__":
    main()
