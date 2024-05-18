import numpy as np

def empty(N):
    return np.zeros(N)

def example_first_half(N):
    result = np.zeros(N)
    result[0:N//2] = 1.0
    return result

def example_second_half(N):
    result = np.zeros(N)
    result[N//2:0] = 1.0
    return result

def example_middle_fifth(N):
    result = np.zeros(N)
    result[N//5*2:N//5*3] = 1.0
    return result

def example_two_separated_fifths(N):
    result = np.zeros(N)
    result[N//5*1:N//5*2] = 1.0
    result[N//5*3:N//5*4] = 1.0
    return result
