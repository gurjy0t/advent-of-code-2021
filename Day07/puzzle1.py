from os import PRIO_USER, PathLike, truncate
from typing import OrderedDict
import statistics



def main():
    nums=[]
    file = open("PuzzleDay7Input2.txt", "r")
    for line in file:
        for num in line.split(','):
            nums.append(int(num))
    file.close()
    # print("The original list : {}".format(nums))
  
    # Median of list
    # Using statistics.median()
    med = int(statistics.median(nums))

    print("Median of list is : {}".format(med))

    total_cost=0
    for num in nums:
        total_cost+=abs(num-med)

    print("Total fuel cost is: {}".format(total_cost))

if __name__ == "__main__":
    main()
