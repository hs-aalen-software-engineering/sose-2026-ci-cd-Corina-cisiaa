"""
Road profile generation.

This module handles generation of road profiles using various mathematical
curves (currently clothoid-like approximations).

All functions are pure (no side effects) and depend only on numpy.
"""

import numpy as np


def generate_road_profile(num_points: int = 100, x_max: float = 80) -> tuple[np.ndarray, np.ndarray]:
    """
    Generate a road profile using a clothoid-like approximation.

    A clothoid (Euler spiral) is a curve whose curvature increases linearly
    with its arc length. This function approximates it with a polynomial curve.

    Parameters
    ----------
    num_points : int, optional
        Number of points to generate (default: 100)
    x_max : float, optional
        Maximum x-coordinate value (default: 80)

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        x and y coordinates of the road profile

    Examples
    --------
    >>> x, y = generate_road_profile(num_points=50, x_max=40)
    >>> len(x)
    50
    >>> x[0], y[0]
    (0.0, 0.0)
    """
    # Generate equidistant x points from 0 to x_max
    x = np.linspace(0, x_max, num_points)

    # Create a clothoid-like curve using a combination of polynomial and sinusoidal terms
    # This creates a road that starts flat and gradually curves
    # Normalize x for the calculation
    x_norm = x / x_max

    # Clothoid approximation: starts flat, gradually increases curvature
    # Scale to keep maximum height around 8m (realistic road profile)
    y = 0.015 * x_norm**3 * x_max + 0.3 * np.sin(2 * np.pi * x_norm) + 0.035 * x_norm * x_max

    # Ensure it starts at (0, 0)
    y = y - y[0]

    return x, y
