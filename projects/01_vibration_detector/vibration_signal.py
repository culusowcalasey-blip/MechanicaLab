"""Simulate and analyze vibration from rotating imbalance."""

import numpy as np
import matplotlib.pyplot as plt


def vibration_signal(time, mass, radius, speed_rpm):
    omega = 2 * np.pi * speed_rpm / 60
    force = mass * radius * omega**2
    return force * np.sin(omega * time)


def peak_force(mass, radius, speed_rpm):
    omega = 2 * np.pi * speed_rpm / 60
    return mass * radius * omega**2


def dominant_frequency(signal, sample_rate):
    frequencies = np.fft.rfftfreq(len(signal), 1 / sample_rate)
    spectrum = np.abs(np.fft.rfft(signal))
    index = np.argmax(spectrum[1:]) + 1
    return frequencies[index]


if __name__ == "__main__":
    sample_rate = 2000
    time = np.arange(0, 1, 1 / sample_rate)

    cases = [
        ("Low imbalance", 0.005, 0.02, 1800),
        ("Baseline", 0.010, 0.02, 1800),
        ("High imbalance", 0.020, 0.02, 1800),
    ]

    fig, axes = plt.subplots(3, 1, figsize=(9, 8), sharex=True)

    for ax, (name, mass, radius, speed_rpm) in zip(axes, cases):
        signal = vibration_signal(time, mass, radius, speed_rpm)
        force = peak_force(mass, radius, speed_rpm)
        frequency = dominant_frequency(signal, sample_rate)

        ax.plot(time[:400], signal[:400])
        ax.set_ylabel("Force (N)")
        ax.set_title(
            f"{name}: peak={force:.3f} N, dominant frequency={frequency:.1f} Hz"
        )
        ax.grid(True)

    axes[-1].set_xlabel("Time (s)")
    fig.tight_layout()
    fig.savefig("projects/01_vibration_detector/results/vibration_comparison.png", dpi=160)
    plt.close()

    print("Saved results/vibration_comparison.png")
