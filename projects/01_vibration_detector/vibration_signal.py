"""Generate a simple vibration signal from a rotating imbalance."""

import numpy as np


def vibration_signal(
    time: np.ndarray,
    mass: float,
    radius: float,
    speed_rpm: float,
) -> np.ndarray:
    """Return the ideal radial force produced by a rotating imbalance."""
    omega = 2 * np.pi * speed_rpm / 60
    force = mass * radius * omega**2
    return force * np.sin(omega * time)


if __name__ == "__main__":
    time = np.linspace(0, 1, 2000)

    signal = vibration_signal(
        time=time,
        mass=0.01,
        radius=0.02,
        speed_rpm=1800,
    )

    print(f"Peak force: {np.max(np.abs(signal)):.3f} N")
    print(f"Samples: {len(signal)}")
