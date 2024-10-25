from . import generators
from . import randomize

browsers = generators.browsers
oss = generators.oss
platforms = generators.platforms

class Loops(object):
    def __init__(self):
        self.randomize = randomize.Randomize()

    async def once(self, browsers: browsers, os: oss, platform: platforms) -> str:
        return await generators.GeneratorsClient(browser=browsers, os=os, platform=platform).generate()
    
    async def createList(self, browsers: browsers, os: oss, platform: platforms, length: int = 100) -> dict:
        fname = await self.randomize.createRandomFileName()

        try:
            with open(fname, "a") as file:
                for agent in range(length):
                    data = await self.once(browsers, os, platform)
                    file.write(data+"\n")
                
                file.close()
            return {"status": "OK", "file_name": fname}
        except Exception as OpenError:
            return {"status": "OpenError", "message": str(OpenError)}