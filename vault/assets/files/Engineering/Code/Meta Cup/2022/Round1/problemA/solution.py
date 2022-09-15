#%%
with open ("Round1/problemA/consecutive_cuts_chapter_1_input.txt", "r") as myfile:
    data = myfile.read().splitlines()
    T = int(data[0])
    data = data[1:]
# %%

def solve(A,B,n,k):
    if k == 0: return 'YES' if A == B else 'NO'
    if k == 1 and A == B: return 'NO'
    if n == 2:
        if k%2 == 0: return 'YES' if A == B else 'NO'
        else: return 'YES' if A != B else 'NO'
    j = B.index(A[0])
    cyclic = (A[:n-j] == B[j:]) and (A[n-j:] == B[:j])
    if not cyclic: return 'NO'
    return 'YES'

ans = []
for i in range(T):
    N, K = tuple(map(int,data[3*i].split(' ')))
    A = list(map(int,data[3*i+1].split(' ')))
    B = list(map(int,data[3*i+2].split(' ')))
    res = solve(A,B,N,K)
    # print(A,B,K,res)
    ans.append(f'Case #{i+1}: {res}')

with open('Round1/problemA/output_A.txt', 'w') as filehandle:
    for listitem in ans:
        filehandle.write('%s\n' % listitem)