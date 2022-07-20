import time

from threading import Thread


def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(
            "================================================================="
        )
        print("function {} using time: {:.5f}".format(func.__name__,
                                                      end - start)
        return res
    return wrapper


class ThreadWithReturnValue(Thread):

    def __init__(self,
                 group=None,
                 target=None,
                 name=None,
                 args=(),
                 kwargs={},
                 Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        # print(type(self._target))
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self, *args):
        Thread.join(self, *args)
        return self._return

def hex_to_word(hex_str, mode='UTF-8')
    data = bytes.fromhex(hex_str[2:])
    data = data.decode(mode)
    return data
