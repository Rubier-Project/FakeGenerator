import random
import string

class Randomize(object):
    def __init__(self):pass

    async def createUnexceptedString(self) -> str:
        us = string.ascii_lowercase + string.ascii_uppercase
        _str = ''.join(random.choice(us) for _ in range(32))
        return _str

    async def createRandomFileName(self, format: str = "txt"):
        unexcepted_string = await self.createUnexceptedString()
        return unexcepted_string + format