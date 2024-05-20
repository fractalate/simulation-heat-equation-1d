# Simulation of the Heat Equation in One Dimension

(**DRAFT**)

This is a simulation of the heat equation in one dimension.

<p align="center">
  <img src="images/heat_diffusion.gif" alt="Heat Diffusion Demo">
</p>

## Overview

The heat equation relates the change in heat over time to how the heat varies inside the material. It is expressed in the following way

$$
\frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2}
$$

where $u(x, t)$ is a function describing the heat at position $x$ at time $t$ and $\alpha$ is the thermal diffusivity of the medium.

## Method

### Finite Difference, Backward

In this method, approximations for the two differential terms are obtained and combined to produce an equation relating one approximate value in the previous step to a linear combination of three approximate values in the next step. This is often expressed as a matrix equation

$$
\begin{align*}
A \mathbf{w}^t = \mathbf{w}^{t-1}
\end{align*}
$$

where $\mathbf{w}^t$ is a vector representing approximations of $u(x, t)$ at time $t$ and $A$ is the matrix encoding the linear combination for each value in the approximation. To go from step $t-1$ to step $t$, the equation is solved for $\mathbf{w}^t$.

---

Let $h$ be a fixed distance (step length) that we will use for finite differences in $x$. Let $i$ index the $x$ portion of the domain where each $x_i$ has distance $h$ from its preceding and following neighbors. Similarly let $k$ be a fixed duration (time step) that we will use for finite differences in $t$. Let $j$ index the $t$ portion of the domain as equidistant values, $t_j$.

An expression for $\frac{\partial u}{\partial t}$ is found by using the second partial derivative in the series expansion of the Lagrange polynomial approximating $u(x, t)$ at $t_{j-1}$ and $t_j$ with respect to $t$ and expressing it as a backward difference quotient with error term:

$$
\begin{align*}
\frac{\partial u}{\partial t}(x_i, t_j) = \frac{u(x_i, t_j) - u(x_i, t_{j-1})}{k} + \frac{k}{2} \frac{\partial^2 u}{\partial x^2}(x_i, \mu_j)
\end{align*}
$$

where $t_{j-1} < \mu_j < t_j$.

An expression for $\frac{\partial^2 u}{\partial x^2}$ is found similarly by using the second partial derivative from the series expansion of the Lagrange polynomial approximating $u(x, t)$ at $x_{i-1}$, $x_i$, and $x_{i+1}$ with respect to $x$ and expressing it as a midpoint difference quotient with error term:

$$
\begin{align*}
\frac{\partial^2 u}{\partial x^2}(x_i, t_j) = \frac{u(x_{i+1}, t_j) - 2u(x_i, t_j) + u(x_{i-1}, t_j)}{h^2} + \frac{h^2}{12} \frac{\partial^4 u}{\partial x^4}(\xi_i, t_j)
\end{align*}
$$

where $x_{i-1} < \xi_i < x_{i+1}$.

Let $w_{ij} \approx u(x_i, t_j)$ represent the approximations of $u(x_i, t_j)$. Substituting the expressions found into the differential equation and dropping the truncation error produces the following equation

$$
\begin{align*}
\frac{w_{ij} - w_{ij-1}}{k} = \alpha \frac{w_{i+1 j} - 2w_{ij} + w_{i-1 j}}{h^2}.
\end{align*}
$$

Let $r$ represent the quantity $\alpha \frac{k}{h^2}$ and the equation can be rearranged into the following form

$$
\begin{align*}
(1 + 2r) w_{ij} - r w_{i+1 j} - r w_{i-1 j} = w_{ij-1}.
\end{align*}
$$

which relates three adjacent points at time $t_j$ with one point at time $t_{j-1}$. This can be expressed as a matrix equation

$$
\begin{pmatrix}
1 + 2r &     -r & \cdots &      0 &      0 \\
    -r & 1 + 2r & \cdots &      0 &      0 \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
     0 &      0 & \cdots & 1 + 2r &     -r \\
     0 &      0 & \cdots &     -r & 1 + 2r
\end{pmatrix}\begin{pmatrix}
w_{0j} \\
w_{1j} \\
\vdots \\
w_{N-1j} \\
w_{Nj}
\end{pmatrix} = \begin{pmatrix}
w_{0j-1} \\
w_{1j-1} \\
\vdots \\
w_{N-1j-1} \\
w_{Nj-1}
\end{pmatrix}
$$

or more concisely as $A \textbf{w}^{t} = \textbf{w}^{t-1}$ and "out-of-bounds" elements are treated like $0$ (e.g. $w_{i-1 j}$ when $i = 0$).

Applying the method involves solving the matrix equation for $\mathbf{w}^t$ at each step of the simulation. This is generally an $O(N^3)$ operation, but for a tridiagonal matrix like we have, it can be done as an $O(N)$ operation.

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
