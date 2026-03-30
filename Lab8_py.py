#6316774
#d1=4
#d2=7
#k = (7 + 4) % 4 + 2 = 3
#shift = 4 - 7 = -3
#rows_keep = (4 % 2) + 2 = 2

#Part A
from os import path
import numpy as np
import math
def read_oscillatory_wave_data(filename):
    data = np.genfromtxt(filename, delimiter=",", skip_header=1)
 
    #data = np.loadtxt(filename, delimiter=',')  # Assuming CSV format
    lengths = data[:, 0]
    amplitudes = data[:, 1]
    mean_amp = np.mean(amplitudes)
    max_amp = np.max(amplitudes)
    return lengths, amplitudes, mean_amp, max_amp


def read_standing_wave_data(filename):
    data = np.genfromtxt(filename, delimiter=",", skip_header=1)
    lengths = data[:, 0]
    tensions = data[:, 1]
    speeds = np.sqrt(tensions / 1)
    return lengths, tensions, speeds


def main():
    # Personalized values
    d1 = 4
    d2 = 7
    k = 3
    shift = -3
    rows_keep = 2

    osc_file = "oscillatory_2672601.csv"
    stand_file = "standing_2672601.csv"
 

    lengths1, amplitudes, mean_amp, max_amp = read_oscillatory_wave_data(osc_file)

    print("Original oscillatory amplitudes:", amplitudes)
    print("Original mean amplitude:", mean_amp)
    print("Original max amplitude:", max_amp)

    new_amplitudes = amplitudes + shift
    new_mean_amp = np.mean(new_amplitudes)
    new_max_amp = np.max(new_amplitudes)

    print("\nShifted amplitudes:", new_amplitudes)
    print("New mean amplitude:", new_mean_amp)
    print("New max amplitude:", new_max_amp)

    lengths2, tensions, speeds = read_standing_wave_data(stand_file)

    print("\nOriginal tensions:", tensions)
    print("Original wave speeds:", speeds)

    new_tensions = tensions * k
    new_speeds = np.sqrt(new_tensions / 1)

    print("\nScaled tensions:", new_tensions)
    print("New wave speeds:", new_speeds)

    print("\nManual oscillatory check using first 3 amplitudes:")
    print("Original first 3 amplitudes:", amplitudes[:3])
    print("Shifted first 3 amplitudes:", new_amplitudes[:3])

    print("\nManual standing-wave check using first row:")
    print("First tension =", tensions[0])
    print("Scaled first tension =", new_tensions[0])
    print("First new speed =", math.sqrt(new_tensions[0]))

#Part B
#I modified the CSV file
#rows_oscillatory = 5 + 7 = 12
#rows_standing = 4 + 2 = 6

    rows_osc = 5 + d2   # 12 rows
    new_amplitudes = amplitudes[:rows_osc] + shift

    new_mean_amp = np.mean(new_amplitudes)
    new_max_amp = np.max(new_amplitudes)

    print("\nOscillatory (Modified)")
    print("Rows used:", rows_osc)
    print("Shift:", shift)
    print("New amplitudes:", new_amplitudes)
    print("New mean:", new_mean_amp)
    print("New max:", new_max_amp)

    # Standing wave modifications
    rows_stand = 4 + rows_keep   # 6 rows
    new_tensions = tensions[:rows_stand] * k
    new_speeds = np.sqrt(new_tensions / 1)

    print("\nStanding Wave (Modified)")
    print("Rows used:", rows_stand)
    print("Scale factor k:", k)
    print("New tensions:", new_tensions)
    print("New speeds:", new_speeds)


if __name__ == "__main__":
    main()
