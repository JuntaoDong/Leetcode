class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        lst = [True] * n
        lst[0] = lst[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if lst[i]:
                lst[i * i: n: i] = [False] * len(lst[i * i: n: i])
        return sum(lst)
