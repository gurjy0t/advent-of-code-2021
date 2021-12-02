def main():
    file = open("PuzzleDay1Input.txt", "r")

    increasing = 0
    nums = [int(num) for num in file.readlines()]
    file.close()

    prevSum = nums[0] + nums[1] + nums[2]
    prev = nums[2]
    prevPrev = nums[1]

    for curr in nums[3:]:
        currSum = curr + prev + prevPrev
        if currSum > prevSum:
            increasing += 1
        prevSum = currSum
        prevPrev = prev
        prev = curr

    print("The num increasing is: {}".format(increasing))


if __name__ == "__main__":
    main()
