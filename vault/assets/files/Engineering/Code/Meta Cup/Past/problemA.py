from collections import Counter
import string
with open ("consistency_chapter_1_input.txt", "r") as myfile:
    data = myfile.read().splitlines()
    T = int(data[0])
    data = data[1:]

def compute(val,arr):
    vowels = 'AEIOU'
    seconds = 0
    for ch in arr:
        if ch == val: continue
        if (ch in vowels) ^ (val in vowels):
            seconds += 1
        else:
            seconds += 2
    return seconds

res = []
for i in range(T):
    arr = data[i]
    c = Counter(arr)
    val = float('inf')
    for ch in string.ascii_letters:
        val = min(val,compute(ch,arr))
    s = f'Case #{i+1}: '
    res.append(s+str(val))
with open('output_A.txt', 'w') as filehandle:
    for listitem in res:
        filehandle.write('%s\n' % listitem)