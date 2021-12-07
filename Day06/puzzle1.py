from os import PRIO_USER, PathLike, truncate
from typing import OrderedDict
import threading

def main():
    initial_lantern_fish = get_fish_from_file("PuzzleDay6Input.txt")
    final_fish = simulate_fish_growth_over_days(initial_lantern_fish.copy(), 80)
    print(len(final_fish))


def simulate_fish_growth_over_days(initial_fish, days):
    curr_day=0
    while curr_day < days:
        num_zeros = count_zeros(initial_fish)
        initial_fish=tick_timers_and_add_fish(initial_fish, num_zeros)
        curr_day+=1
    return initial_fish




def add_new_fish_for_zeros(fishes, num_to_add):
    i = 0
    while i < num_to_add:
        fishes.append(8)
        i+=1
    return fishes


def tick_timers_and_add_fish(fishes, num_zeros):
    i=0
    while i<len(fishes):
        if fishes[i]==0:
            fishes[i]=6
        else:
            fishes[i]-=1
        i+=1
    return add_new_fish_for_zeros(fishes, num_zeros)

def count_zeros(fishes):
    count=0
    for fish in fishes:
        if fish==0:
            count+=1
    return count

def get_fish_from_file(filename):
    file = open(filename, "r")
    initial_lantern_fish=[]
    for line in file:
        for fish in line.split(','):
            initial_lantern_fish.append(int(fish))
    file.close()
    return initial_lantern_fish


if __name__ == "__main__":
    main()
