def fibThree(n: int) -> int:
    memo = [0, 1, 1]
    if n < 3:
        return memo[n]
    for i in range(3, n + 1):
        memo.append(sum(memo))
        memo.pop(0)
    return memo[-1]
