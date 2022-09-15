#%%
from collections import Counter
from re import I
with open ("second_friend_input.txt", "r") as myfile:
    data = myfile.read().splitlines()
    T = int(data[0])
    data = data[1:]

inputs = []
line = 0
while line < len(data):
    r,c = tuple(map(int,data[line].split(' ')))
    inputs.append(data[line+1:line+r+1])
    line += r+1

res = []
for i in range(T):
    s = f'Case #{i+1}: '
    scene = inputs[i]
    m,n = len(scene),len(scene[0])
    val = 'Possible'
    if (m == 1 or n == 1) and any('^' in row for row in scene):
        val = 'Impossible'
    res.append(s+val)
    if val == 'Possible':
        if not (m==1 or n==1):
            for _ in range(m):
                res.append('^'*n)
        else:
            for _ in range(m):
                res.append('.'*n)


with open('output_B.txt', 'w') as filehandle:
    for listitem in res:
        filehandle.write('%s\n' % listitem)
# %%
