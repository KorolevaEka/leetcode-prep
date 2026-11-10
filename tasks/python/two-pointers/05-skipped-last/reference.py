def skipped_last(results: list[str]) -> list[str]:
    out = list(results)
    write = 0
    for read in range(len(out)):
        if out[read] != "skipped":
            out[write], out[read] = out[read], out[write]
            write += 1
    return out
