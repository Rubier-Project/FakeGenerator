from fake_useragent import FakeUserAgent
from typing import Literal

browsers = Literal["chrome", "edge", "firefox", "safari"]
oss = Literal["windows", "macos", "linux", "android", "ios"]
platforms = Literal["pc", "mobile", "tablet"]

class GeneratorsClient(object):
    def __init__(self, browser: browsers, os: oss, platform: platforms):
        self.fake = FakeUserAgent(browsers=browser, os=os, platforms=platform)

    async def generate(self):
        return self.fake.random