# Classics
# Some maths: Number of all possible valid parenthesis of length n is the n-th Catalan number
def generateParenthesis(n: int) -> list[str]:
    def backtrack(opened, closed, path):
        if closed == n:
            res.append("".join(path))
            return
        if opened > closed:
            backtrack(opened, closed + 1, path + [")"])
        if opened < n:
            backtrack(opened + 1, closed, path + ["("])

    res = []
    backtrack(0, 0, [])
    return res
