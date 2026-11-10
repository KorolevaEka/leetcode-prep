def find_pair(durations: list[int], slot: int) -> tuple[int, int] | None:
    for i in range(len(durations)):
        for j in range(i + 1, len(durations)):
            if durations[i] + durations[j] == slot:
                return (i, j)
    return None
