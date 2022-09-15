#%%
from sortedcontainers import SortedList

sl = SortedList()
sl.update([5, 1, 3, 4, 2])
sl.remove(5)
# sl.pop()
sl.add(0)
# %%
# Built atop Python’s built-in dict data type and SortedList is the mutable mapping data type SortedDict. Sorted dict keys are maintained in sorted order.
from sortedcontainers import SortedDict

sd = SortedDict()
sd.update({"d": 3, "c": 4})
# %%
