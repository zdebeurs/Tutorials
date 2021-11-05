# Code modified from Konrad Hafen
# link to full article: https://towardsdatascience.com/asynchronous-parallel-programming-in-python-with-multiprocessing-a3fc882b4023

import multiprocessing as mp
import numpy as np
import time
from my_function import my_function

def get_result(result):
    global results
    results.append(result)


if __name__ == '__main__':
    params = np.random.random((10, 3)) * 100.0
    results = []
    ts = time.time()
    for i in range(0, params.shape[0]):
        get_result(my_function(i, params[i, 0], params[i, 1], \
                               params[i, 2]))
    print('Time in serial:', time.time() - ts)
    print(results)

    results = []
    ts = time.time()
    pool = mp.Pool(mp.cpu_count())
    for i in range(0, params.shape[0]):
        pool.apply_async(my_function, args=(i, params[i, 0], params[i, \
                                                                    1], params[i, 2]), callback=get_result)
    pool.close()
    pool.join()
    print('Time in parallel:', time.time() - ts)
    print(results)