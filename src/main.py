from numpy import ndarray
from numpy.fft import fft
from numpy.random import randn

from src.time import clock


def anothersuperfeature():
    return 300

def mynewfeature():
    return 100

@clock
def fft_array(arr: ndarray):
    return fft(arr)


if __name__ == '__main__':
    arr = randn(1000000 - 1)
    res = fft_array(arr)
