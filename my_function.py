import os
import sys
import numpy as np
import time

def my_function(i, param1, param2, param3):
    result = param1 ** 2 * param2 + param3
    time.sleep(1)
    return (i, result)
