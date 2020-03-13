import math
import sys
from os import rename

import requests

print(sys.version)
# print(sys.executable)
print('Hello Itauma')


class Awesome(object):
    def greet(self, who_to_greet):
        print(f'Hello, {who_to_greet}')


if __name__ == "__main__":
    # a = Awesome()
    # a.greet("World")
    # a.greet("Mighty")
    r = requests.get('http://gralswerk.org')
    print(r.status_code)
