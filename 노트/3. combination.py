import itertools
def solution(nums):
    r = len(nums) // 2
    comb = list(itertools.combinations(nums, r))

    max_choice = 0
    for c in comb:
        max_choice = max(len(set(c)), max_choice)
        if max_choice == r:
            return r

    return max_choice