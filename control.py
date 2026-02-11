import sys
import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from colorama import init, Fore

init(autoreset=True)

def record_audio(seconds, rate=16000):
    p = pyaudio.PyAudio()
    stream = p.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=rate,
        input=True,
        frames_per_buffer=1024
    )

    frames = []
    for _ in range(int(rate / 1024 * seconds)):
        frames.append(stream.read(1024, exception_on_overflow=False))

    stream.stop_stream()
    stream.close()
    p.terminate()

    return b"".join(frames), rate


def analyze_audio(data, rate):
    samples = np.frombuffer(data, dtype=np.int16)
    energy = float(np.mean(samples.astype(np.float64) ** 2))
    return {
        "samples": samples,
        "duration": len(samples) / rate,
        "avg_volume": float(np.mean(np.abs(samples))),
        "max_amplitude": int(np.max(np.abs(samples))),
        "energy": energy
    }


def compare_audio(a,b):
    print(Fore.CYAN + "\nComparasion Result")
    print(Fore.CYAN + "-" * 40)

    duration_diff = abs(a["duration"] - b["duration"]) / min(a["duration"], b["duration"]) * 100
    volume_diff = abs(a["avg_volume"] - b["avg_volume"]) / min(a["avg_volume"], b["avg_volume"]) * 100
    energy_diff = abs(a["energy"] - b["energy"]) / min(a["energy"], b["energy"]) * 100
    print("Longer Recording      :", "File 1" if a["duration"] > b["duration"] else "File 2")
    print("Duration Difference % :", f"{duration_diff:.2f}")

    print("Louder Recording      :", "File 1" if a["avg_volume"] > b["avg_volume"] else "File 2")
    print("Volume Difference %   :", f"{volume_diff:.2f}")

    print("Higher Peak Amplitude :", "File 1" if a["max_amplitude"] > b["max_amplitude"] else "File 2")
    print("Higher Signal Energy  :", "File 1" if a["energy"] > b["energy"] else "File 2")
    print("Energy Difference %   :", f"{energy_diff:.2f}")
def plot_comparison(a, b, rate):
    t1 = np.linspace(0, a["duration"], len(a["samples"]))
    t2 = np.linspace(0, b["duration"], len(b["samples"]))

    plt.figure(figsize=(12, 6))
    plt.plot(t1, a["samples"], linewidth=0.5, label="File 1")
    plt.plot(t2, b["samples"], linewidth=0.5, label="File 2")

    plt.title("Audio Waveform Comparison")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
def main():
    print(Fore.CYAN + "=" * 40)
    print(Fore.CYAN + "========= AUDIO COMPARE SYSTEM =========")
    print(Fore.CYAN + "=" * 40)

    while True:
        user_input = input(
            Fore.YELLOW + "\nEnter recording duration in seconds (or type 'exit'): "
        ).strip().lower()

        if user_input == "exit":
            print(Fore.MAGENTA + "System exit acknowledged. Shutting down gracefully.")
            sys.exit(0)

        if not user_input.isdigit() or int(user_input) <= 0:
            print(Fore.RED + "Invalid input. Please enter a positive number.")
            continue

        seconds = int(user_input)

        print(Fore.GREEN + "\nRecording audio file 1...")
        audio1, rate = record_audio(seconds)
        stats1 = analyze_audio(audio1, rate)

        print(Fore.GREEN + "Recording audio file 2...")
        audio2, _ = record_audio(seconds)
        stats2 = analyze_audio(audio2, rate)

        compare_audio(stats1, stats2)
        plot_comparison(stats1, stats2, rate)
if __name__ == "main":
    main()


            


