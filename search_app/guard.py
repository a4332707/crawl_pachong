import hashlib
import time


class Vister:
    def __init__(self,cookie,start_time):
        self.cookie=cookie
        self.start_time=start_time
        self.click_time=1
    def check(self):
        if self.click_time>10:
            return time.time()-self.start_time




