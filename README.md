# Simulation Heat Equation (1 Dimension)

(**DRAFT**)

This is a simulation of the heat equation in one dimension.

<p align="center">
  <img src="images/heat_diffusion.gif" alt="Heat Diffusion Demo">
</p>

## Overview

The heat equation relates the change in temperature over time to changing differences in temperature at a distance. It expressed in the following way

$$
\frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2}
$$

where $u(x, t)$ is a function describing the heat at position $x$ at time $t$ and $\alpha$ is the thermal diffusivity of the medium.

### Model

* $u(x)$ is heat at position $x$ in the "rod".
* $\alpha$ is the thermal diffusivity of the entire medium, which is constant.
* The domain of $u$ is split into $N$ bins, each corresponding to a range of uniformly sized intervals around $x$. E.g. if there are $N$ bins and the total "rod" length is 1 cm, then the $k^{\text{th}}$ index satisfies
  $\frac{1 \, \text{cm}}{N} \cdot k \le x_k < \frac{1 \, \text{cm}}{N} \cdot (k + 1)$.
* The values for $u(x)$ are stored in an array indexed by $k$.

### Simulation

The simulation implements the [Crank-Nicolson Method](https://en.wikipedia.org/wiki/Crank%E2%80%93Nicolson_method) to calculate the numeric approximations of the evolving heat dispersion over time. This method was chosen for its known stability and well-behaved error term, $O(dt^2 + dx^2)$ (TODO: make sure this is the case even though I deviated from the tridiagonal matrix setup and solving method presented in Burden and Faires Numerical Analysis, 9e).

## Setup

The following Python libraries are required to run the simulation:

```
pip install numpy scipy matplotlib
```

Additionally, ffmpeg is required to render video files. You can get this on Debian with the following command:

```
apt-get install ffmpeg
```

See [requirements.txt](./requirements.txt) for full dependency details.

## Running

To run the simulations, run the [simulate.py](./simulate.py) script with the demo you are interested in.

```
python3 simulate.py heat_diffusion
```

This one will generate `heat_diffusion.mp4` which you can then watch.

## Development

Use GNU make to build the static assets presented in the repository:

```
make
```
