def powerset(S):
    if not S:
        ans =[[]] # not []
    else:
        loseit = powerset(S[1:])
        useit = list(map(lambda L: [S[0]] + L, loseit))
        ans = useit+loseit

    return ans
def comb(S,k):
    if not k:
        ans =[[]]
    elif not S:
        ans = []
    else:
        loseit = comb(S[1:],k)
        useit = list(map(lambda T: [S[0]] + T, comb(S[1:], k-1)))
        ans = useit+loseit
    return ans
