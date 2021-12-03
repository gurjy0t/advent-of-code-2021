def main():
    file = open("PuzzleDay3Input.txt", "r")
    nums = [x.strip() for x in file.readlines()]
    file.close()

    seen0 = [0]*len(nums[0])
    seen1 = [0]*len(nums[0])

    i=0 
    while i < len(nums):
        pos = 0
        while pos<len(nums[i]):
            if nums[i][pos] == '0':
                seen0[pos]+=1
            else:
                seen1[pos] +=1
            pos+=1
        i+=1

    gamma = [0]*len(nums[0])
    epsilon = [0]*len(nums[0])
    i = 0
    while i < len(nums[0]):
        if seen0[i]>seen1[i]:
            gamma[i]=0
            epsilon[i]=1
        else:
            gamma[i]=1
            epsilon[i]=0
        i += 1

    print(i, gamma, epsilon)
    
    
    print((int(''.join([str(x) for x in gamma]), 2)))
    print((int(''.join([str(x) for x in epsilon]), 2)))

    print((int(''.join([str(x) for x in gamma]), 2)) * (int(''.join([str(x) for x in epsilon]), 2)))

if __name__ == "__main__":
    main()
