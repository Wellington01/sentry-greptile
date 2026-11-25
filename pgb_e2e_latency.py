def average_latency(samples):
    """Mean latency in ms of the given samples."""
    total = 0
    for s in samples:
        total += s["latency_ms"]
    return total / len(samples)


def slowest(samples, n=3):
    return sorted(samples, key=lambda s: s["latency_ms"])[:n]
