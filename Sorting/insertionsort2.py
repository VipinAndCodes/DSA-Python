# ex1.0.1 Measuring algorithm performance
import timeit
from random import randint


def run_sorting(algorithm, nts):
    setup_code = f"from __main__ import {algorithm}"

    stmt = f"{algorithm}({nts})"

    # repeat specifies the number of samples to take
    # number specifies the number of times to repeat the code for each sample.
    time = timeit.repeat(stmt=stmt, setup=setup_code, repeat=1, number=1)

    print(f"Quickest execution time: {min(time)}")

def insertion_sort(nts):

    for i in range(1, len(nts)):
        current_num = nts[i]

        p = i - 1

        while p >= 0 and nts[p] > current_num:
            nts[p + 1] = nts[p]
            p -= 1

        nts[p + 1] = current_num

def bubbleSort(nts):

    nts_len = len(nts)

    for i in range(len(nts)):
        for p in range(nts_len - i - 1):
            if nts[p] > nts[p + 1]:
                nts[p], nts[p + 1] = nts[p + 1], nts[p]


if __name__ == "__main__":

    nts = [randint(0, 10000) for i in range(5000)]
    run_sorting(algorithm="insertion_sort", nts=nts)
