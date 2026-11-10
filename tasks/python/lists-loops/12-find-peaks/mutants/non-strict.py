def find_peaks(load: list[int]) -> list[int]:
    return [i for i in range(1, len(load) - 1) if load[i] >= load[i - 1] and load[i] >= load[i + 1]]
