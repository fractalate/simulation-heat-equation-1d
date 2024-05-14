import sys

import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# TODO: Rename this. This is confusable with sys.
import system

def print_samples(samples, prefix = '', postfix = ''):
    print(prefix + ', '.join(['{:.2f}'.format(s) for s in samples]) + postfix)

def dump_samples(samples, out_name):
    with open(out_name, 'w') as fout:
        for sample in samples:
            fout.write(str(sample) + '\n')

class Simulation:
    """A base class for all simulations."""

    def copy(self):
        raise NotImplementedError()

    def iterate(self):
        raise NotImplementedError()

class SimulationCrankNicholson(Simulation):
    def __init__(self, samples: np.array, alpha: float, dx: float, dt: float):
        Simulation.__init__(self)

        self.samples: np.array = samples
        self.alpha: float = alpha
        self.dx: float = dx
        self.dt: float = dt

        self.r: float = alpha * dt / dx**2

    def copy(self):
        return SimulationCrankNicholson(self.samples.copy(), self.alpha, self.dx, self.dt)

    def iterate(self):
        # Solve the tridiagonal matrix with linalg.solve_banded().
        # Instead of being organized as a triangular matrix, the
        # relevant diagonals are stacked vertically.
        # TODO: a, b, c, and ab can be pre-calculated.
        a = np.full(len(self.samples), -self.r)
        b = np.full(len(self.samples), 1 + 2*self.r)
        c = np.full(len(self.samples), -self.r)
        a[0] = c[-1] = 0 # And these elements should be zero.
        ab = np.vstack((a, b, c))
        self.samples = linalg.solve_banded((1, 1), ab, self.samples)

def setup_basic():
    LENGTH = 0.1
    SAMPLES = 10
    samples = system.example_two_separated_fifths(SAMPLES)
    return SimulationCrankNicholson(
        samples,
        alpha = 1,
        dx = LENGTH / SAMPLES,
        dt = 0.00001,
    )

def demo_basic():
    sim = setup_basic()
    print_samples(sim.samples)
    sim.iterate()
    print_samples(sim.samples)
    sim.iterate()
    print_samples(sim.samples)
    sim.iterate()
    print_samples(sim.samples)

def setup_heat_diffusion():
    LENGTH = 0.1
    SAMPLES = 10000
    samples = system.example_two_separated_fifths(SAMPLES)
    return SimulationCrankNicholson(
        samples,
        alpha = 1,
        dx = LENGTH / SAMPLES,
        dt = 0.0000001,
    )

def demo_heat_diffusion():
    sim = setup_heat_diffusion()

    fig, ax = plt.subplots()
    
    ax.set_title("Heat Diffusion")
    line, = ax.plot(sim.samples)

    def update(frame_number):
        sim.iterate()
        line.set_ydata(sim.samples)
        return line,

    ani = FuncAnimation(fig, update, frames=750, blit=True)
    ani.save('heat_diffusion.mp4', writer='ffmpeg', fps=60)
    print('saved heat_diffusion.mp4')

demos = {
    "basic": demo_basic,
    "heat_diffusion": demo_heat_diffusion,  
}

def print_usage(file=None):
    print('Usage: {} [{}]'.format(sys.argv[0], '|'.join(demos.keys())), file=file)
    print('This will run the simulation with the given name.', file=file)

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print_usage(file=sys.stderr)
        sys.exit(1)
    demo = demos.get(sys.argv[1])
    if demo is None:
        print_usage(file=sys.stderr)
        print('Demo named {} not found.'.format(repr(sys.argv[1])), file=sys.stderr)
        sys.exit(1)
    demo()

if __name__ == '__main__':
    main()
