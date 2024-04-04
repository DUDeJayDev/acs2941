# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

from itertools import combinations


def combine(n: int, k: int) -> list[list[int]]:
    return combinations(range(1, n + 1), k)