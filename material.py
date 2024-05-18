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

class Material:
    def __init__(self, temperature: np.array, density: np.array = None, specific_heat: np.array = None, thermal_conductivity: np.array = None):
        """
        Create the new material. Each provided array should have the same shape.
        This class takes ownership of the arrays passed to it, so be sure to .copy()
        if that presents an issue to your use case.

        @param temperature - The temperature of the material at each position.
        @param density - The density of the material at each position.
        @param specific_heat - The specific heat capacity of the material at each position.
        @param thermal_conductivity - The thermal conductivity of the material at each position.
        """
        self.temperature = temperature
        self.density = np.full(temperature.shape, 1.0) if density is None else density
        self.specific_heat = np.full(temperature.shape, 1.0) if specific_heat is None else specific_heat
        self.thermal_conductivity = np.full(temperature.shape, 1.0) if thermal_conductivity is None else thermal_conductivity
