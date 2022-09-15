#%%
from collections import Counter
with open ("second_hands_input.txt", "r") as myfile:
    data = myfile.read().splitlines()
    T = int(data[0])
    data = data[1:]
res = []
for i in range(0,2*T,2):
    N, K = tuple(map(int,data[i].split(' ')))
    arr = list(map(int,data[i+1].split(' ')))
    s = f'Case #{(i+2)//2}: '
    c = Counter(arr)
    val = 'YES'
    if any(v > 2 for v in c.values()) or len(arr) > 2*K: val = 'NO'
    print(s+val)
    res.append(s+val)

with open('output_A.txt', 'w') as filehandle:
    for listitem in res:
        filehandle.write('%s\n' % listitem)