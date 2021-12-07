from os import PRIO_USER, PathLike, truncate
from typing import OrderedDict
import statistics



def main():
    nums=[]
    file = open("PuzzleDay7Input.txt", "r")
    for line in file:
        for num in line.split(','):
            nums.append(int(num))
    file.close()
  
    # Median of list
    # Using statistics.median()
    print(statistics.mean(nums))
    target = int((statistics.mean(nums)))

    print("Mean of list is : {}".format(target))

    total_cost=0
    for num in nums:
        amount_to_move = abs(num-target)
        total_cost+=calculate_fuel_used(amount_to_move)

    print("Total fuel cost is: {}".format(total_cost))

def calculate_fuel_used(distance):
    price_paid=0
    while distance > 0:
        price_paid += distance
        distance-=1
    
    return price_paid

if __name__ == "__main__":
    main()
