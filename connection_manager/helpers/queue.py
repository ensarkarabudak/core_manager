
class Queue(object):

    sub = 0
    base = 0
    success = 0
    fail = 0
    interval = 0
    is_ok = False

    def set_step(self, sub, base, success, fail, interval, is_ok):
        self.sub = sub
        self.base = base
        self.success = success
        self.fail = fail
        self.interval = interval
        self.is_ok = is_ok

queue = Queue()

