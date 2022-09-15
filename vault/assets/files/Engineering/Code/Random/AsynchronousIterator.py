# %%
import asyncio

async def all_keys(key):

    keys = {"key1": 1234, "key2": 2345, 
            "key3": 3456, "key4": 4567, 
            "key5": 5678}

    return keys.get(key)



class KeyTaker:

    def __init__(self, keys):
        self.keys = keys

    def __aiter__(self):
        # create an iterator of the input keys
        self.iter_keys = iter(self.keys)
        return self

    async def __anext__(self):
        try:
            # extract the keys one at a time
            k = next(self.iter_keys)
        except StopIteration:
            # raise stopasynciteration at the end of iterator
            raise StopAsyncIteration
        # return values for a key
        value = await all_keys(k)

        return value


async def main():
    async for c in KeyTaker(["key1", "key2", "key3"]):
        print(c)

asyncio.run(main())
# %%
