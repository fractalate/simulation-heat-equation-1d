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

### Methods

#### Finite Difference (Backward)

An expression for $\frac{\partial u}{\partial t}$ is found via taking partial derivative of the Lagrange polynomial approximating $u(x, t)$ with respect to $t$ and expressing it as a backward difference quotient with error term:

$$
\begin{align*}
\frac{\partial u}{\partial t}(x_i, t_j) = \frac{u(x_i, t_j) - u(x_i, t_{j-1})}{k} + \frac{k}{2} \frac{\partial^2 u}{\partial x^2}(x_i, \mu_j)
\end{align*}
$$

where $t_{j-1} < \mu_j < t_j$.

An expression for $\frac{\partial^2 u}{\partial x^2}$ is found similarly by taking the second partial derivative of the Lagrange polynomial approximating $u(x, t)$ with respect to $x$ and expressing it as a midpoint difference quotient with error term:

$$
\begin{align*}
\frac{\partial^2 u}{\partial x^2}(x_i, t_j) = \frac{u(x_{i+1}, t_j) - 2u(x_i, t_j) + u(x_{i-1}, t_j)}{h^2} + \frac{h^2}{12} \frac{\partial^4 u}{\partial x^4}(\xi_i, t_j)
\end{align*}
$$

where $x_{i-1} < \xi_i < x_{i+1}$.

Following convention, we let $w_{ij} \approx u(x_i, t_j)$ represent the approximations of $u(x_i, t_j)$. Substituting the expressions found into the differential equation and dropping the truncation error produces the following equation

$$
\begin{align*}
\frac{w_{ij} - w_{ij-1}}{k} = \alpha^2 \frac{w_{i+1 j} - 2w_{ij} + w_{i-1 j}}{h^2}.
\end{align*}
$$

### Model

* $u(x)$ is heat at position $x$ in the "rod".
* $\alpha$ is the thermal diffusivity of the entire medium, which is constant.
* The domain of $u$ is split into $N$ bins, each corresponding to a range of uniformly sized intervals around $x$. E.g. if there are $N$ bins and the total "rod" length is 1 cm, then the $i^{\text{th}}$ index satisfies
  $\frac{1 \, \text{cm}}{N} \cdot i \le x_i < \frac{1 \, \text{cm}}{N} \cdot (i + 1)$.
* The values for $u(x)$ are stored in an array indexed by $i$.
* The endpoints of the rod are assumed to be a fixed heat of $0$.
* The small step in space is labeled $h$, but is named `dx` in the code.
* The small step in time is labeled $k$, but is named `dt` in the code.

### Simulation

The simulation implements a [](https://en.wikipedia.org/wiki/Finite_difference_method) utilizing the backward difference to calculate the numeric approximations of the evolving heat dispersion over time. This method was chosen for its known stability and well-behaved error term, $O(k + h^2)$.

## Setup

The following Python libraries are required to run the simulation:

```
pip install numpy scipy matplotlib
```

See [requirements.txt](./requirements.txt) for full Python dependency details.

Additionally, ffmpeg is required to render video files. You can get this on Debian with the following command:

```
apt-get install ffmpeg
```

## Running

To run the simulations, run the [simulate.py](./simulate.py) script with the demo you are interested in.

```
python3 simulate.py heat_diffusion
```

This one will generate `heat_diffusion.mp4` which you can then watch.

The following demos are available:

* `basic`
* `heat_diffusion`
* `heat_diffusion_silver`

## Development

Use GNU make to build the static assets presented in the repository:

```
make
```
