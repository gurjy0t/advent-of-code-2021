def main():
    file = open("PuzzleDay3Input.txt", "r")
    nums = [x.strip() for x in file.readlines()]
    file.close()

    o2, co2 = get_most_and_least_at(nums, 0)

    pos = 1
    while len(o2)!=1:
        o2 = get_most_at(o2, pos)
        pos+=1
    
    print(o2)

    pos = 1
    while len(co2)!=1:
        co2 = get_least_at(co2, pos)
        pos+=1
    print(co2)

    print(int(o2[0], 2), int(co2[0], 2), int(o2[0], 2)*int(co2[0],2))




def get_most_and_least_at(nums, pos):
    return get_most_at(nums, pos), get_least_at(nums, pos)

def get_most_at(nums, pos):
    seen0, seen1 = 0, 0
    zeros, ones = [], []

    i=0
    while(i<len(nums)):
        if nums[i][pos]=='0':
            zeros.append(nums[i])
            seen0+=1
        else:
            ones.append(nums[i])
            seen1+=1
        i+=1
    
    if seen0 > seen1:
        return zeros
    else:
        return ones

def get_least_at(nums, pos):
    seen0, seen1 = 0, 0
    zeros, ones = [], []

    i=0
    while(i<len(nums)):
        if nums[i][pos]=='0':
            zeros.append(nums[i])
            seen0+=1
        else:
            ones.append(nums[i])
            seen1+=1
        i+=1
    
    if seen0 > seen1:
        return ones
    else:
        return zeros

if __name__ == "__main__":
    main()
